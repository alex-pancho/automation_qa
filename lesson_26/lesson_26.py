import sys
import pathlib
from selenium.webdriver.support.select import Select



sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lesson_25.lesson_25 import *

novapost_url = f"https://tracking.novaposhta.ua/#/uk/"
cmr_input_id = "en"
search_button_id = "np-number-input-desktop-btn-search-en"
cmr_status_xpath = "//*[@class='header__status-text']"
parcel_number = "20400373461432"


def main():
    return get_url("http://localhost")


def selector(driver):
    xpath = '//select[@name="selectomatic"]'
    element = find_by_xpath(driver, xpath)
    select = Select(element)
    return select






if __name__ == "__main__":
    driver = main()
    select = selector(driver)
    two_element = find_by_xpath(driver, '//option[@value="two"]')
    four_element = find_by_xpath(driver, '//option[@value="four"]')
    count_element = find_by_xpath(driver, '//option[@value="still learning how to count, apparently"]')
    select.select_by_visible_text('Four')
    assert four_element.is_selected()
    select.select_by_value('two')
    assert two_element.is_selected()
    select.select_by_index(3)
    assert count_element.is_selected()
