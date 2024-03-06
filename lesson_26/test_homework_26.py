import sys
import pathlib
import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lesson_25.lesson_25 import *
from lesson_26.lesson_26 import *

xpath_status_text = '//*[@id="chat"]/header/div[2]/div[2]/div[2]'
xpath_field = '//*[@id="en"]'
TR_ID = "59001082084790"

def test_status_by_TR_ID():
    driver = main()
    input_field = expected_element(driver, xpath_field)
    input_to(input_field, TR_ID)
    status_result = expected_element(driver, xpath_status_text)
    assert status_result.text == "Отримано"

