# homeworks
# task1.func1
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
from typing import Sized


def whole_price(months, payment: int):
    if months < 1:
        return "Warning: min month value = 1"
    else:
        return months * payment


# print(whole_price(12,500))


# task2.func2
def find_longest_word(testlist: list):
    """ приймає список слів та повертає найдовше слово у списку """
    words = max(testlist, key=len)
    return words


test_line = ["раз", "чотири", "хробашашашки"]
print(find_longest_word(test_line))


# task3.func3
# average_value = sum(small_list) / len(small_list)
# print("Cереднє арифметичне всіх елементів у списку small_list:",average_value)

def avg_value(test_list: list):
    return sum(test_list) / len(test_list)


testlist2 = [3, 7, 5]
# print(avg_value(testlist2))

#func4

def duplicate_verification(verification_list: list) -> object:
   """Function checks list if there are duplicated values"""
   duplicates = ((len(verification_list)) == (set(verification_list)))
   if not duplicates:
       return "дублікати є"
   else:
       return "дублікатів нема"
# big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# print(duplicate_verification(big_list))

