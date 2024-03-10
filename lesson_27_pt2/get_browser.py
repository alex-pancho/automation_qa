from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver



def chrome(debug=False):
    options = ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome() if debug else \
        webdriver.Chrome(options)
    return driver


if __name__ == "__main__":
    import pathlib
    # driver = firefox()
    # driver = chrome()
    # driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")
    # screen_path = pathlib.Path(__file__).parent / "screenshot.png"
    # driver.save_screenshot(f'{screen_path}')
    # driver.close()
