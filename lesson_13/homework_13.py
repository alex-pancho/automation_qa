"""Розробити клас Human.
Людина має:
    Ім'я
    Прізвище
    Дату народження
    Стать
    Енергію = 100
Люди можуть:
    Їсти (Енергія +5)
    Спати (Енергія +10)
    Говорити (Енергія -5)
    Ходити (Енергія -10)
    Робити домашку (Енергія -90)
if __name__ == "__main__":
    Створити 3 чоловіків та 2 жінок, Задати кожному з них виконання
    декількох дій, вивести в кого найбільше енергії лишилося.
Створити тести на клас та на атрибути класу.
"""
import unittest

class Human:
    def __init__(self, name, surname, birthday, sex):
        """
        Class representing a human with attributes: name, surname, birthday, sex, and initial energy set to 100.
        """
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.sex = sex
        self.energy = 100

    def eat(self):
        """
        Method to increase energy by 5.
        """
        self.energy += 5

    def sleep(self):
        """
        Method to increase energy by 10.
        """
        self.energy += 10

    def speak(self):
        """
        Method to decrease energy by 5.
        """
        self.energy -= 5

    def walk(self):
        """
        Method to decrease energy by 10.
        """
        self.energy -= 10

    def do_homework(self):
        """
        Method to decrease energy by 90.
        """
        self.energy -= 90

if __name__ == "__main__":
    human_1 = Human("Ivan", "Petrov", "01.01.1990", "man")
    human_2 = Human("Oleg", "Ivanov", "12.11.1995", "man")
    human_3 = Human("Alex", "Sidorov", "11.12.2000", "man")
    human_4 = Human("Maria", "Petrenko", "03.03.1985", "woman")
    human_5 = Human("Olga", "Petrenko", "01.06.1988", "woman")

    human_5.eat()
    human_5.sleep()
    human_4.sleep()
    human_4.walk()
    human_3.do_homework()
    human_3.eat()
    human_2.speak()
    human_1.walk()

    people = [human_1, human_2, human_3, human_4, human_5]

    people_energy = {human.name: human.energy for human in people}
    more_energy = max(people_energy, key= people_energy.get)

    print(f"The most energy is left in {more_energy}: {people_energy[more_energy]}")

class TestHumanClass(unittest.TestCase):
    def test_attributes(self):
        """
        Test to check if the attributes of the human are set correctly.
        """
        human = Human("Ivan", "Petrov", "01.01.1990", "man")
        self.assertEqual(human.name, "Ivan")
        self.assertEqual(human.surname, "Petrov")
        self.assertEqual(human.birthday, "01.01.1990")
        self.assertEqual(human.sex, "man")
    def test_eat(self):
        """
        Test for the 'eat' method, checking if energy increases by 5.
        """
        human = Human("Ivan", "Petrov", "01.01.1990", "man")
        human.eat()
        self.assertEqual(human.energy, 105)

    def test_sleep(self):
        """
        Test for the 'sleep' method, checking if energy increases by 10.
        """
        human = Human("Ivan", "Petrov", "01.01.1990", "man")
        human.sleep()
        self.assertEqual(human.energy, 110)

    def test_speak(self):
        """
        Test for the 'speak' method, checking if energy decreases by 5.
        """
        human = Human("Ivan", "Petrov", "01.01.1990", "man")
        human.speak()
        self.assertEqual(human.energy, 95)

    def test_walk(self):
        """
        Test for the 'walk' method, checking if energy decreases by 10.
        """
        human = Human("Ivan", "Petrov", "01.01.1990", "man")
        human.walk()
        self.assertEqual(human.energy, 90)

    def test_do_homework(self):
        """
        Test for the 'do_homework' method, checking if energy decreases by 90.
        """
        human = Human("Ivan", "Petrov", "01.01.1990", "man")
        human.do_homework()
        self.assertEqual(human.energy, 10)
