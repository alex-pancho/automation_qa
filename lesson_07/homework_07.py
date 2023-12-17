# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            pass
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


def sum_of_integers(a: int, b: int):
    """ функція, яка обчислює суму двох чисел """
    return a + b


print("сумма двох чисел", sum_of_integers(8, 2))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average_value(a_1: int):
    """функція яка розрахує середнє арифметичне списку чисел """
    return sum(a_1) // len(a_1)


test_list = [13, 7, 4]
print('Cереднє арифметичне списку чисел', average_value(test_list))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reversed_string(text: str):
    """ приймає рядок та повертає його у зворотному порядку """
    return text[::-1]


test_string = "Нехай проблеми та незгоди не роблять Вам в житті погоди. Хай вам щастить...і будьте...здорові"
print(reversed_string(test_string))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def find_longest_word(testlist: list):
    """ приймає список слів та повертає найдовше слово у списку """
    words = max(testlist, key=len)
    return words


test_line = ["раз", "чотири", "хробашашашки"]
print(find_longest_word(test_line))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# Task1 from previous homework

def average(testlist: list):
    """functions counts average value from list"""
    average_result = sum(testlist) // len(testlist)
    return average_result


new_list = [12, 8, 4]
print(f"Average value of {new_list} = ", average(new_list))


# Task2 from previous homework
# немного переделал задачу про зеленого инопланетянина


def alien_colour_verification(alien_colour: str):
    """function checks if alien colour is green, if its true - gives 5 points"""
    if alien_colour != 'green':
        return "Прибулець не зелений"
    else:
        return "Гравець щойно заробив 5 балів"


cosmic_invader_colour = "red"
print(alien_colour_verification(cosmic_invader_colour))


# Task3 from previous homework
# немного переделал задачу проверки списка на дубликаты


def duplicate_verification(verification_list: list):
    """Function checks list if there are duplicated values"""
    duplicates = ((len(verification_list)) == (set(verification_list)))
    if not duplicates:
        return "дублікати є"
    else:
        return "дублікатів нема"


big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
print(duplicate_verification(big_list))


# Task4 from previous homework
# замена в словаре ключей на значения и наоборот
def reversed_dict(somedict: dict):
    """function returns dictionary with reversed key to values and vice versa"""
    new_dict = {}
    for key, value in add_dict.items():
        new_dict[value] = key
    return new_dict


add_dict = {"a": 1, "b": 2, "c": 2, "d": 3, 'size': 12}
print("Словник в якому ключі та значення замінені місцями", reversed_dict(add_dict))
