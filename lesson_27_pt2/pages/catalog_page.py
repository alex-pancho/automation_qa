from automation_qa.lesson_27_pt2.pages.base_page import BasePage


class CatalogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        product_title = "//span[@class='title h5']",
        toast_error = "//div[@class='toast toast-error']",
        catagories_block = "//ul[@class='categories__list']"
    )

    def get_category_names(self):
        category_elements = self.item("catagories_block").get_text()
        return category_elements

    def get_text_in_product_title(self):
        title_text = self.item("product_title").get_text()
        return title_text

    def get_toast_error_element(self):
        toast_error_element = self.item("toast_error")
        return toast_error_element

    def go_to_catalog_page(self):
        self.driver.get("https://harwind.com.ua/catalog")







