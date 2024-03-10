from dotenv import load_dotenv
import os

load_dotenv()
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
wrong_password = os.getenv("WRONG_PASSWORD")


def test_sign_in_with_valid_data(home_page, cabinet_page):
    home_page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    assert cabinet_page.get_user_profile_element().is_visible(), "User not loggined"

def test_error_after_login_with_wrong_password(home_page):
    home_page.login(os.getenv("LOGIN"), os.getenv("WRONG_PASSWORD"))
    assert home_page.get_toast_error_element().is_visible()

def test_open_empty_cart(home_page,cabinet_page):
    home_page.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    cabinet_page.get_cart_button().click()
    empty_cart_text_element = cabinet_page.item("empty_cart_text")
    assert empty_cart_text_element.is_visible(), "Текст 'Кошик порожній' не отображается"



