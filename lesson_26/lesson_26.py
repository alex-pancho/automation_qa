import sys
import pathlib
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lesson_25.lesson_25 import *


def main():
    return get_url("http://localhost")


def selector(driver):
    xpath = '//select[@name="selectomatic"]'
    element = find_by_xpath(driver, xpath)
    select = Select(element)
    return select


def wait_and_click(driver, xpath):
    """Wait few seconds before click. Wait until find element by Xpath"""
    element = WebDriverWait(driver, 3.5).until(lambda x: x.find_element(By.XPATH, xpath))
    element.click()


def get_text(driver, xpath):
    """Get text from found element (by Xpath)"""
    element = find_by_xpath(driver, xpath)
    return element.text


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
