from homework_14 import *
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        user_1.logcount = 11
        user_2.logcount = 55
        user_1._access_type = "admin"
        user_3._access_type = "user"

    def tearDown(self):
        pass

    def test_getter(self):
        """tests logcount property getter func"""
        expected_res = 11
        actual_res = user_1.logcount
        self.assertEqual(expected_res, actual_res)

    def test_eq_different(self):
        """tests __eq__ func, checks if users access type equal(different is expected)"""
        expected_res = "Користувачі різні"
        actual_res = (user_1 == user_3)
        self.assertEqual(expected_res, actual_res)

    def test_eq_same(self):
        """test checks eq func - expected that user 3 and 4 has same access type"""
        expected_res = "Користувачі однакові"
        actual_res = (user_3 == user_4)
        self.assertEqual(expected_res, actual_res)

    def test_setter(self):
        """tests logcount property setter func"""
        expected_res = 55
        actual_res = user_2.logcount
        self.assertEqual(expected_res, actual_res)

    def test_str(self):
        """tests str function"""
        actual_res = f"Користувач: {user_4.name}, Електронна пошта: {user_4.email}, Рівень доступу: {user_4._access_type}"
        expected_res = "Користувач: Alena, Електронна пошта: alena@gmail.com, Рівень доступу: user"
        self.assertEqual(expected_res, actual_res)


if __name__ == '__main__':
    unittest.main()
