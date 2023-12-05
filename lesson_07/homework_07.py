# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5: # має бути multiplier <= 5, або інше число, щоб не перевищувати 25
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25: # порівнюємо з числом, а не рядком "25"
            # Enter the action to take if the result is greater than 25
            break # зупиняємо цикл, якщо результат більший за 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1 # має бути multiplier, а не multi

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_of_two_numebrs(number1, number2):
    """
    Функція обчислює суму двох чисел.

    Parameters:
    number1 (int or float): Перше число.
    number2 (int or float): Друге число.

    Returns:
    int or float: Сума двох чисел.
    """
    if not (isinstance(number1, (int, float)) and isinstance(number2, (int, float))):
        return "Введіть числа"
    
    return f"Сума двох чисел {number1} та {number2} дорівнює: {number1 + number2}"

# Приклад роботи функції
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
print(sum_of_two_numebrs(num1, num2))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def sum_of_list(numbers):
    """
    Функція розраховує середнє арифметичне для списку чисел.

    Parameters:
    numbers (list of int or float): Список чисел.

    Returns:
    float: Середнє арифметичне чисел у списку.
    """
    if not numbers:
        return "Список порожній"

    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return round(avg, 2)

# Приклад роботи функції
numbers_to_average = [1.7, 15.87, 20.09, 25, 30.76, 35.12, 40.06, 45.71, 50.85, 55, 60.98, 65.12, 70.8]
print(sum_of_list(numbers_to_average))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers_string(string):
    """
    Функція повертає рядок у зворотньому порядку.

    Parameters:
    string (str): Вхідний рядок.

    Returns:
    str: Рядок, в якому порядок символів обернутий.
    """
    if not isinstance(string, str):
        return "Введіть рядок"
    return string[::-1]

# Приклад роботи функції
print(revers_string("hello, word!"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(list_of_words):
    """
    Функція приймає список слів та повертає найдовше слово у списку.

    Parameters:
    list_of_words (list of str): Список слів.

    Returns:
    str: Найдовше слово у списку.
    """
    if not list_of_words:
        return "Список порожній"
    longest = max(list_of_words, key=len)
    return longest

# Приклад роботи функції
random_words = ["apple", "banana", "orange", "grape", "mango", "pizza", "python", "keyboard", "coffee", "unicorn", "sepultura"]
print(longest_word(random_words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    """
    Функція яка приймає два рядки та повертає індекс першого входження другого рядка
    у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
    не є підрядком першого рядка.

    Parameters:
    str1 (str): Перший рядок.
    str2 (str): Другий рядок.

    Returns:
    int: Індекс першого входження другого рядка у перший рядок, або -1, якщо не знайдено.
    """

    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7

def sum_of_digits():
    """
    Функція приймає натуральне число від користувача та обчислює суму його цифр.
    Виводить результат на екран.
    """
    natural_number = input("Введіть натуральне число: ")
    
    sum_numbers = 0
    for digit in natural_number:
        sum_numbers += int(digit)
    
    print(f"Сума цифр числа {natural_number}: {sum_numbers}")

# Виклик функції:
sum_of_digits()


# task 8

def calculate_sum():
    """
    Функція просить користувача вводити числа, доки він не введе 0.
    Підраховує суму всіх введених чисел (окрім 0) та виводить результат на екран.
    """
    total_sum = 0

    while True:
        another_number = int(input("Введіть ваше число у калькулятор плюсів або 0 для виводу результату на єкран: "))
        total_sum += another_number

        if another_number == 0:
            break

    print(f"Сума ваших чисел дорівнює: {total_sum}")

# Виклик функції:
calculate_sum()


# task 9

def create_pizza_order():
    """
    Функція пропонує користувачеві вводити начинки для піци,
    доки він не введе 'quit'. Після введення кожної начинки виводить повідомлення про додавання до піци.
    Після того як користувач введе 'quit' на екран виводиться  список його додатків до піци
    """
    final_order = []

    while True:
        pizza_topping = input("Введіть яку начинку ви бажаєте додати? Або quit для виходу з меню додавання ")
        if pizza_topping.lower() == 'quit':
            break
        else:
            final_order.append(pizza_topping)
            print(f"Ми додали цю начинку '{pizza_topping}' до вашої піци")

    print("Ваша піцца з додатками:", final_order)

# Виклик функції:
create_pizza_order()


# task 10

def square_of_even_numbers(list_of_numbers):
    """
    Функція приймає список чисел та повертає список квадратів парних чисел.

    Parameters:
    list_of_numbers (list of int): Список чисел.

    Returns:
    list of int: Список квадратів парних чисел.
    """
    return [x**2 for x in list_of_numbers if x % 2 == 0]

# Приклад використання функції:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = square_of_even_numbers(numbers)
print(result)  # [4, 16, 36, 64, 100]


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""