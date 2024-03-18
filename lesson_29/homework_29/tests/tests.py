def test_invalid_login(home_page):
    error_text = home_page.login_invalid_user("invalid", "user")
    assert error_text.endswith("Username and password do not match any user in this service")


def test_valid_login(home_page):
    home_page.login_user("standard_user", "secret_sauce")
    product_item = home_page.item("products")
    assert product_item.get_text() == "Products"


def test_purchase_product(home_page):
    home_page.purchase_product("John", "Doe", "11111")
    thank_page_msg = home_page.item("thank_page_msg")
    assert thank_page_msg.get_text() == "Thank you for your order!"
    back_home_button = home_page.item("back_home_button")
    back_home_button.click()

