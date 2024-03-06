import sys
import pathlib
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lesson_25.lesson_25 import *


# def main():
#     return get_url("http://localhost")


# def selector(driver):
#     xpath = '//select[@name="selectomatic"]'
#     element = find_by_xpath(driver, xpath)
#     select = Select(element)
#     return select


# if __name__ == "__main__":
#     driver = main()
#     select = selector(driver)
#     two_element = find_by_xpath(driver, '//option[@value="two"]')
#     four_element = find_by_xpath(driver, '//option[@value="four"]')
#     count_element = find_by_xpath(driver, '//option[@value="still learning how to count, apparently"]')
#     select.select_by_visible_text('Four')
#     assert four_element.is_selected()
#     select.select_by_value('two')
#     assert two_element.is_selected()
#     select.select_by_index(3)
#     assert count_element.is_selected()
def main():
    return get_url("https://tracking.novaposhta.ua/#/uk/")

def expected_element (driver, xpath):
   # xpath = '//*[@id="en"]'
    try:
        element = WebDriverWait(driver, timeout=5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except(TimeoutException):
        element = None
    return element

