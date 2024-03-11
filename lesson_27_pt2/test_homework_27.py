from homework_27 import *

base_url = "https://www.lastingdynamics.com/"


def test_click_contact_us():
    driver = get_url(base_url)
    with driver:
        contact_us_btn = find_by_xpath(driver, '//*[@id="link_button-1830-12"]')
        if is_visible(contact_us_btn):
            click(driver, contact_us_btn)
            contact_us_header = find_by_xpath(driver, '//*[@id="headline-84-6141"]')
            print(contact_us_header.text)
            assert contact_us_header.text.startswith("Looking for a tech partner?")


def test_ld_logo_present():
    driver = get_url(base_url)
    with driver:
        ld_logo = find_by_xpath(driver, '//*[@id="logo-classic"]')
        if is_visible(ld_logo):
            assert True


def test_our_projects_btn():
    driver = get_url(base_url)
    with driver:
        our_projects_btn = find_by_xpath(driver, '//*[@id="link_button-1831-12"]')
        if is_visible(our_projects_btn):
            assert our_projects_btn.text == "Our Projects"


def test_menu_btn():
    driver = get_url(base_url)
    with driver:
        menu_btn = find_by_xpath(driver, '//*[@id="div_block-1143-7"]')
        if is_visible(menu_btn):
            click(driver, menu_btn)
            book_call_btn = find_by_xpath(driver, '//*[@id="link_button-1238-7"]')
            if is_visible(book_call_btn):
                assert book_call_btn.text == "Book a call"
