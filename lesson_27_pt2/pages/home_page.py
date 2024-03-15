import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from automation_qa.lesson_27_pt2.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        login_button = "//li[@class='item modal__open open__login-modal']",
        register_button = "//a[@class='item modal__open']",
        user_name_field = "//input[@type='email']",
        password_field = "//input[@type='password']",
        login_submit_button = "//button[contains(text(), 'Увійти')]",
        toast_error = "//div[@class='toast toast-error']",
        search_box = "//*[@id='app']/header[2]/div[2]/div/div/div[2]/form/div/div/input",
        search_button = "//*[@id='app']/header[2]/div[2]/div/div/div[2]/form/div/div/button[2]/img"
        )

    def login(self, username, password):
        login_button = self.item("login_button")
        login_button.click()
        user_name_field = self.item("user_name_field")
        user_name_field.send_keys(username)
        password_field = self.item("password_field")
        password_field.send_keys(password)
        login_submit_button = self.item("login_submit_button")
        login_submit_button.click()

    def get_toast_error_element(self):
        toast_error_element = self.item("toast_error")
        return toast_error_element

    def search(self, text):
        search_box = self.item("search_box")
        search_box.send_keys(text)
        search_button = self.item("search_button")
        search_button.click()
