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
import function_homework_08

class PositiveTests(unittest.TestCase):
    def test_calc_average(self):
        """Test calculation of average"""
        input_numbers = [1, 2, 3, 6] 
        expected = 3
        actual_result = function_homework_08.calc_average(input_numbers) 
        self.assertEqual(expected, actual_result, msg=f"calculation of average is failed. Average of list {input_numbers}={expected}" )
    
    def test_calc_average_for_same_numbers(self):
     """test calculation of average for the same numbers"""
     input_numbers = [2, 2, 2, 2] 
     expected = 2
     actual_result = function_homework_08.calc_average(input_numbers) 
     self.assertTrue(expected == actual_result, msg=f"calculation of average for the same numbers is failed. Average of list {input_numbers}={expected}")

    def test_calc_average_for_longList(self):
     """test calculation of average for the long list"""
     input_numbers = list(range(1, 5000))
     expected = 2500
     actual_result = function_homework_08.calc_average(input_numbers) 
     self.assertEqual(expected, actual_result, msg=f"calculation of average for the long list is failed. Average of list {input_numbers}={expected}")

    def test_calc_average_for_single_element(self):
        """test calculation of average for the single element"""
        input_numbers = [5]
        expected = 5
        actual_result = function_homework_08.calc_average(input_numbers) 
        self.assertEqual(expected, actual_result, msg=f"calculation of average for the single element is failed. Average of list {input_numbers}={expected}")

    def test_sum_of_numbers(self):
        """test sum of numbers"""
        input_a = 5
        input_b = 7
        expected_result = 12
        actual_result = function_homework_08.sum_of_numbers(input_a, input_b) 
        self.assertTrue(expected_result == actual_result, msg=f"sum of numbers is failed. {input_a}+{input_b}={actual_result} ")
       
    def test_sum_of_float_numbers(self):
        """test sum of float numbers"""
        input_a = 5.77
        input_b = 7.12
        expected_result = 12.9
        actual_result = function_homework_08.sum_of_numbers(input_a, input_b)  
        self.assertAlmostEqual(expected_result, actual_result, 1, msg=f"sum of float numbers is failed {input_a}+{input_b}={actual_result}")

    def test_of_negative_numbers(self):
        """test sum of negative numbers"""
        input_a = -5
        input_b = -7
        expected_result = -12
        actual_result = function_homework_08.sum_of_numbers(input_a, input_b) 
        self.assertEqual(expected_result, actual_result, msg=f"sum of negative numbers is failed. {input_a}+{input_b}={actual_result} ")     
    
    
    def test_of_search_longest_word(self):
        """test of search longest word from list"""
        input_list = ["first", "second", "third"]
        expected_result = "second"
        actual_result = function_homework_08.longest_word(input_list)
        self.assertEqual(expected_result, actual_result, msg="search longest word from list is failed")


    def test_of_search_word_empty_list(self):
        """test of search longest word from empty list"""
        input_list = []
        with self.assertRaises(ValueError):
            return(function_homework_08.longest_word(input_list))     
           

    def test_list_word_with_emty_elements(self):
        """test list with empty elements"""
        input_list = ["", "", "third"]
        expected_result = "third"
        actual_result = function_homework_08.longest_word(input_list)
        self.assertEqual(expected_result, actual_result, msg=f"test word list with empty elements is failed")

if __name__ == '__main__':
    unittest.main(verbosity=2)


