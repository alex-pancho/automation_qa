"""
POSITIVE TEST FOR HOME PAGE https://pethouse.ua/ua/shop/koshkam/
"""
import pytest
from pethouse_po.conftest import driver_shop_cats, shop_cats_page
from pethouse_po.pages.src import *


def test_shop_cats_page(driver_shop_cats):
    """Test that the section of shop is cats section, and it has correct url."""
    assert URL_SHOP_CATS == driver_shop_cats.current_url, \
        f"It seems homepage button has incorrect link! Current url: {driver_shop_cats.current_url}"


@pytest.mark.parametrize("index, title", [
    (1, 'Годування'),
    (2, 'Ветеринарна аптека'),
    (3, 'Догляд та гігієна'),
    (4, 'Ігри та розваги'),
    (5, 'Прогулянки і подорожі'),
    (6, 'Одяг і аксесуари'),
    (7, 'Інструменти для догляду'),
    (8, 'Косметика'),
    (9, 'Домашній затишок'),
    (10, 'Корекція поведінки'),
    (11, 'Чистота в будинку'),
    (12, 'Набори та подарунки'),
])
def test_shop_cats_subsections(shop_cats_page, index, title):
    """Test that cat shop has correct sections"""
    element = shop_cats_page.get_section_title(index)
    assert element.is_visible(), f"Not found: {element._locator}"

    title_text = element.get_text()
    assert title_text == title


@pytest.mark.parametrize("index, link", [
    (1, URL_SUHOI_KORM),
    (2, URL_VETERINARNYE_DIETY),
    (3, URL_KONSERVI),
    (4, URL_LAKOMSTVA),
    (5, URL_ZAMENITELI_MOLOKA),
    (6, URL_MISKI),
    (7, URL_VITAMINI),
    (8, URL_PROTIVOPARAZIT),
    (9, URL_DERMATOLOGIC),
    (10, URL_PREPARATY_GLAZA_USHI),
    (11, URL_PREPARATY_SUSTAVI),
    (12, URL_GASTROENTEROLOGIC),
    (13, URL_SERDCE),
    (14, URL_UROLOGIC),
    (15, URL_STOMATOLOGIC),
    (16, URL_ANTIBIOTIKI),
    (17, URL_VET_AKSESSUARY),
    (18, URL_SREDSTVA_PO_UHODY),
    (19, URL_TUALETY),
    (20, URL_NAPOLNITELI),
    (21, URL_PELENKI),
    (22, URL_IGRUSHKI),
    (23, URL_OSHEINIKI),
    (24, URL_PERENOSKI),
    (25, URL_RULETKI),
    (26, URL_ODEZHDA),
    (27, URL_FURMINATORI),
    (28, URL_RASCHESKI),
    (29, URL_KOGTEREZI),
    (30, URL_SHAMPUNI),
    (31, URL_KONDICIONERY),
    (32, URL_DUHI),
    (33, URL_SPALNYE_MESTA),
    (34, URL_PODSTILKI),
    (35, URL_DVERTSY),
    (36, URL_KOGTETOCHKI),
    (37, URL_OTPUGIVATELI),
    (38, URL_USPOKAIVAUSCHIE),
    (39, URL_PRIVLECHENIE),
    (40, URL_DLYA_DOMA),
    (41, URL_DLYA_CHISTKI),
    (42, URL_PETBOX),
    (43, URL_PETMERCH),
])
def test_food_subsections_href(shop_cats_page, index, link):
    """Test that subsections has correct links"""
    element = shop_cats_page.get_subsection_href(index)
    assert element.is_clickable(), f"Not clickable element: {element._locator}"

    href = element.get_attribute("href")
    assert href == link
