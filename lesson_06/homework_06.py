# task 1
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
print("Task #1:")
alien_color = "green"
if alien_color == "green":
    print(f"Alien color is {alien_color}.You receive 5 points!")

# task 2
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
print("Task #2:")
alien_color = "red"
if alien_color == "green":
    print(f"Alien color is {alien_color}.You receive 5 points!")
else:
    print(f"Alien color is {alien_color}.You receive 10 points!")

# task 3
# task 4
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
print("Task #3-4:")
alien_color = ["green", "yellow", "red"]
for i in alien_color:
    if i == "green":
        print(f"Alien color is {i}.You receive 5 points!")
    elif i == "red":
        print(f"Alien color is {i}.You receive 15 points!")
    else:
        print(f"Alien color is {i}.You receive 10 points!")

# task 5
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
print("Task #5:")
pizza_topping = []
while True:
    toppingAdd = input("Add topping:")
    if toppingAdd == "quit":
        break
    pizza_topping.append(toppingAdd)
print(f"You added {pizza_topping} to pizza")

# task 6
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
print("Task #6:")
num = input("Add digit: ")
sumNum = 0
if not num.isdigit():
    print("Enter digit!!!")
elif int(num) == 0:
    print("Digit must be above 0!")
else:
    for i in num:
        if int(i) % 2 == 0:
            sumNum = sumNum + int(i)
print(f"Sum of the digit {num} = {sumNum}")

# task 7
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
print("Task #7:")
total_sum = 0
while True:
    addDig = int(input("Add digit (0 - to calculate): "))
    if addDig == 0:
        break
    else:
        plus = input("Enter addition sign: ")
        total_sum = total_sum + addDig
print(f"Sum = {total_sum}")

#task 8
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
print("Task #8:")
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
for guesses in range(max_guesses):
    attempt = int(input("Enter number between 1 to 20: "))

    if attempt > secret_number:
        print("Try smaller digit")
    elif attempt < secret_number:
        print("Try biggest number")
    elif guesses == max_guesses:
        print("You spent all attempts")
    else:
        print(f"You guessed the number! ({secret_number})")
        break

# task 9
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
print("Task #9:")
for i in fruits:
    if i == "orange":
        continue
    print(i)

# task 10
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
print("Task #10:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i * i for i in numbers if i % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]
