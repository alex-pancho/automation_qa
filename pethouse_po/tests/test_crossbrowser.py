import pytest
from pethouse_po.conftest import MP, driver_factory


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_open_main_page(browser, driver_factory):
    """Fast smoke test for main page:
    open main page in different browsers and check few elements are visible and clickable"""
    assert "Зоомагазин Pethouse.ua" in driver_factory.title

    locators = ['home_page_button_xpath', 'profile_button_xpath', 'search_field_xpath',
                'basket_button_xpath', 'contacts_button_xpath']

    for xpath in locators:
        main_page = MP(driver_factory)

        element = main_page.item(xpath)
        assert element.is_visible(), f"Not found: {element._locator}"
        assert element.is_clickable(), f"Not clickable element: {element._locator}"


