# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number: int) -> str:
    """
    This function returns the multiplication table of a given digit up to 25.
    :param number: Int
    :return: multiplication table.
    """
    result_table = ''
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:
            break
        result_table += f"{number}x{multiplier}={result}\n"
        multiplier += 1

    return result_table


print(multiplication_table(3))
# result:
# 3x1=3
# ...
# 3x8=24


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_ints(a, b) -> int or float:
    """
    This function returns result of sum two numbers (float or/and int).
    """
    print(f"{a} + {b} = {a + b}")
    return a + b


sum_ints(8.55, 19)  # 8.55 + 19 = 27.55


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def arithmetic_mean(nums) -> float:
    """
    This function returns an arithmetic mean of any count of numbers in list.
    :param nums: list of ints/floats
    :return: arithmetic mean of nums (float)
    """
    arithmetic = sum(nums) / len(nums)
    return arithmetic


list_of_nums = [10, 40]
print(arithmetic_mean(list_of_nums))  # 25.0


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(string) -> str:
    """
    This function reverses any string.
    :param string: string
    :return: reversed string
    """
    return string[::-1]


my_str = "This is string to reverse!"
print(reverse_string(my_str))  # !esrever ot gnirts si sihT

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(words: list) -> str:
    """
    This function returns as result of the longest string in list.
    :param words: list of strings
    :return: longest str
    """
    result = max(words, key=len)
    return result


list_of_words = ['samsung', 'apple', 'xaomi']
print(longest_word(list_of_words))  # samsung

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2) -> int:
    """
    This function returns index of first letter of second string in first one.
    The function return '-1' if second string doesn't in first one.
    :param str1: str
    :param str2: str
    :return: index str2 in str1 // -1
    """
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1


str_1 = "Hello, world!"
str_2 = "world"
print(find_substring(str_1, str_2))  # 7

str_1 = "The quick brown fox jumps over the lazy dog"
str_2 = "cat"
print(find_substring(str_1, str_2))  # -1


# task 7-10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
# Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
# потрібно вивести на екран всі елементи списку, окрім "orange"

def exclude(obj, excl) -> list:
    """
    This function can exclude item from list/set/tuple/dict and return result.
    Your original variable won't be changed.
    :param obj: list/set/tuple/dict
    :param excl: str
    :return: Your variable (list) without excluding item
    """
    res = [item for item in obj if item != excl]
    return res


fruits_list = ["apple", "banana", "orange", "grape", "mango"]
print(exclude(fruits_list, 'orange'))
# ['apple', 'banana', 'grape', 'mango']


# task 8
# ...Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
# змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
# Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
# Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
# Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
# + напишіть цикл for що перебере і обробить всі значення списку alien_color


def alien_color_points(colors: list) -> str:
    """
    This function returns result of achived points for each color in list.
    :param colors: list
    :return: total qty of points (message)
    """
    points = 0
    for color in colors:
        if color == 'green':
            points += 5
        elif color == 'red':
            points += 15
        else:
            points += 10

    res = f"Congratulations! You achived {points} points!"
    return res


alien_color = ['yellow', 'green', 'red', 'blue']
total_points = alien_color_points(alien_color)
print(total_points)  # Congratulations! You achived 40 points!


# task 9
# Задано список чисел numbers, потрібно знайти список квадратів
# парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.

def square_pairwise_nums(nums) -> list:
    """
    This function returns the result of squaring all pairwise numbers in the list.
    :param nums: list of numbers
    :return: list of squaring pairwise numbers
    """
    result = [i ** 2 for i in nums if i % 2 == 0]
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9.8, 10]
print(square_pairwise_nums(numbers))  # [4, 16, 36, 64, 100]


# task 10
# Родина зібралася в автомобільну подорож із Харкова в Будапешт.
# Відстань між цими містами становить 1600 км.
# Відомо, що на кожні 100 км необхідно 9 літрів бензину.
# Місткість баку становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на заправку
# під час цієї подорожі, кожного разу заправляючи повний бак?

def distance_costs(dist, capacity, flow_100) -> str:
    """
    This function can calculete how much litters of gasoline you need for trip and how many times should refuel.
    :param dist: int (km)
    :param capacity: int (litter)
    :param flow_100: int (litter)
    :return: message (total gasoline, refuel times)
    """
    total_gas = int(dist / 100 * flow_100)
    refuel = int(total_gas / capacity)
    result = (f"The trip of {dist} km will require {total_gas} liters of gasoline, "
              f"so you will have to refuel at least {refuel} times.")
    return result


print(distance_costs(1600, 48, 9))
# The trip of 1600 km will require 144 liters of gasoline, so you will have to refuel at least 3 times.
