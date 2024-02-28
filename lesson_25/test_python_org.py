from lesson_25 import *
import time


def test_search():
    driver = get_url(python_url)
    search = find_by_name(driver, "q")
    input_to(search, "python")
    time.sleep(1)
    search_results = find_by_xpath(driver, '//ul[@class="list-recent-events menu"]')
    assert "No results found." not in search_results.text

def test_search_negative():
    driver = get_url(python_url)
    search = find_by_name(driver, "q")
    input_to(search, "bjdjbddugbcskfcs")
    time.sleep(1)
    search_results = find_by_xpath(driver, '//ul[@class="list-recent-events menu"]')
    assert "No results found." in search_results.text
