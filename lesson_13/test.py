import unittest
import homework_13


class TestHumanMethods(unittest.TestCase):
    def test_eat(self):
        human = homework_13.Human("Oleg", "Petrov", "01.01.2000", "male")
        human.eat()
        self.assertEqual(human.energy, 105)

    def test_sleep(self):
        human = homework_13.Human("Oleg", "Petrov", "01.01.2000", "male")
        human.sleep()
        self.assertEqual(human.energy, 110)

    def test_talk(self):
        human = homework_13.Human("Oleg", "Petrov", "01.01.2000", "male")
        human.talk()
        self.assertEqual(human.energy, 95)

    def test_walk(self):
        human = homework_13.Human("Oleg", "Petrov", "01.01.2000", "male")
        human.walk()
        self.assertEqual(human.energy, 90)

    def test_homework(self):
        human = homework_13.Human("Oleg", "Petrov", "01.01.2000", "male")
        human.homework()
        self.assertEqual(human.energy, 10)


class TestNegativeHumanMethods(unittest.TestCase):
    def test_talk_much(self):
        human = homework_13.Human("Oleg", "Petrov", "01.01.2000", "male")
        # Занадто багато раз викликаємо метод говорити, щоб вичерпати енергію
        for _ in range(25):
            human.talk()
        self.assertEqual(human.energy, 0)

    def test_walk_much(self):
        human = homework_13.Human("Oleg", "Petrov", "01.01.2000", "male")
        # Занадто часто викликаємо метод ходити, щоб вичерпати енергію
        for _ in range(15):
            human.walk()
        self.assertEqual(human.energy, 0)

    def test_homework_much(self):
        human = homework_13.Human("Oleg", "Petrov", "01.01.2000", "male")
        # Занадто часто викликаємо метод робити_домашку, щоб вичерпати енергію
        for _ in range(10):
            human.homework()
        self.assertEqual(human.energy, 0)


if __name__ == '__main__':
    unittest.main()
