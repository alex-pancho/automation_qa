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


class Human:
    def __init__(self, name, second_name, birthday, gender):
        self.name = name
        self.second_name = second_name
        self.birthday = birthday
        self.gender = gender
        self.energy = 100

    def eat(self):
        self.energy += 5
        if self.energy <= 0:
            print(f"{self.name} {self.second_name} has no energy")
            self.energy = 0
    def sleep(self):
        self.energy += 10
        if self.energy <= 0:
            print(f"{self.name} {self.second_name} has no energy")
            self.energy = 0

    def speak(self):
        self.energy -= 5
        if self.energy <= 0:
            print(f"{self.name} {self.second_name} has no energy")
            self.energy = 0

    def walk(self):
        self.energy -= 10
        if self.energy <= 0:
            print(f"{self.name} {self.second_name} has no energy")
            self.energy = 0

    def make_hm(self):
        self.energy -= 90
        if self.energy <= 0:
            print(f"{self.name} {self.second_name} has no energy")
            self.energy = 0


person1 = Human("John", "Johnny", "11/11/1990", "male")
person2 = Human("Tony", "Tonny", "12/01/1988", "male")
person3 = Human("Cuper", "Johns", "12/10/1991", "male")
person4 = Human("Ana", "Dee", "02/04/2003", "female")
person5 = Human("Lola", "Smith", "21/12/2010", "female")

person1.eat()
person1.make_hm()

person2.speak()
person2.walk()

person3.sleep()
person3.eat()

person4.make_hm()
person4.walk()

person5.walk()
person5.eat()

persons = [person1, person2, person3, person4, person5]
max_energy_person = persons[0]
for p in persons:
    if p.energy > max_energy_person.energy:
        max_energy_person = p

print(f"{max_energy_person.name} {max_energy_person.second_name} has more energy than others.")