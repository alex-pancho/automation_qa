import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))

from automation_qa.ideas_for_test.hillel_test_api.hillel_api import *


class TestApiHillel:
    def test_signup_with_valid_data(self):
        """Test for user sign up with valid data"""
        request_body = {
            "name": "Tester",
            "lastName": "Testovich",
            "email": "testovich@test.com",
            "password": "Qwe12345@",
            "repeatPassword": "Qwe12345@"
        }
        r = auth.signup(s, request_body)
        r_json = r.json()
        assert r.status_code == 201, f"Error: {r_json.get('message')}"

        users.delete_user(s, r_json)


    def test_signup_empty_email_field(self):
        """Test for user sign up with empty email"""

        request_body = {
            "name": "Tester",
            "lastName": "Testovich",
            "email": " ",
            "password": "Qwe12345",
            "repeatPassword": "Qwe12345"
            }
        r = auth.signup(s, request_body)
        r_json = r.json()
        assert r.status_code == 400, "Status code is not 400"
        assert r_json["message"] == "\"email\" is not allowed to be empty"


    def test_signup_to_long_name(self):
        """Test for user sign up with email more than 20 characters"""
        request_body = {
            "name": "Testerwithloooooongnaaaame",
            "lastName": "Testovich",
            "email": " ",
            "password": "QWE12345",
            "repeatPassword": "QWW12345"
        }
        r = auth.signup(s, request_body)
        r_json = r.json()
        assert r.status_code == 400, "Status code is not 400"
        assert r_json["message"] ==  "Name has to be from 2 to 20 characters long"


    def test_create_a_car_with_valid_data(self):
        """Test for car creating with valid data"""
        #create a user before car creating
        request_body = {
            "name": "Tester",
            "lastName": "Testovich",
            "email": "testovich@test.com",
            "password": "Qwe12345",
            "repeatPassword": "Qwe12345"
        }
        r = auth.signup(s, request_body)
        assert r.status_code == 201, "Status code is not 201"

        request_body = {
            "carBrandId": 1,
            "carModelId": 1,
            "mileage": 999999
        }
        r = cars.cars_post(s, request_body)
        r_json = r.json()
        assert r.status_code == 201, "Status code is not 201"

        users.delete_user(s, r_json)
        cars.cars_id_delete(s, r_json['data'])


    def test_error_when_not_authorized_user_creates_a_car(self):
        """Test for car creating when user not authorized"""
        request_body = {
            "carBrandId": 1,
            "carModelId": 1,
            "mileage": 999999
            }
        r = cars.cars_post(s, request_body)
        r_json = r.json()
        assert r.status_code == 401, "Status code is not 401"
        assert r_json["message"] == "Not authenticated"

    def test_update_existing_car_with_valid_data(self):
        """Test updating car data"""
        # create a user before car creating
        request_body = {
            "name": "Tester",
            "lastName": "Testovich",
            "email": "testovich@test.com",
            "password": "Qwe12345",
            "repeatPassword": "Qwe12345"
             }
        r = auth.signup(s, request_body)
        assert r.status_code == 201, "User is not created"

        # create a car before updating
        request_body = {
            "carBrandId": 1,
            "carModelId": 1,
            "mileage": 999999
            }
        r = cars.cars_post(s, request_body)
        r_json = r.json()
        assert r.status_code == 201, "Cat is not creating"

        #car_updating
        update_car_data = {
            "id": r_json["data"]["id"],
            "carBrandId": 2,
            "carModelId": 2,
            "mileage": 100000
            }
        update_car = cars.cars_id_put(s, update_car_data)
        update_car_json = update_car.json()
        assert update_car.status_code == 200, "Status code is not 200"
        assert update_car_json["data"]["carModelId"] == 2, "Car model ID is not changed"
        assert update_car_json["data"]["carBrandId"] == 2, "Car Brand ID is not changed"
        assert update_car_json["data"]["mileage"] == 100000, "Car mileage is not changed"

        users.delete_user(s, r_json)
        cars.cars_id_delete(s, r_json['data'])

    def test_get_brands(self):
        """Test getting car brands"""
        expected_brands = [
            {"id": 1, "title": "Audi", "logoFilename": "audi.png"},
            {"id": 2, "title": "BMW", "logoFilename": "bmw.png"},
            {"id": 3, "title": "Ford", "logoFilename": "ford.png"},
            {"id": 4, "title": "Porsche", "logoFilename": "porsche.png"},
            {"id": 5, "title": "Fiat", "logoFilename": "fiat.png"}
             ]
        get_car_brands = cars.brands(s)
        response_json = get_car_brands.json()
        assert get_car_brands.status_code == 200, "Status code is not 200"
        received_brands = response_json["data"]
        for expected_brand in expected_brands:
            assert expected_brand in received_brands, f"Expected brand {expected_brand} not found in received brands"

    def test_delete_user(self):
        # create a user before delete
        request_body = {
            "name": "Tester",
            "lastName": "Testovich",
            "email": "testovich@test.com",
            "password": "Qwe12345",
            "repeatPassword": "Qwe12345"
        }
        r = auth.signup(s, request_body)
        assert r.status_code == 201, "User is not created"

        #delete user
        r = users.delete_user(s, request_body)
        r_json = r.json()
        assert r.status_code == 200, "Status code is not 200"
        assert r_json["status"] == "ok", "Status is not 'ok'"

        #login in to the deleted account
        request_body = {
            "email": "testovich@test.com",
            "password": "Qwe123456",
            "remember": False
        }
        r = auth.signin(s, request_body)
        r_json = r.json()
        assert r.status_code == 400, "Status code is not 400"
        assert r_json["status"] == "error", "Status is not 'error'"