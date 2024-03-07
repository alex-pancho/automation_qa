from homework_26 import *

tracking_number = "59001082084790"
positive_status = "Отримана"

def test_status_parcel_received():
    driver = get_url(base_url)
    with driver:
        input_box = find_by_xpath(driver, '//input[@id="en"]')
        if is_visible(input_box):
            input_to(input_box, tracking_number)
            parcel_status_header = find_by_xpath(driver, '//div[@class="header__status-header"]')
            parcel_status = find_by_xpath(driver, '//div[@class="header__status-text"]')
            if is_visible(parcel_status_header) and is_visible(parcel_status):
                assert parcel_status.text == positive_status
