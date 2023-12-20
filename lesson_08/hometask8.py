import unittest
import homework8


class BananaTest(unittest.TestCase):

    def test_calculate_bananas_positive(self):
        apples = 5
        expected_bananas = 20
        actual_bananas = homework8.calculate_bananas(apples)
        self.assertEqual(actual_bananas, expected_bananas)

    def test_calculate_bananas_negative_invalid_input(self):
        apples = -5
        with self.assertRaises(ValueError):
            homework8.calculate_bananas(apples)


class TreeTest(unittest.TestCase):

    def test_positive_apple_tree(self):
        # Test when apple_tree is a positive number
        result = homework8.calculate_total_trees(10)
        self.assertEqual(result, 10 + (10 + 5) + (10 - 2))

    def test_zero_apple_tree(self):
        # Test when apple_tree is zero
        result = homework8.calculate_total_trees(0)
        self.assertEqual(result, 0 + (0 + 5) + (0 - 2))

    def test_negative_apple_tree(self):
        # Test when apple_tree is a negative number
        result = homework8.calculate_total_trees(-5)
        self.assertEqual(result, -5 + (-5 + 5) + (-5 - 2))


class TestCalculateTemperatures(unittest.TestCase):

    def test_positive_morning_temperature(self):
        # Test when morning_temperature is a positive number
        result = homework8.calculate_temperatures(25)
        expected_result = (25, 15, 19)
        self.assertEqual(result, expected_result)

    def test_zero_morning_temperature(self):
        # Test when morning_temperature is zero
        result = homework8.calculate_temperatures(0)
        expected_result = (0, -10, -6)
        self.assertEqual(result, expected_result)

    def test_negative_morning_temperature(self):
        # Test when morning_temperature is a negative number
        result = homework8.calculate_temperatures(-5)
        expected_result = (-5, -15, -11)
        self.assertEqual(result, expected_result)


class TestCalculateTotalCostBooks(unittest.TestCase):

    def test_positive_cost_book_1(self):
        # Test when cost_book_1 is a positive number
        result = homework8.calculate_total_cost_books(20)
        expected_result = 20 + (20 + 2) + ((20 + (20 + 2)) / 2)
        self.assertEqual(result, expected_result)

    def test_zero_cost_book_1(self):
        # Test when cost_book_1 is zero
        result = homework8.calculate_total_cost_books(0)
        expected_result = 0 + (0 + 2) + ((0 + (0 + 2)) / 2)
        self.assertEqual(result, expected_result)

    def test_negative_cost_book_1(self):
        # Test when cost_book_1 is a negative number
        result = homework8.calculate_total_cost_books(-5)
        expected_result = -5 + (-5 + 2) + ((-5 + (-5 + 2)) / 2)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()

    