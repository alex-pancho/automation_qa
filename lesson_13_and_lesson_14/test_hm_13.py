import unittest
from homework_13 import Human

class TestHumanClass(unittest.TestCase):
    def test_attributes(self):
        human = Human ("Іван", "Петров", "01.01.1990", "чоловік")
        self.assertEqual(human.ім_я, "Іван")
        self.assertEqual(human.прізвище, "Петров")
        self.assertEqual(human.дата_народження, "01.01.1990")
        self.assertEqual(human.стать, "чоловік")
        self.assertEqual(human.енергія, 100)

if __name__ == '__main__':
    unittest.main(verbosity=1)
