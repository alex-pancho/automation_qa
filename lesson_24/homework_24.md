### Практика з x-path
складність: легка

1. Оберіть сайт, який ви збираєтеся тестувати
2. Напишіть не менш ніж 10 x-path до елементів сайту, що важливі для пперевірки його функцональності.

Ваші відповіді і адресу сайту додате у цей файл нижче.
Робота виконується в новій гілці і здається як PR у репозиторій викладача.



site - https://www.sinsay.com/ua/uk/
1 input_email = '//*[@id="loginRegisterRoot"]/div/div[1]/div/form/div[1]/div/label'
2 input_password = '//*[@id="login[password]_id"]'
3 log_in_button = '//*[@id="loginRegisterRoot"]/div/div[1]/div/form/button'
4 create_account_button = '//*[@id="loginRegisterRoot"]/div/div[2]/div/form/button'
5 add_product_to_favorite = '//*[@id="categoryProducts"]/article[2]/figure/div/div/div'
6 add_to basket = '//*[@id="quantity-section"]/button'
7 go_to_cart = '//*[@id="headerWrapper"]/div/div[3]/button[2]'
8 shopping_cart_preview= '/html/body/div[7]/div[2]/div[2]/button/div' 
9 create_order = '//*[@id="cartRoot"]/div/div[2]/div[1]/div[2]/button'
10 remove_product = '//*[@id="cartRoot"]/div/div[1]/div[2]/div/button'