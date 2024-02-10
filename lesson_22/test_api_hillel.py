import pytest
from automation_qa.ideas_for_test.hillel_test_api.hillel_api import *


def test_user_registration():

    user_reg_data = {
        "name": "Vasyl",
        "lastName": "Vasyl`ev",
        "email": "user0001@tst.tst",
        "password": "123456a",
        "repeatPassword": "123456a"
        }
    r = auth.signup(s, user_reg_data)
    r_json = r.json()