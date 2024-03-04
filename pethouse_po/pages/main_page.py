from lesson_27_pt2.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locators = dict(
        home_page_button_xpath='//*[@id="tpl-logo"]',

        profile_button_xpath="(//span[@class='hidden-tablet'])[1]",
        login_form_xpath="(//div[@class='vex-content']//form)[1]",

        search_field_xpath='//*[@id="search"]',
        not_found_xpath="(//div[@class='tpl-prods-wrapper z2-search-page']//div)[1]",

        basket_button_xpath="//div[@class='header-cart']//a[1]",
        count_in_basket_xpath="//span[@class='quantity large-int']",

        payment_delivery_button_xpath="(//a[@class='ph-header-phone'])[1]",
        all_promotions_button_xpath="(//div[@class='main-header-link']//a)[1]",

        appstore_a="((//div[@class='ph-bubble-items'])[2])/a[1]",
        appstore_app_button_xpath="(//img[@alt='Pethouse App'])[1]",

        contacts_button_xpath="//li[@class='header-contacts']//span[1]",
        contacts_form_xpath="//div[@class='vex-content']//form[1]",

        menu_cats_button_xpath="//li[@id='tpl-top-menu-first-li-2']/a[1]",
        menu_cats_block_xpath="(//a[@class='first-level-a']/following-sibling::ul)[2]",
        menu_cats_dry_food_button_xpath="(//*[@id='tpl-top-menu-first-li-2']//child::a[1])[2]",

    )

