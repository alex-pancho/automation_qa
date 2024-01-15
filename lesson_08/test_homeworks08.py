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
import warnings

class Mytests(unittest.TestCase):

    def test1_trees_1(self):
        input_apple = 12
        input_peer = 12
        input_plum = 12
        expected = 36
        actual_result = homeworks.trees_total(input_apple, input_peer, input_plum)
        self.assertEqual(expected, actual_result, msg=f"Trees test 1 is FAILED")

    def test2_trees_2(self):
        input_apple = -12
        input_peer = 105
        input_plum = -8
        expected = input_plum + input_peer + input_apple
        actual_result = homeworks.trees_total(input_apple, input_peer, input_plum)
        self.assertNotEqual(expected, actual_result, msg=f"Trees test 2 is FAILED")

    def test3_trees_3(self):
        input_apple = 0
        input_peer = 0
        input_plum = 0
        expected = input_plum + input_peer + input_apple
        actual_result = homeworks.trees_total(input_apple, input_peer, input_plum)
        self.assertTrue(expected == actual_result, msg=f"Trees test 3 is FAILED")

    def test4_text_1(self):
        text = "Pfj   jfekk efk  jejfl            ejfkejhlkj;jorsg fehfqi  jhefqhk"
        expected = 1
        result = homeworks.space_delete(text)
        if "  " in result:
            actual_result = 0
        else:
            actual_result = 1
        self.assertEqual(expected, actual_result, msg=f"Text test 1 is FAILED")

    def test5_text_2(self):
        text = "Pfjjfekk"
        expected = 1
        result = homeworks.space_delete(text)
        if "  " in result and type(text) is str:
            actual_result = 0
        else:
            actual_result = 1
        self.assertEqual(expected, actual_result, msg=f"Text test 2 is FAILED")

    def test6_text_3(self):
        text = 22
        expected = 1
        result = str(homeworks.space_delete(text))
        if result != "Заданий текст не є строкою":
            actual_result = 0
        elif "  " in result:
            actual_result = 0
        else:
            actual_result = 1
        self.assertNotEqual(expected, actual_result, msg=f"Text test 3 is FAILED")

    def test7_word_1(self):
        words = "Тут буде чотири слова"
        expected = 4
        result = homeworks.words_count_in_sentence(words, 1)
        if result == "Заданий текст не є строкою":
            result = 0
        self.assertEqual(expected, result, msg=f"Words test 1 is FAILED")

    def test8_word_2(self):
        words = "Тут буде чотири слова. а тут три"
        expected = 3
        result = homeworks.words_count_in_sentence(words, 2)
        if result == "Заданий текст не є строкою":
            result = 0
        self.assertEqual(expected, result, msg=f"Words test 2 is FAILED")

    def test9_word_3(self):
        words = []
        expected = 0
        result = homeworks.words_count_in_sentence(words, 1)
        if result == "Заданий текст не є строкою":
            result = 0
        else:
            result = 1
        self.assertNotEqual(expected, result, msg=f"Words test 3 is FAILED")

    def test_10_word_4(self):
        words = "Тут буде чотири слова. а тут три"
        with self.assertRaises(IndexError):
            result = homeworks.words_count_in_sentence(words, 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)