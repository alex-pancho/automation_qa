from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "https://www.geeksforgeeks.org/action-chains-in-selenium-python/"
driver = webdriver.Firefox()
driver.get(url)
# https://www.selenium.dev/documentation/webdriver/actions_api/
action = ActionChains(driver)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav # submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

# FullentWait
wait = WebDriverWait(driver,
                        timeout=10,
                        poll_frequency=1,
                        ignored_exceptions=[ElementNotVisibleException,
                                            ElementNotSelectableException]
                        )
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div")))
