import requests
import pytest
from ideas_for_test.hillel_test_api.hillel_api import auth, users, cars, expenses

s = requests.session()
new_s = requests.session()


@pytest.fixture()
def user_data():
    """Default data for user"""
    data = {
        'name': 'Tori',
        'lastName': 'Smyrnova',
        'email': 'tori42@te.st',
        'password': 'Qwerty12345',
        'repeatPassword': 'Qwerty12345'
    }
    return data


@pytest.fixture()
def car_data():
    """Default data for car"""
    car_data = {
        'carBrandId': 4,  # Porsche
        'carModelId': 17,  # Cayenne
        'mileage': 200
    }
    return car_data


@pytest.fixture()
def expenses_data(car, car_data):
    """Default data for expense"""
    data = {
        'carId': car['data']['id'],
        'reportedAt': '2024-02-14',
        'mileage': car_data['mileage'] + 1,
        'liters': 50,
        'totalCost': 50,
        'forceMileage': False
    }
    return data


@pytest.fixture()
def user(user_data):
    """Sing up and sing in user before test and delete user after it"""
    auth.signup(s, user_data)
    data_sign_in = {
        'email': user_data['email'],
        'password': user_data['password'],
        'remember': False
    }
    auth.signin(s, data_sign_in)
    yield
    users.users(s)


@pytest.fixture()
def car(car_data):
    """Creating car before test and delete car after it"""
    new_car = cars.cars_post(s, car_data)
    yield new_car.json()
    car_id = {'id': new_car.json()['data']['id']}
    cars.cars_id_delete(s, car_id)


"""AUTH SIGN UP"""


def test_auth_signup_01(user_data):
    """Positive test that the user can Sign up with valid data"""
    new_user = auth.signup(s, user_data)

    assert new_user.status_code == 201
    assert new_user.json()['status'] == 'ok'
    assert new_user.json().get('data', {}).get('userId', int)
    assert new_user.json().get('data', {}).get('distanceUnits', 'km')
    assert new_user.json().get('data', {}).get('currency', 'usd')
    users.users(s)


def test_auth_signup_02():
    """Negative test that user can't Sign up with invalid data"""
    new_user = auth.signup(s, {})

    assert new_user.status_code == 400
    assert new_user.json()['status'] == 'error'


"""DELETE USER"""


def test_users_delete_user_01(user_data):
    """Positive test that user could be deleted correctly"""
    auth.signup(s, user_data)
    del_user = users.users(s)

    assert del_user.status_code == 200
    assert del_user.json()['status'] == 'ok'


def test_users_delete_user_02(user_data):
    """Negative test that user couldn't be deleted with incorrect session"""
    auth.signup(s, user_data)
    del_user = users.users(new_s)

    assert del_user.status_code == 401
    assert del_user.json()['status'] == 'error'
    assert del_user.json()['message'] == "Not authenticated"


"""UPDATE USER'S PROFILE"""


def test_users_profile_put_01(user):
    """Positive test that user can change profile info with valid data"""
    current_user = users.current(s)
    upd_data = {
        'lastName': 'Sofiyskaya',
        'dateBirth': '2002-01-15T11:00:00.000Z',
    }
    upd_user = users.profile_put(s, upd_data)
    assert upd_user.status_code == 200
    assert upd_user.json()['status'] == 'ok'
    assert upd_user.json()['data']['userId'] == current_user.json().get('data', {}).get('userId', int)
    assert upd_user.json().get('data', {}).get('lastName', 'Sofiyskaya')
    assert upd_user.json().get('data', {}).get('dateBirth', '2002-01-15T11:00:00.000Z')


def test_users_profile_put_02():
    """Negative test that user can't change profile info without authorization"""
    upd_data = {"lastName": "Sofiyskaya"}
    upd_user = users.profile_put(new_s, upd_data)  # incorrect session

    assert upd_user.status_code == 401
    assert upd_user.json()['status'] == 'error'
    assert upd_user.json()['message'] == "Not authenticated"


def test_users_profile_put_03(user):
    """Negative test that user can't change profile info with invalid data"""
    upd_data = {}
    upd_user = users.profile_put(s, upd_data)

    assert upd_user.status_code == 400
    assert upd_user.json()['status'] == 'error'
    assert upd_user.json()['message'] == "Empty body is not allowed"


"""UPDATE USER'S EMAIL"""


def test_users_email_01(user, user_data):
    """Positive test of changing password"""
    upd_email = {
        'email': 'tori_s_42@te.st',
        'password': user_data['password']
    }
    upd_user = users.email(s, upd_email)

    assert upd_user.status_code == 200
    assert upd_user.json()['status'] == 'ok'
    assert upd_user.json().get('data', {}).get('userId', int)


def test_users_email_02(user):
    """Negative test of changing email without authorization"""
    upd_email = {
        'email': 'tori_s_42@te.st',
        'password': 'test'
    }
    upd_user = users.email(new_s, upd_email)  # incorrect session

    assert upd_user.status_code == 401
    assert upd_user.json()['status'] == 'error'
    assert upd_user.json()['message'] == 'Not authenticated'


def test_users_email_03(user):
    """Negative test of changing email with incorrect password"""
    upd_email = {
        'email': 'tori_s_42@te.st',
        'password': 'test'
    }
    upd_user = users.email(s, upd_email)

    assert upd_user.status_code == 400
    assert upd_user.json()['status'] == 'error'
    assert upd_user.json()['message'] == "Wrong password"


"""CARS CREATE"""


def test_cars_post_01(user, car_data):
    """Positive test that user can create new car correctly"""
    new_car = cars.cars_post(s, car_data)
    assert new_car.status_code == 201
    assert new_car.json()['status'] == 'ok'
    assert new_car.json().get('data', {}).get('id', int)
    assert new_car.json().get('data', {}).get('carBrandId', int) == car_data['carBrandId']
    assert new_car.json().get('data', {}).get('carModelId', int) == car_data['carModelId']
    assert new_car.json().get('data', {}).get('mileage', int) == car_data['mileage']
    assert new_car.json().get('data', {}).get('brand', 'Porsche')
    assert new_car.json().get('data', {}).get('model', 911)


def test_cars_post_02(user, car_data):
    """Negative test that user couldn't create new car with incorrect data"""
    car_data['carModelId'] = 20
    new_car = cars.cars_post(s, car_data)

    assert new_car.status_code == 404
    assert new_car.json()['status'] == 'error'
    assert new_car.json()['message'] == "Model not found"


def test_cars_post_03(user, car_data):
    """Negative test that user couldn't create new car without correct session"""
    new_car = cars.cars_post(new_s, car_data)  # incorrect session

    assert new_car.status_code == 401
    assert new_car.json()['status'] == 'error'
    assert new_car.json()['message'] == "Not authenticated"


"""CARS UPDATE"""


def test_cars_id_put_01(user, car, car_data):
    """Test that user can edit existing car with correct data and can't do it with incorrect ones"""
    car_data['id'] = car['data']['id']
    car_data['mileage'] = 265
    edited_car = cars.cars_id_put(s, car_data)

    assert edited_car.status_code == 200
    assert edited_car.json()['status'] == 'ok'
    assert edited_car.json().get('data', {}).get('mileage', int) == car_data['mileage']


def test_cars_id_put_02(user, car, car_data):
    """Negative test that user couldn't update car mileage if it less than previous one"""
    car_data.update({'id': car['data']['id'], 'mileage': 199})
    edited_car = cars.cars_id_put(s, car_data)

    assert edited_car.status_code == 400
    assert edited_car.json()['status'] == 'error'
    assert edited_car.json()['message'] == "New mileage is less then previous entry"


def test_cars_id_put_03(user, car_data):
    """Negative test that user couldn't update car without correct session"""
    edited_car = cars.cars_id_put(new_s, car_data)  # incorrect session

    assert edited_car.status_code == 401
    assert edited_car.json()['status'] == 'error'
    assert edited_car.json()['message'] == 'Not authenticated'


def test_cars_id_put_04(user, car, car_data):
    """Negative test that user couldn't update car with incorrect id"""
    car_data.update({'id': 856523654789636, 'mileage': 199})
    edited_car = cars.cars_id_put(s, car_data)

    assert edited_car.status_code == 404
    assert edited_car.json()['status'] == 'error'
    assert edited_car.json()['message'] == 'Car not found'


"""GET CARS BRAND BY ID"""


def test_cars_brand_id_01(car_data):
    """Positive test that car id is correct"""
    cars.cars_post(s, car_data)
    data = {'id': car_data['carBrandId']}
    car_id = cars.brands_id(s, data)

    assert car_id.status_code == 200
    assert car_id.json()['status'] == 'ok'
    assert car_id.json().get('data', {}).get('id', int) == car_data['carBrandId']
    assert car_id.json().get('data', {}).get('title', 'Porsche')


def test_cars_brand_id_02():
    """Negative test response if id incorrect"""
    data = {'id': 0}
    car_id = cars.brands_id(s, data)

    assert car_id.status_code == 404
    assert car_id.json()['status'] == 'error'
    assert car_id.json()['message'] == "No car brands found with this id"


"""EXPENSES CREATE"""


def test_expenses_post_01(user, car, expenses_data):
    """Positive test to create new expense"""
    expense = expenses.expenses_post(s, expenses_data)

    assert expense.status_code == 200
    assert expense.json()['status'] == 'ok'
    assert expense.json().get('data', {}).get('id', int)
    assert expense.json()['data']['carId'] == car['data']['id']
    assert expense.json()['data']['reportedAt'] == expenses_data['reportedAt']
    assert expense.json()['data']['liters'] == expenses_data['liters']
    assert expense.json()['data']['totalCost'] == expenses_data['totalCost']


def test_expenses_post_02(user):
    """Negative test that car id is required for creating expense"""
    expense = expenses.expenses_post(s, {})

    assert expense.status_code == 400
    assert expense.json()['status'] == 'error'
    assert expense.json()['message'] == "Car id is required"


def test_expenses_post_03(user):
    """Negative test that user couldn't create expense without correct session"""
    expense = expenses.expenses_post(new_s, {})  # incorrect session

    assert expense.status_code == 401
    assert expense.json()['status'] == 'error'
    assert expense.json()['message'] == "Not authenticated"


def test_expenses_post_04(user, car, expenses_data):
    """Negative test if car id is invalid"""
    expenses_data.update({'carId': 0})
    expense = expenses.expenses_post(s, expenses_data)

    assert expense.status_code == 404
    assert expense.json()['status'] == 'error'
    assert expense.json()['message'] == "Car not found"


"""GET EXPENSES BY ID"""


def test_expenses_get_01(user, car, expenses_data):
    """Positive test to get expense by id"""
    expense = expenses.expenses_post(s, expenses_data)
    expense_id = {'id': expense.json()['data']['id']}
    expense_get = expenses.expenses_id_get(s, expense_id)

    assert expense_get.status_code == 200
    assert expense_get.json()['status'] == 'ok'
    assert expense_get.json()['data']['id'] == expense.json()['data']['id']
    assert expense_get.json()['data']['carId'] == car['data']['id']
    assert expense_get.json()['data']['reportedAt'] == expenses_data['reportedAt']
    assert expense_get.json()['data']['mileage'] == expenses_data['mileage']
    assert expense_get.json()['data']['liters'] == expenses_data['liters']
    assert expense_get.json()['data']['totalCost'] == expenses_data['totalCost']


def test_expenses_get_02(user, car):
    """Negative test to get expense by id"""
    expense_get = expenses.expenses_id_get(s, {'id': 0})

    assert expense_get.status_code == 404
    assert expense_get.json()['status'] == 'error'
    assert expense_get.json()['message'] == "Expense not found"


def test_expenses_get_03(user):
    """Negative test to get expense without correct session"""
    expense_get = expenses.expenses_id_get(new_s, {})  # incorrect session

    assert expense_get.status_code == 401
    assert expense_get.json()['status'] == 'error'
    assert expense_get.json()['message'] == "Not authenticated"
