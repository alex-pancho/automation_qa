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


#
# def calculate_sum_until_zero_entered():
#     """
#     Функція, яка просить користувача ввести числа, доки він не введе 0.
#     Підраховує суму всіх введених чисел, окрім 0, і виводить її на екран.
#
#     :return: Сума введених чисел.
#     """
#     total_sum = 0
#
#     while True:
#         user_input = input("Введіть число (для завершення введіть 0): ")
#
#         if user_input.isdigit():
#             num = int(user_input)
#         else:
#             print("Некоректний ввід. Будь ласка, введіть число.")
#             continue
#
#         if user_input == '0':
#             break
#
#         total_sum += num
#
#     return total_sum
#
# result = calculate_sum_until_zero_entered()
# print(f"Результат сумування: {result}")

def calculate_average(numbers):
    """
    Функція, яка розраховує середнє арифметичне для списку чисел.

    """
    if not numbers:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return average

