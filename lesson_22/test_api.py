import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from ideas_for_test.hillel_test_api.hillel_api import s, auth, users


# def test_signup():
#     user_data = {
#         "name": "John",
#         "lastName": "Dou",
#         "email": "test050224@test.com",
#         "password": "Qwerty12345",
#         "repeatPassword": "Qwerty12345"
#         }
#     r = auth.signup(s, user_data)
#     r_json = r.json()
#     assert r.status_code == 201, f"Wrong status code:\n{r_json}"
#     assert r_json.get('status', False) == "ok", "Key 'status' is not ok"

def test_sign_in():
    user_data = {
        "email": "qam2808@2022test.com",
        "password": "Qam2608venv",
        "remember": False
    }
    r = auth.signin(s, user_data)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"

def test_get_userdata():
    r = users.current(s)
    r_json = r.json()
    assert r.status_code == 200, f"Wrong status code:\n{r_json}"
    assert r_json.get('status', False) == "ok", "Key 'status' is not ok"
    assert r_json.get('data', {}).get('userId', 0) == 47413, r_json['data']['userId']
