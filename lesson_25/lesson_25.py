import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from dotenv import load_dotenv
# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)


np_url = "https://tracking.novaposhta.ua"

# user = os.environ.get("UNAME")
# password = os.environ.get("HLLPASS")
# hilell_url = f"https://{user}:{password}@qauto.forstudy.space"

def get_url(url):
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    driver.get(url)
    return driver


def find_by_id(driver, _id):
    element = driver.find_element(By.ID, _id)
    return element

def find_by_xpath(driver, xpath, timeout=3):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))

def find_by_name(driver, name):
    element = driver.find_element(By.NAME, name)
    return element

def input_to(element, text):
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)



if __name__ == "__main__":

    driver = get_url(python_url)
    about = find_by_id(driver, "about")
    about.click()
    search = find_by_name(driver, "q")
    input_to(search, "python")
    # search.text
    # driver.close()