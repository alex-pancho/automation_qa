from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

timeout = 5


def get_url(url) -> ChromeWebDriver or FirefoxWebDriver:
    _driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    _driver.get(url)
    return _driver


def find_by_xpath(driver, xpath) -> WebElement:
    try:
        element = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(driver, timeout).until(element)
    except TimeoutException:
        raise Exception("Timeout waiting for page to load")
    return driver.find_element(By.XPATH, xpath)


def input_to(element: WebElement, text) -> None:
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)


def is_visible(element: WebElement) -> bool:
    return element.is_displayed()


def click(driver, element: WebElement, hold_seconds=0, x_offset=1, y_offset=1):
    action = ActionChains(driver)
    action.move_to_element_with_offset(element, x_offset, y_offset). \
        pause(hold_seconds).click(on_element=element).perform()
