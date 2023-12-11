import unittest
import sys
import pathlib
from homeworks import *

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))


""" Оберіть від 3 до 5 різних домашніх завдань
- перетворюєте їх у функції (якщо це потрібно)
- створіть в папці файл homeworks.py куди вставте ваші функції з дз
- та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
-- імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""

class LongestWordTesting (unittest.TestCase):
    """
    Testing of longest_word() function.
    """

    def test_positive_01(self):
        """ Test using correct and expected data: list of str """
        list_of_words = ['samsung', 'apple', 'xaomi']
        expected_res = 'samsung'
        actual_res = longest_word(list_of_words)
        self.assertEqual(expected_res, actual_res, msg=f"The longest word isn't correct!\n"
                                                       f"{expected_res} != {actual_res}")

    def test_positive_02(self):
        """ Test using correct and expected data with two equal items in list """
        list_of_words = ['flower', 'book', 'lesson']
        expected_res = 'flower'
        actual_res = longest_word(list_of_words)
        self.assertEqual(expected_res, actual_res, msg=f"The longest word isn't correct!\n"
                                                       f"{expected_res} != {actual_res}")

    def test_negative_03(self):
        """ Test using uncorrected data: str instead of list """
        str_of_words = "samsung, apple, xaomi"
        expected_res = TypeError
        with self.assertRaises(TypeError):
            result = longest_word(str_of_words)


class ExcludeTesting(unittest.TestCase):
    """
    Testing of exclude() function.
    """

    def test_positive_01(self):
        """ Test using correct and expected data: list, str """
        excl = 'mango'
        fruits_list = ['apple', 'banana', 'orange', 'grape', 'mango']
        expected_res = ['apple', 'banana', 'orange', 'grape']
        actual_res = exclude(fruits_list, excl)
        self.assertEqual(expected_res, actual_res, msg="The actual object is different than expected.")

    def test_positive_02(self):
        """ Test using correct and expected data: tuple, str """
        excl = 'bmw'
        cars_tuple = ('audi', 'bmw', 'mustang')
        expected_res = ['audi', 'mustang']
        actual_res = exclude(cars_tuple, excl)
        self.assertEqual(expected_res, actual_res, msg="The actual object is different than expected.")

    def test_negative_03(self):
        """ Test using uncorrected data: int as 'obj', 'str' """
        obj_int = 542154
        excl = '54'
        expected_res = TypeError
        with self.assertRaises(TypeError):
            result = exclude(obj_int, excl)

    def test_negative_04(self):
        """ Test using uncorrected data: list, int as 'excl' """
        nums_list = ['123', '456', '789']
        excl = 123
        expected_res = TypeError
        with self.assertRaises(TypeError):
            result = exclude(nums_list, excl)


class DistanceCostsTesting(unittest.TestCase):
    """
    Testing of distance_costs() function.
    """

    def test_positive_01(self):
        """ Test using correct and expected data: int, int, int """
        dist = 1200
        capacity = 52
        flow_100 = 11
        expected_res = (f"The trip of {1200} km will require {132} liters of gasoline, "
                        f"so you will have to refuel at least {2} times.")
        actual_res = distance_costs(dist, capacity, flow_100)
        self.assertEqual(expected_res, actual_res, msg="The value of 'liters of gasoline' or 'times refuel' is "
                                                       "different than expected.")

    def test_positive_02(self):
        """ Test using correct and expected data: int, int, int. Test of condition fulfillment: total_gas < 1 """
        dist = 10
        capacity = 48
        flow_100 = 9
        expected_res = (f"The trip of {dist} is very short, so you should refuel only one time before the trip, "
                        f"because you need less than 1 litter of gasoline.")
        actual_res = distance_costs(dist, capacity, flow_100)
        self.assertEqual(expected_res, actual_res, msg="The value of 'liters of gasoline' or 'times refuel' is "
                                                       "different than expected.")

    def test_positive_03(self):
        """ Test using correct and expected data: int, int, int. Test of condition fulfillment: refuel < 1 """
        dist = 10
        capacity = 52
        flow_100 = 11
        expected_res = (f"The trip of {dist} is very short, so you should refuel only one time before the trip, "
                        f"because you need only {1} litters of gasoline.")
        actual_res = distance_costs(dist, capacity, flow_100)
        self.assertEqual(expected_res, actual_res, msg="The value of 'liters of gasoline' or 'times refuel' is "
                                                       "different than expected.")

    def test_negative_04(self):
        """ Test using uncorrected data: str instead of int """
        dist = '10'
        capacity = 52
        flow_100 = '11'
        expected_res = TypeError
        with self.assertRaises(TypeError):
            result = distance_costs(dist, capacity, flow_100)


class MultTableTesting(unittest.TestCase):
    """
    Testing of multiplication_table() function.
    """

    def test_positive_01(self):
        """ Test using correct and expected data: positive int """
        mult_num = 12
        expected_res = "12x1=12\n12x2=24\n"
        actual_res = multiplication_table(mult_num)
        self.assertEqual(expected_res, actual_res, msg="The result of multiplication table isn't like expected!")

    def test_negative_02(self):
        """ Test using uncorrected data: str instead of int """
        mult_num = '12'
        expected_res = TypeError
        with self.assertRaises(TypeError):
            result = multiplication_table(mult_num)

    def test_negative_03(self):
        """ Test using uncorrected data: negative int """
        mult_num = -12
        expected_res = ValueError
        with self.assertRaises(ValueError):
            result = multiplication_table(mult_num)


if __name__ == '__main__':
    unittest.main(verbosity=2)

# Ran 14 tests in 0.007s OK