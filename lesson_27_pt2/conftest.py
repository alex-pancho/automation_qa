import pytest
from .get_browser import chrome
from .pages.home_page import HomePage
from .pages.cabinet_page import CabinetPage
from .pages.catalog_page import CatalogPage

URL = "https://harwind.com.ua/"

@pytest.fixture(scope="function")
def driver():
    _driver = chrome(True)
    _driver.maximize_window()
    _driver.get(URL)
    yield _driver
    _driver.quit()


@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def cabinet_page(driver):
    return CabinetPage(driver)

@pytest.fixture
def catalog_page(driver):
    return CatalogPage(driver)

@pytest.fixture
def catalog_page(driver):
    catalog_page = CatalogPage(driver)
    catalog_page.go_to_catalog_page()
    return catalog_page
