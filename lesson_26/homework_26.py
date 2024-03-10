"""
Написати тест, що вводить трекінг посилки на сайті НП

https://tracking.novaposhta.ua/#/uk/

та отримує статус посилки в теркінгу, напр.

<div data-v-631babf2="" class="header__parcel-dynamic-status px-4 d-flex align-center">
<div data-v-631babf2="" class="d-flex flex-column status-icon mr-4 status-icon-grey">
<!----></div>
<div data-v-631babf2="" class="flex-grow-1"
<div data-v-631babf2="" class="header__status-header"> Зараз: </div><!---->
<div data-v-631babf2="" class="header__status-text">Посилка отримана </div>
</div></div>

== Посилка отримана

Виконання:

    Оновити форк
    створити гілку
    у файл lesson_26/lesson_26.py додати нові def з новими хпазами
    додати файл lesson_26/test_homework_26.py - туди додати нові тести
    Створити ПР
    написати ПР у відповіді в ЛМС
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from lesson_26 import *


def test_parcel_status():
    driver = get_url(novapost_url)
    element = find_by_id(driver, cmr_input_id)
    element.click()
    input_to(element, parcel_number)
    search_button = find_by_id(driver, search_button_id)
    search_button.click()
    driver.implicitly_wait(2)
    parcel_status = find_by_xpath(driver, cmr_status_xpath)
    assert "Отримана" in parcel_status.text
