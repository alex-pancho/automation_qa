from pathlib import Path
from selenium import webdriver

from selenium.webdriver.common.by import By


def file_uploader(folder: Path, filename: str = 'some-file.txt'):
    driver = webdriver.Firefox()
    file = str(folder / filename)
    driver.get('http://the-internet.herokuapp.com/upload')
    upload_button = driver.find_element(By.ID, 'file-upload')
    upload_button.send_keys(file)
    driver.find_element(By.ID,'file-submit').click()
    uploaded_file = driver.find_element(By.ID, 'uploaded-files').text
    assert uploaded_file == filename, f"uploaded file should be {filename}"


folder = Path("C:\\Users\\Alex\\Downloads")
filename = "image (1).png"
file_uploader(folder, filename)
