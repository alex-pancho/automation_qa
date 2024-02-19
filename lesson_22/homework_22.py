### Task 1
# Improved users.resetpassword method

### Task2

from hillel_api import *

DEF_EMAIL = "viki@mydemouser2.com"


# 1. User sign up
def test_user_signup():
    user_data = {
        "name": "Viki",
        "lastName": "Lopa",
        "email": DEF_EMAIL,
        "password": "Qwerty12345",
        "repeatPassword": "Qwerty12345"
    }
    response = auth.signup(s, user_data)
    json = response.json()
    # If user already exists, it gives 400
    assert response.status_code == 201
    assert "status" in json
    assert json["status"] == "ok"


# User authentication
def test_user_signin():
    user_data = {
        "email": DEF_EMAIL,
        "password": "Qwerty12345",
        "remember": True
    }
    response = auth.signin(s, user_data)
    json = response.json()
    assert response.status_code == 200
    assert "status" in json
    assert json["status"] == "ok"


# 2. Create a car
def test_create_car():
    data = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 180
    }
    response = cars.cars_post(s, data)
    json = response.json()
    assert response.status_code == 201
    assert "carBrandId" in json['data']
    cars.last_created_car_id = json['data']['id']


# 3. Edit a car
def test_edit_car():
    data = {
        "id": cars.last_created_car_id,
        "carBrandId": 1,
        "carModelId": 2
    }
    response = cars.cars_id_put(s, data)
    json = response.json()
    assert response.status_code == 200
    assert json["data"]["carModelId"] == 2


# 4. GET data of cars
def test_get_cars():
    response = cars.cars_get(s)
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json["data"], list)


# 5. DELETE current user in session
def test_user_delete():
    response = users.users(s)
    assert response.status_code == 200
