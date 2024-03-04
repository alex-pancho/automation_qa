from lesson_27_pt2.pages.base_page import BasePage


class SuperOffersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        first_buy_button_xpath="(//a[@class='tpl-unit-buy'])[1]",
    )
