import unittest
from homework_13 import Human

class TestHuman(unittest.TestCase):
    def setUp(self):
        self.person1 = Human("John", "Johnny", "11/11/1990", "male")
        self.person2 = Human("Ana", "Dee", "02/04/2003", "female")

    def test_eat(self):
        self.person1.eat()
        self.assertEqual(self.person1.energy, 105)

    def test_sleep(self):
        self.person2.sleep()
        self.assertEqual(self.person2.energy, 110)

    def test_talk(self):
        self.person1.speak()
        self.assertEqual(self.person1.energy, 95)

    def test_walk(self):
        self.person2.walk()
        self.assertEqual(self.person2.energy, 90)

    def test_do_homework(self):
        self.person1.make_hm()
        self.assertEqual(self.person1.energy, 10)


if __name__ == '__main__':
    unittest.main()