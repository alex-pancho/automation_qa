def sum_two_numbers(a, b):
    """
    Функція, яка обчислює суму двох чисел.
    """
    result = a + b
    return result


def reverse_string(input_string):
    """
    Функція, яка повертає рядок у зворотньому порядку.

    """
    reversed_string = input_string[::-1]
    return reversed_string



def calculate_average(numbers):
    """
    Функція, яка розраховує середнє арифметичне для списку чисел.

    """
    if not numbers:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return average

