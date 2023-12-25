""" Оберіть від 3 до 5 різних домашніх завдань
- перетворюєте їх у функції (якщо це потрібно)
- створіть в папці файл homeworks.py куди вставте ваші функції з дз
- та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
-- імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""

import unittest
import homeworks


class SomeTest(unittest.TestCase):
    def test_wholeprice(self):
        """Test calculates multiplication months on payment-per-month"""
        test_month = 12
        test_payment = 50
        expected_results = 600
        actual_results = homeworks.whole_price(test_month, test_payment)
        self.assertEqual(expected_results, actual_results, msg=f"Warning : some conditions are not correct, please "
                                                               f"verify input data")

    def test_price_payment_with_decimals(self):
        """Test calculates multiplication months on payment-per-month when payment has decimals"""
        test_month2 = 10
        test_payment_decimal = 1225.4
        expected_results = 12254
        actual_results = homeworks.whole_price(test_month2, test_payment_decimal)
        self.assertEqual(expected_results, actual_results, msg=f"Warning : some conditions are not correct, "
                                                               f"please verify input data")

    def test_wholeprice_with_invalid_month(self):
        """test how system will behave when invalid month value will be added"""
        test_month = 0.5
        test_payment = 50
        expected_results = 25
        actual_results = homeworks.whole_price(test_month, test_payment)
        self.assertNotEquals(expected_results, actual_results, msg=f"Warning : some conditions are not correct, "
                                                                   f"please verify input data")

    def test_longestword(self):
        """Test of functions that returns longest word in list"""
        test_words_list = ["monday", "tuesday", "wednesday"]
        expected_results = "wednesday"
        actual_results = homeworks.find_longest_word(test_words_list)
        self.assertEqual(expected_results, actual_results, msg=f"Warning : some conditions are not correct, please "
                                                               f"verify input data")

    def test_longestword_with_one_word(self):
        """Test of function that returns longest word in list when there is only one option"""
        test_words_list = ["friday"]
        expected_results = "friday"
        actual_results = homeworks.find_longest_word(test_words_list)
        self.assertEqual(expected_results, actual_results, msg=f"Warning : some conditions are not correct, please "
                                                               f"verify input data")

    def test_longestword_with_repeated_word(self):
        """Test of function that returns longest word in list when some options are repeated"""
        test_words_list = ["friday", "monday", "friday", "wednesday", "saturday", "wednesday"]
        expected_results = "wednesday"
        actual_results = homeworks.find_longest_word(test_words_list)
        self.assertEqual(expected_results, actual_results, msg=f"Warning : some conditions are not correct, please "
                                                               f"verify input data")




    def test_average(self):
        """Test of function that returns average value in list"""
        testlist_1 = [10, 20, 30]
        expected = 20
        actual_results = homeworks.avg_value(testlist_1)
        self.assertEqual(expected, actual_results, msg=f'Average value function is failed :'
                                                       f' {expected} is not average from {testlist_1}')


    def test_average_with_decimals(self):
        """Test of function that returns average value in list which contains decimal values"""
        testlist_decimals = [10.1, 20.25, 20.65]
        expected = 17
        actual_results = homeworks.avg_value(testlist_decimals)
        self.assertEqual(expected, actual_results, msg=f'Average value function is failed :'
                                                       f' {expected} is not average from {testlist_decimals}')

    def test_average_with_null(self):
        """Test of function that returns average value in list which contains zero values"""
        testlist_zeroes = [12, 0, 7, 0, 101]
        expected = 24
        actual_results = homeworks.avg_value(testlist_zeroes)
        self.assertEqual(expected, actual_results, msg=f'Average value function is failed :'
                                                       f' {expected} is not average from {testlist_zeroes}')



    def test_check_duplucates(self):
        """test of function that checks list for duplicates"""
        test_list11 = [12, 0, 7, 0, 101]
        expected = "дублікати є"
        actual = homeworks.duplicate_verification(test_list11)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(verbosity=2)
