from homework_28 import *


def test_click_contact_us(base_driver):
    contact_us_btn = find_by_xpath(base_driver, '//*[@id="link_button-1830-12"]')
    if is_visible(contact_us_btn):
        click(base_driver, contact_us_btn)
        contact_us_header = find_by_xpath(base_driver, '//*[@id="headline-84-6141"]')
        assert contact_us_header.text.startswith("Looking for a tech partner?")


def test_ld_logo_present(base_driver):
    ld_logo = find_by_xpath(base_driver, '//*[@id="logo-classic"]')
    if is_visible(ld_logo):
        assert True


def test_our_projects_btn(base_driver):
    our_projects_btn = find_by_xpath(base_driver, '//*[@id="link_button-1831-12"]')
    if is_visible(our_projects_btn):
        assert our_projects_btn.text == "Our Projects"


def test_menu_btn(base_driver):
    menu_btn = find_by_xpath(base_driver, '//*[@id="div_block-1143-7"]')
    if is_visible(menu_btn):
        click(base_driver, menu_btn)
        book_call_btn = find_by_xpath(base_driver, '//*[@id="link_button-1238-7"]')
        if is_visible(book_call_btn):
            assert book_call_btn.text == "Book a call"
