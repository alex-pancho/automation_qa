from automation_qa.lesson_27_pt2.pages.base_page import BasePage


class CabinetPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        user_profile_button = "//button[@class='menu-button button button_text']",
        cart_button = "//button[@class='button button_icon search-button']",
        empty_cart_text = "//span[contains(text(), 'Кошик порожній')]",
        catalog_button = "//div[@class='header__search']/div[@class='catalog-menu']",
        add_to_cart_button = "(//button[contains(text(), 'В кошик')])[1]"
        )

    def get_user_profile_element(self):
        user_profile_button_element = self.item("user_profile_button")
        return user_profile_button_element

    def get_cart_button(self):
        cart_button = self.item("cart_button")
        return cart_button

    def get_catalog_button(self):
        catalog_button = self.item("catalog_button")
        return catalog_button

    def get_to_cart_button(self):
        add_to_cart_button = self.item("add_to_cart_button")
        return add_to_cart_button

