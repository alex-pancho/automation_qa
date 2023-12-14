# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = 'yellow'
if alien_color == 'yellow':
    print('Сongratulations you earned 5 points')


# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = 'yellow'
if alien_color == 'green':
    print('Сongratulations you earned 5 points')
else:
    alien_color == 'yellow'
    print('Сongratulations you earned 10 points!')


# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_color = 'red'
if alien_color == 'green':
    print('Сongratulations you earned 5 points')
elif alien_color == 'red':
    print('Сongratulations you earned 15 points!')
else:
    alien_color == 'yellow'
    print('Сongratulations you earned 10 points!')

alien_color = ['green', 'yellow', 'red']
print(alien_color)

for i in alien_color:
    print(i)



# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""

pizza_toppings = []

while True:
    topping = input("Enter a pizza topping (type 'quit' to finish): ")

    if topping.lower() == 'quit':
        break

    pizza_toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print("Your pizza toppings are:")
for topping in pizza_toppings:
    print(topping)

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр цілого числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть число: 12345
Сума цифр числа 12345: 15
"""
user_input = input("Enter the number: ")

sum_of_digits = 0

for digit in user_input:
    if digit.isdigit():
        sum_of_digits += int(digit)

print(f"The sum of the digits of the number {user_input}: {sum_of_digits}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""

total_sum = 0

while True:
    number = float(input("Enter a number (enter 0 to finish): "))

    if number == 0:
        break

    total_sum += number

print(f"The sum of the entered numbers (excluding 0) is: {total_sum}")

# task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
for attempt in range(1, max_guesses + 1):
    guess = int(input(f"Attempt {max_guesses}/{max_guesses}: Enter your guess (between 1 and 20): "))
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
filtered_fruits = [fruit for fruit in fruits if fruit != "orange"]

print(filtered_fruits)


# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x**2 for x in numbers if x % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]
