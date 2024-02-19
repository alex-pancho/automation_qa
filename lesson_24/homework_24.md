### Практика з x-path
складність: легка

1. Оберіть сайт, який ви збираєтеся тестувати
2. Напишіть не менш ніж 10 x-path до елементів сайту, що важливі для пперевірки його функцональності.

Ваші відповіді і адресу сайту додате у цей файл нижче.
Робота виконується в новій гілці і здається як PR у репозиторій викладача.

url_signup = "https://www.testgorilla.com/demo-signup/"

FIRST_NAME = (By.XPATH, "//input[@id = "firstname-ed48c067-0da8-415c-89d4-079f9adc675e"]")
LAST_NAME = (By.XPATH, "//input[@id = "lastname-ed48c067-0da8-415c-89d4-079f9adc675e"]")
COMPANY_NAME = (By.XPATH, "//div[@class="input"]//input[@name="company"]")
WORK_EMAIL_ADDRESS = (By.XPATH, "//fieldset[@class="form-columns-1"]//div[@class = "input"]//input[@autocomplete="email"]")
WORKED_PEOPLE_DROPDOWN = (By.XPATH, "//div[@class = "input"]//select[@id = "fte_segmentation__demo_sign_up_-ed48c067-0da8-415c-89d4-079f9adc675e"]")
OPTION_F = (By.XPATH, "//div[@class = "input"]//select[@name]//option[text()= "f. 201-300"]")
BUTTON_NEXT = (By.XPATH, "//div[@class = "actions"]//input[@value = "Next"]")
ANCHOR = (By.XPATH, "//div[@class = "rc-anchor-invisible-text"]")
LINK_PRIVACY = (By.XPATH, "//div[@class="rc-anchor-invisible-text"]//div[@class = "rc-anchor-pt"]//a[text() = "Privacy"]")
LINK_TERMS = (By.XPATH, "//div[@class="rc-anchor-invisible-text"]//div[@class = "rc-anchor-pt"]//a[text() = "Terms"]")


