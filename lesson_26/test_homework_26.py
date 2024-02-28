import sys
import pathlib
import pytest
root = str(pathlib.Path(__file__).parent)
sys.path.insert(0, root)
from lesson_26 import *


@pytest.fixture
def np_driver():
    driver_np = get_url("https://tracking.novaposhta.ua/#/uk/")
    yield driver_np
    driver_np.quit()


@pytest.fixture
def search(np_driver):
    search_field_xpath = '//div[@class=\'track__form-group-input-wrap\']//input[1]'
    search_field = find_by_xpath(np_driver, search_field_xpath)
    return search_field


search_button_xpath = '//input[@id="np-number-input-desktop-btn-search-en"]'
close_button_xpath = '(//span[@class="v-btn__content"])[6]'
status_text_xpath = '//div[@class=\'header__status-header\']/following-sibling::div[1]'


def test_valid_search_np_01(np_driver, search):
    """Validation test for button search component.
    Expect disabled button if user enter less than 10 symbols"""
    input_to(search, "000000000")  # 9 symbols
    search_button = find_by_xpath(np_driver, search_button_xpath)

    assert search_button.get_attribute("disabled") is not None, \
        f"Element {search} hasn't attribute 'disabled'"


def test_valid_search_np_02(np_driver, search):
    """Validation test for button search component.
    Expect disabled button if user enter special symbols or cyrillic letters"""
    input_to(search, 'тест%тест@$#')
    search_button = find_by_xpath(np_driver, search_button_xpath)

    assert search_button.get_attribute("disabled") is not None, f"Element {search} hasn't attribute 'disabled'"
    assert 'тест%тест@$#' not in search.text, f"Element was found in field '{search}'"


def test_get_correct_status_np(np_driver, search):
    """Test to getting correct status ('Отримана') of package with valid tracking number"""
    input_to(search, '20400371989832')
    wait_and_click(np_driver, close_button_xpath)
    elem_text = get_text(np_driver, status_text_xpath)

    assert "Отримана" in elem_text, f"Expected 'Отримана', but got {elem_text}"
