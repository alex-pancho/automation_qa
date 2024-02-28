import sys
import pathlib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from lesson_25.lesson_25 import *

MULTI = 2


def find_by_path(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        element.is_displayed()
    except (NoSuchElementException, AttributeError, TimeoutException):
        element = None
    return element

# EXplicit is EXpected
# IMplicit is IMaginary

def test_explicit(driver):
    driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
    revealed = driver.find_element(By.ID, "revealed")
    driver.find_element(By.ID, "reveal").click()
    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d : revealed.is_displayed())


def expected_nf_field(driver):
    xpath = '//li[@id="ewuygeb"]'
    try:
        element = WebDriverWait(driver, timeout=5*MULTI).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        print(element)
    except TimeoutException:
        print("За даний час елемент не зявився на сторінці")
    finally:
        driver.quit()


def expected_field(driver):
    xpath = '//*[@name="q"]'
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )  # наявність поля
        element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )  # чи клікабельне
        screen_path = pathlib.Path(__file__).parent / "screenshot.png"
        driver.save_screenshot(f'{screen_path}')
    except TimeoutException:
        print("За даний час елемент не зявився на сторінці")
    finally:
        driver.quit()



if __name__ == "__main__":
    # обробка виключень в селеніум
    # driver = get_url(python_url)
    # driver.implicitly_wait(2)
    # search = find_by_path(driver, '//*[@name="q"]')
    # assert search is not None
    # очікування 1
    # driver = webdriver.Firefox()
    # test_explicit(driver)

    # очікування 2
    # expected_nf_field(driver)

    # очікування і скріншот
    driver = get_url(python_url)
    expected_field(driver)

