# Функція на обрізання строки де перший параметр це строка а другий це число скільки символів цієї строки буде виведено
def my_substr(string, slice):
    index = 0
    new_string = ''
    while index < slice:
        new_char = string[index]
        new_string = new_string + new_char
        index = index + 1
    return new_string


# Приклад
# print(my_substr('My goal is Python!', 7)) # == My goal

def sum_of_two_numbers(number1, number2):
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


# # Приклад роботи функції
# num1 = int(input("Введіть перше число: "))
# num2 = int(input("Введіть друге число: "))
# print(sum_of_two_numbers(num1, num2))

def square_of_even_numbers(list_of_numbers):
    """
    Функція приймає список чисел та повертає список квадратів парних чисел.

    Parameters:
    list_of_numbers (list of int): Список чисел.

    Returns:
    list of int: Список квадратів парних чисел.
    """
    return [x ** 2 for x in list_of_numbers if x % 2 == 0]


# # Приклад використання функції:
# numbers = [2, 4, 6, 8, 10]
# result = square_of_even_numbers(numbers)
# print(result)  # [4, 16, 36, 64, 100]
