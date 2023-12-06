# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

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

def sum_two_numbers(a, b):
    """
    Функція, яка обчислює суму двох чисел.
    """
    result = a + b
    return result

num1 = 5
num2 = 7
sum_result = sum_two_numbers(num1, num2)
print(f"Сума {num1} і {num2} дорівнює {sum_result}")



# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def calculate_average(numbers):
    """
    Функція, яка розраховує середнє арифметичне для списку чисел.

    """
    if not numbers:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return average

number_list = [3, 5, 7, 10, 15]
result = calculate_average(number_list)

if result is not None:
    print(f"Середнє арифметичне для списку {number_list} дорівнює {result}")
else:
    print("Список чисел порожній.")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(input_string):
    """
    Функція, яка повертає рядок у зворотньому порядку.

    """
    reversed_string = input_string[::-1]
    return reversed_string

original_string = "Hello, World!"
result = reverse_string(original_string)
print(f"Оригінальний рядок: {original_string}")
print(f"Рядок у зворотньому порядку: {result}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def find_longest_word(word_list):
    """
    Функція, яка повертає найдовше слово зі списку.

    :param word_list: Список слів.
    :return: Найдовше слово.
    """
    if not word_list:
        return None

    longest_word = max(word_list, key=len)
    return longest_word

words = ["apple", "banana", "grapefruit", "kiwi", "strawberry"]
result = find_longest_word(words)

if result is not None:
    print(f"Найдовше слово у списку: {result}")
else:
    print("Список слів порожній.")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
        """
        Функція, яка повертає індекс першого входження другого рядка у перший рядок.

        :param str1: Перший рядок.
        :param str2: Другий рядок.
        :return: Індекс першого входження другого рядка або -1, якщо другий рядок не є підрядком першого рядка.
        """
        index = str1.find(str2)
        return index if index != -1 else -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
def create_pizza():
    """
    Функція, яка дозволяє користувачеві вводити начинки для піци, доки він не введе значення 'quit'.
    Кожну введену начинку додає до списку та виводить повідомлення про це.

#     """
    pizza_toppings = []
    pizza_topping = ""

    while pizza_topping.lower() != 'quit':
        pizza_topping = input("Введіть начинку для піци (або 'quit' для завершення): ")
        if pizza_topping.lower() != 'quit':
            print(f"Додаємо {pizza_topping} до вашої піци.")
            pizza_toppings.append(pizza_topping)

    print("Ваш список начинок для піци:")
    for topping in pizza_toppings:
        print(topping)

    return pizza_toppings

pizza_toppings_list = create_pizza()

# task 8

def has_duplicates_in_list(input_list):
    """
    Функція, яка перевіряє наявність дублікатів у списку.
    :return: True, якщо є дублікати, False - якщо немає.
    """
    return len(input_list) != len(set(input_list))

big_list = [1, 2, 3, 4, 5, 1]
result = has_duplicates_in_list(big_list)

if result:
    print("У списку big_list є дублікати.")
else:
    print("У списку big_list немає дублікатів.")

# task 9

def process_person_list(person_list):
    """
    Функція, яка обробляє список кортежів person_list, що містять ім'я та вік людей,
    і повертає словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
    а значення - списки імен людей, які потрапляють в кожен діапазон.

    """
    age_ranges_dict = {}

    for name, age in person_list:
        age_range_start = (age // 10) * 10
        age_range_end = age_range_start + 9
        age_range = f"{age_range_start}-{age_range_end}"

        if age_range in age_ranges_dict:
            age_ranges_dict[age_range].append(name)
        else:
            age_ranges_dict[age_range] = [name]

    return age_ranges_dict

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

result = process_person_list(person_list)
print(result)

# task 10

def calculate_sum_until_zero_entered():
    """
    Функція, яка просить користувача ввести числа, доки він не введе 0.
    Підраховує суму всіх введених чисел, окрім 0, і виводить її на екран.

    :return: Сума введених чисел.
    """
    total_sum = 0

    while True:
        user_input = input("Введіть число (для завершення введіть 0): ")

        if user_input.isdigit():
            num = int(user_input)
        else:
            print("Некоректний ввід. Будь ласка, введіть число.")
            continue

        if user_input == '0':
            break

        total_sum += num

    return total_sum

result = calculate_sum_until_zero_entered()
print(f"Результат сумування: {result}")

