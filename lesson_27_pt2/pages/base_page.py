from .elements import WebElement

class BasePage:
    locators = {}

    def __init__(self, driver):
        self.driver = driver


    def item(self, name:str):
        _xpath = self.locators.get(name)
        if _xpath is None:
            raise AttributeError(
                f"{self.__class__.__name__} has no xpath for element: {name}, " \
                f"may be typo? Exsist names is: {self.locators.keys()}"
                )
        return WebElement(driver=self.driver, xpath=_xpath)