from automation_qa.ideas_for_test.hillel_test_api.hillel_api import *



def test_signup():
    """Test successful signup and check data"""

    request_body = {
        "name": "Nixongftk",
        "lastName": "Silverhand",
        "email": "johnd3222@ts.ts",
        "password": "Aa123456",
        "repeatPassword": "Aa123456"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 201, f"Assertion failed: {r_json}"
    assert r_json["data"]["userId"] is not None, f"Assertion failed. User id is: {r_json["data"]["userId"]}"
    assert r_json["data"]["distanceUnits"] == "km", f"Assertion failed:{r_json["data"]["distanceUnits"]} "
    assert r_json["data"]["currency"] == "usd", f"Assertion failed. Currency is: {r_json["data"]["currency"]}"


def test_signup_different_password():
    """Test unsuccessful signup
        with different password"""

    request_body = {
        "name": "Nixongftk",
        "lastName": "Silverhand",
        "email": "johnd3222@ts.ts",
        "password": "Aa123456",
        "repeatPassword": "aa123456"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, f"Assertion failed: {r_json}"
    assert r_json["status"] == "error", f"Assertion failed. Status is: {r_json["status"]}"
    assert r_json["message"] == "Passwords do not match", f"Assertion failed. Message is: {r_json["message"]}"


def test_create_car():
    """Test successful create new car
        and check the data"""
    user_data = {
        "email": "johnd3222@ts.ts",
        "password": "Aa123456",
        "remember": False
    }
    auth.signin(s, user_data)

    request_body = {
        "carBrandId": 4,
        "carModelId": 16,
        "mileage": 442
    }
    r = cars.cars_post(s, request_body)
    r_json = r.json()
    assert r.status_code == 201, f"Assertion failed: {r_json}"
    assert r_json["data"]["id"] is not None, f"Assertion failed: {r_json["data"]["id"]}"
    assert r_json["data"]["carBrandId"] == 4, f"Assertion failed: {r_json["data"]["carBrandId"]}"
    assert r_json["data"]["carModelId"] == 16, f"Assertion failed: {r_json["data"]["carModelId"]}"
    assert r_json["data"]["initialMileage"] == 442, f"Assertion failed: {r_json["data"]["initialMileage"]}"


def test_create_car_no_auth():
    """Create car without auth"""

    request_body = {
        "carBrandId": 4,
        "carModelId": 16,
        "mileage": 442
    }
    r = cars.cars_post(s, request_body)
    r_json = r.json()
    assert r.status_code == 401, f"Assertion failed: {r_json}"
    assert r_json["message"] == "Not authenticated", f"Assertion failed: {r_json["message"]}"


def test_edite_car_positive():
    """Check valid edits car"""

    user_data = {
        "email": "johnd3222@ts.ts",
        "password": "Aa123456",
        "remember": False
    }
    auth.signin(s, user_data)

    request_body = {
        "id": 112775,
        "carBrandId": 4,
        "carModelId": 16,
        "mileage": 442
    }

    r = cars.cars_id_put(s, request_body)
    r_json = r.json()
    assert r.status_code == 200, f"Assertion failed: {r_json}"
    assert r_json["data"]["id"] == request_body["id"], f"Assertion failed: {r_json['data']['id']}"
    assert r_json["data"]["carBrandId"] == request_body["carBrandId"], f"Assertion failed: {r_json['data']['carBrandId']}"
    assert r_json["data"]["carModelId"] == request_body["carModelId"], f"Assertion failed: {r_json['data']['carModelId']}"
    assert r_json["data"]["mileage"] == request_body["mileage"], f"Assertion failed: {r_json['data']['mileage']}"


def test_current_user_cars():
    user_data = {
        "email": "johnd3222@ts.ts",
        "password": "Aa123456",
        "remember": False
    }
    auth.signin(s, user_data)

    r = cars.cars_get(s)
    r_json = r.json()
    assert r.status_code == 200, f"Assertion failed: {r_json}"
    assert "data" in r_json, "Assertion failed: 'data' is missing in the response"
    assert isinstance(r_json["data"], list), "Assertion failed: 'data' should be a list"

    expected_keys = ["id", "carBrandId", "carModelId", "mileage",
                     "brand", "model", "logo"]
    for record in r_json["data"]:
        assert all(key in record for key in expected_keys), "Assertion failed: Unexpected keys in 'data' record"


def test_user_delete():
    user_data = {
        "email": "johnd3222@ts.ts",
        "password": "Aa123456",
        "remember": False
    }
    auth.signin(s, user_data)

    r = users.users(s)
    r_json = r.json()
    assert r.status_code == 200, f"Assertion failed: {r_json}"
    assert r_json["status"] == "ok", f"Assertion failed: {r_json}"

def test_user_delete_no_auth():
    r = users.users(s)
    r_json = r.json()
    assert r.status_code == 401, f"Assertion failed: {r_json}"
    assert r_json["status"] == "error", f"Assertion failed: {r_json["status"]}"
    assert r_json["message"] == "Not authenticated", f"Assertion failed: {r_json["message"]}"