from lesson_27_pt2.pages.base_page import BasePage
from lesson_27_pt2.pages.elements import WebElement
from pethouse_po.conftest import *


class ShopCatsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict()

    def get_section_title(self, index):
        """Get index and create xpath by it, return WebElement"""
        _xpath = f"(//div[@class='ph-new-upcategory-block']//span)[{index}]"
        return WebElement(driver=self.driver, xpath=_xpath)

    def get_subsection_href(self, index):
        """Get index and create xpath by it, return WebElement"""
        _xpath = f"(//div[@class='ph-new-category-block']//a)[{index}]"
        return WebElement(driver=self.driver, xpath=_xpath)
