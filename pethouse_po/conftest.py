import pytest
from lesson_27_pt2.get_browser import firefox, chrome
from .pages.main_page import MainPage as MP
from .pages.superoffers_page import SuperOffersPage as SoP
from .pages.shop_cats_page import ShopCatsPage as ScP
from .pages.src import *


"""DRIVERS"""


@pytest.fixture(scope="function")
def driver():
    _driver = chrome()
    _driver.get(URL)
    yield _driver
    _driver.quit()


@pytest.fixture(scope="function")
def driver_factory(request, browser):
    if browser == "chrome":
        _driver = chrome()
    elif browser == "firefox":
        _driver = firefox()
    else:
        raise ValueError("Invalid browser name")

    _driver.get(URL)
    yield _driver
    _driver.quit()


@pytest.fixture(scope="function")
def driver_shop_cats():
    _driver = chrome()
    _driver.get(URL_SHOP_CATS)
    yield _driver
    _driver.quit()


"""PAGES"""


@pytest.fixture()
def main_page(driver):
    return MP(driver)


@pytest.fixture()
def offers_page(driver):
    return SoP(driver)


@pytest.fixture()
def shop_cats_page(driver_shop_cats):
    return ScP(driver_shop_cats)
