"""
POSITIVE TEST FOR HOME PAGE https://pethouse.ua/ua/
"""
import time
from pethouse_po.conftest import URL, driver, main_page, offers_page


def test_homepage_button(driver, main_page):
    """Test that the main page button is visible and functionally"""
    element = main_page.item('home_page_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"
    element.click()
    assert URL == driver.current_url, \
        f"It seems homepage button has incorrect link! Current url: {driver.current_url}"


def test_profile_button(main_page):
    """Test that the profile button is visible and functionally"""
    element = main_page.item('profile_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"

    element.click()
    login_form = main_page.item('login_form_xpath')
    assert login_form.is_presented(), f"Don't presented: {login_form._locator}"


def test_search_field(driver, main_page):
    """Test that the search field is visible, functionally and results of search are correct"""
    element = main_page.item('search_field_xpath')
    search_key = "0000000"
    assert element.is_visible(), f"Not found: {element._locator}"

    element.click()
    element.send_keys_and_enter(search_key)
    assert f'{URL}search-results/?search_value={search_key}' == driver.current_url, \
        f"It seems link of search result isn't correct! Current url: {driver.current_url}"

    expected_result = ': знайдено 0 результатів'
    search_result = main_page.item('not_found_xpath')
    assert expected_result in search_result.get_text()
    assert search_key in search_result.get_text()


def test_basket_button(driver, main_page):
    """Test that the basket button is visible and functionally"""
    element = main_page.item('basket_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"

    element.click()
    assert f'{URL}basket/' == driver.current_url


def test_basket_count(main_page, offers_page):
    """
    Test that count of item in basket changeable
    Step 1: get homepage and get count of items (0)
    Step 2: add to card any one item
    Step 3: compare 1 with current count in basket
    """
    # Step 1
    element = main_page.item('count_in_basket_xpath')
    count_before = element.get_text()
    assert count_before == '0'

    # Step 2
    all_promotions_element = main_page.item('all_promotions_button_xpath')
    all_promotions_element.click()
    buy_element = offers_page.item('first_buy_button_xpath')
    buy_element.click()
    time.sleep(5)

    # Step 3
    count_after = element.get_text()
    assert count_after == '1'


def test_payment_delivery_button(driver, main_page):
    """Test that button 'Payment&Delivery' is visible and functionally"""
    element = main_page.item('payment_delivery_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"

    element.click()
    assert f'{URL}about/oplata-i-dostavka/' == driver.current_url


def test_promotions_button(driver, main_page):
    """Test that button 'Payment&Delivery' is visible and functionally"""
    element = main_page.item('all_promotions_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"

    element.click()
    assert f'{URL}superoffers/' == driver.current_url


def test_appstore_app_button(main_page):
    """Test that button 'Payment&Delivery' is visible and functionally"""
    element = main_page.item('appstore_app_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"

    appstore_a = main_page.item('appstore_a')
    first_link = appstore_a.get_attribute("href")
    assert "apps.apple.com" and "pethouse" in first_link, \
        f"Not found expected values. Result link: {first_link}"


def test_contacts_button(main_page):
    """Test that contacts button is visible and functionally"""
    element = main_page.item('contacts_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"

    element.click()
    contact_form = main_page.item('contacts_form_xpath')
    assert contact_form.is_presented(), f"Don't presented: {contact_form._locator}"


def test_menu_cats_button(main_page):
    """Test that menu button is visible and functionally"""
    element = main_page.item('menu_cats_button_xpath')
    assert element.is_visible(), f"Not found: {element._locator}"

    element.move_to_element()
    menu_block = main_page.item('menu_cats_block_xpath')
    assert menu_block.is_presented(), f"Don't presented: {menu_block._locator}"


def test_menu_cats_dry_food_button(driver, main_page):
    """Test that button with Dry food in cats section is visible and functionally"""
    element_cats = main_page.item('menu_cats_button_xpath')
    element_dry_food = main_page.item('menu_cats_dry_food_button_xpath')

    element_cats.move_to_element()
    element_dry_food.click()

    assert f"{URL}shop/koshkam/suhoi-korm/" == driver.current_url
