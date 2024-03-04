import pytest
from lesson_27_pt2.get_browser import firefox, chrome
from .pages.main_page import MainPage as MP
from .pages.superoffers_page import SuperOffersPage as SoP

URL = "https://pethouse.ua/ua/"


@pytest.fixture(scope="function")
def driver():
    _driver = chrome()
    _driver.get(URL)
    yield _driver
    _driver.quit()


@pytest.fixture()
def main_page(driver):
    return MP(driver)


@pytest.fixture()
def offers_page(driver):
    return SoP(driver)
