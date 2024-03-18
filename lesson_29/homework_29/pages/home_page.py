from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        username_input='//input[@id="user-name"]',
        password_input='//input[@id="password"]',
        login_button='//input[@id="login-button"]',
        error_msg='//div[@class="error-message-container error"]//h3[@data-test="error"]',
        products='//div[@id="header_container"]//span[@class="title"]',
        product_backpack_button='//button[@id="add-to-cart-sauce-labs-backpack"]',
        shop_cart_page='//a[@class="shopping_cart_link"]',
        checkout_button='//button[@id="checkout"]',
        checkout_firstname_input='//input[@id="first-name"]',
        checkout_lastname_input='//input[@id="last-name"]',
        checkout_zip_input='//input[@id="postal-code"]',
        checkout_continue_button='//input[@id="continue"]',
        checkout_finish_button='//button[@id="finish"]',
        thank_page_msg='//div[@id="checkout_complete_container"]//h2[@class="complete-header"]',
        back_home_button='//button[@id="back-to-products"]'
    )

    def login_user(self, username, password):
        username_by = self.item("username_input")
        password_by = self.item("password_input")
        signin_by = self.item("login_button")

        username_by.send_keys(username)
        password_by.send_keys(password)
        signin_by.click()

    def login_invalid_user(self, username, password):
        self.login_user(username, password)
        error_msg = self.item("error_msg")
        error_msg.wait_until_not_visible()
        return error_msg.get_text()

    def purchase_product(self, first_name, last_name, zipcode):
        # Add the backpack item to the cart
        product_backpack_button = self.item("product_backpack_button")
        product_backpack_button.click()

        # Go to the checkout page
        shop_cart_page = self.item("shop_cart_page")
        shop_cart_page.click()
        checkout_button = self.item("checkout_button")
        checkout_button.click()

        # Insert the customer information
        checkout_firstname_input = self.item("checkout_firstname_input")
        checkout_lastname_input = self.item("checkout_lastname_input")
        checkout_zip_input = self.item("checkout_zip_input")
        checkout_firstname_input.send_keys(first_name)
        checkout_lastname_input.send_keys(last_name)
        checkout_zip_input.send_keys(zipcode)
        checkout_continue_button = self.item("checkout_continue_button")
        checkout_continue_button.click()

        # Complete the order
        checkout_finish_button = self.item("checkout_finish_button")
        checkout_finish_button.click()
