from dotenv import load_dotenv
import os
import pytest
load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
wrong_password = os.getenv("WRONG_PASSWORD")

@pytest.mark.parametrize("login, password", [
    (os.getenv("LOGIN"), os.getenv("PASSWORD")),
    (os.getenv("LOGIN"), os.getenv("WRONG_PASSWORD")),
    ("wrong_mail@com.wrong", "password123")
])
def test_sign_in(home_page, cabinet_page, login, password):
    home_page.login(login, password)
    if password == os.getenv("PASSWORD"):
        assert cabinet_page.get_user_profile_element().is_visible(), "User not logged in"
    else:
        assert home_page.get_toast_error_element().is_visible(), "Error toast not visible"

def test_open_empty_cart(home_page,cabinet_page):
    home_page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    cabinet_page.get_cart_button().click()
    empty_cart_text_element = cabinet_page.item("empty_cart_text")
    assert empty_cart_text_element.is_visible(), "Текст 'Кошик порожній' не отображается"

@pytest.mark.parametrize("search_query, expected_text, valid", [
    ("Система обігріву пацієнта Warm 6200", "Система обігріву пацієнта Warm 6200", True),
    ("Невалидный запрос", "Ошибка: продукт не найден", False)
])
def test_search(home_page, catalog_page, search_query, expected_text, valid):
    home_page.search(search_query)
    if valid:
        factual_text = catalog_page.get_text_in_product_title()
        assert expected_text == factual_text
    else:
        error_message = catalog_page.get_toast_error_element()
        assert expected_text == error_message

@pytest.mark.parametrize("expected_categories", [
    ([  "Акушерське обладнання",
        "Ендоскопічне обладнання",
        "Ультразвукова діагностика",
        "Кардіологічне обладнання",
        "Операційне обладнання",
        "Рентгенологічне обладнання",
        "Неонатологічне обладнання",
]),
    ])
def test_catalog_open_with_expected_categories(catalog_page, expected_categories):
    category_names = catalog_page.get_category_names()
    missing_categories = [name for name in expected_categories if name not in category_names]
    assert not missing_categories, f"Expected categories not found: {missing_categories}. Founded categories: {category_names}"


