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

class Human():
    def __init__(self, name, surname, birthdate, gender):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.energy = 100

    def eating(self):
        """function ads +5 energy points"""
        self.energy += 5

    def sleeping(self):
        """function ads +10 energy points"""
        self.energy += 10

    def speaking(self):
        """function takes 5 energy points"""
        self.energy -= 5

    def walking(self):
        """function takes 10 energy points"""
        self.energy -= 10

    def homework(self):
        """function takes 90 energy points"""
        self.energy -= 90


Alex = Human("Alex", "Petrenko", "12.03.89", 'male')
Pawlo = Human("Pawlo", "Semenow", "02.11.82", 'male')
Serhii = Human("Serhii", "Rykov", "22.09.98", 'male')
Olena = Human("Olena", "Petrenko", "10.03.99", 'female')
Katya = Human("Olena", "Verzilowa", "22.06.79", 'female')

if __name__ == "__main__":
    Alex.sleeping(), Alex.speaking()
    Pawlo.walking(), Pawlo.eating()
    Serhii.homework()
    Olena.eating(), Olena.sleeping()
    Katya.homework(), Katya.sleeping()
    energy_list = [Alex.energy, Pawlo.energy, Serhii.energy, Olena.energy, Katya.energy]
    print("Max energy after all actions :", max(energy_list))


import unittest

class Test(unittest.TestCase):
    def test_Alex_gender(self):
        """test checks Alex gender"""
        expected_res = 'male'
        actual_res = Alex.gender
        self.assertEqual(actual_res, expected_res)

    def test_Olena_surname(self):
        """test checks Olena surname"""
        expected_res ="Petrenko"
        actual_res = Olena.surname
        self.assertEqual(actual_res, expected_res)

    def test_Katya_birthday(self):
        """test checks Katya birthday"""
        expected_res = "22.06.79"
        actual_res = Katya.birthdate
        self.assertEqual(actual_res, expected_res)

    def test_Pawlo_energy(self):
        """test checks Pawlo energy by default"""
        expected_res = 100
        actual_res = Pawlo.energy
        self.assertEqual(actual_res, expected_res)

    def test_Serhii_name(self):
        """test checks Serhii name"""
        expected_res = "Serhii"
        actual_res = Serhii.name
        self.assertEqual(expected_res, actual_res)

    def test_alex_eating(self):
        """test checks Alex energy after eating"""
        expected_res = 105
        Alex.eating()
        actual_res = Alex.energy
        self.assertEqual(expected_res, actual_res)

    def test_Katya_sleeping(self):
        """test checks Katya energy after sleeping"""
        expected_res = 110
        Katya.sleeping()
        actual_res = Katya.energy
        self.assertEqual(expected_res, actual_res)


    def test_Olena_walking(self):
        """test checks Olena energy after walked"""
        expected_res = 90
        Olena.walking()
        actual_res = Olena.energy
        self.assertEqual(expected_res, actual_res)

    def test_Pawlo_speaking(self):
        """test checks Pawlo energy after speaking"""
        expected_res = 95
        Pawlo.speaking()
        actual_res = Pawlo.energy
        self.assertEqual(expected_res, actual_res)

    def test_Serhii_homework(self):
        """test checks Serhii energy after homework"""
        expected_res = 10
        Serhii.homework()
        actual_res = Serhii.energy
        self.assertEqual(expected_res, actual_res)



