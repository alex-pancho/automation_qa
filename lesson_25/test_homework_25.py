from lesson_25 import *


def test_tracking_received_package():
    driver = get_url(np_url)
    search_field = find_by_xpath(driver, "//input[@id='en']")
    input_to(search_field, "20400378406543")
    search_result = find_by_xpath(driver, "//div[@class='header__status-text']").text
    assert "Отримана" in search_result
