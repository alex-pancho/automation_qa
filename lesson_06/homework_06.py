import random


# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = 'red'
if alien_color == 'green':
    print("Congratulations! You've got 5 points!")


# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = 'yellow'
if alien_color == 'green':
    print("Congratulations! You've got 5 points!")
else:
    print("Congratulations! You've got 10 points!")


# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_color = ['green', 'yellow', 'red']
for color in alien_color:
    if color == 'green':
        print("Congratulations! You've got 5 points!")
    if color == 'red':
        print("Congratulations! You've got 15 points!")
    elif color != 'green':
        print("Congratulations! You've got 10 points!")


# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
pizza_topping = []
while True:
    topping = input("Enter pizza topping (enter 'quit' to stop): ")
    if topping != 'quit':
        pizza_topping.append(topping)
        print("Anything else? ")
        continue
    if not pizza_topping:
        print("Okay, we won't add anything to your pizza.")
    if pizza_topping:
        print(f"Well, the ingredients added to your pizza are: {', '.join(pizza_topping)}.")
    break


# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
user_int = input("Enter an integer: ")
sum_int = 0
for item in user_int:
    sum_int += int(item)
print(f"Sum of integers {int(user_int)} is {sum_int}.")


# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
integer = 0
while True:
    input_int = int(input("Enter an integer for sum (enter '0' to quit): "))
    if input_int != 0:
        integer += input_int
        print("Sum to...")
        continue
    if input_int == 0:
        break
print(f"Sum of your integers is: {integer}")


# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
secret_number = random.randint(1, 20)
print(secret_number)
guesses = 0
max_guesses = 5

while True:
    guess = int(input("Вгадайте число від 1 до 20: "))
    if secret_number != guess:
        guesses += 1
        if guess >= secret_number:
            print("Занадто велике число!")
        elif guess <= secret_number:
            print("Занадто маленьке число!")

        if guesses == max_guesses:
            print(f"Іншого разу пощастить! Число було: {secret_number}.")
            break
        print(f"У Вас залишилось {max_guesses - guesses} спроб! ")
    else:
        print("Вітаємо! Ви вгадали число!")
        break


# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]

for item in fruits:
    if item != 'orange':
        print(item)
        continue


# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i ** 2 for i in numbers if i % 2 == 0]
print(result)  # [4, 16, 36, 64, 100]