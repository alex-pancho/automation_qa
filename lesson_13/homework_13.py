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
    def __init__(self, name, lastName, birthdayDate, gender) -> None:
        self.name = name
        self.lastName = lastName
        self.birthdayDate = birthdayDate
        self.gender = gender
        self.energy = 100

    def eat(self):
        self.energy += 5
    
    def sleep(self):
        self.energy += 10

    def speak(self):
        self.energy -= 5

    def go(self):
        self.energy -= 10

    def doHomework(self):
        self.energy -= 90

    def __repr__(self) -> str:
        return f"Енергія: {self.energy}, Ім'Я: {self.name}"
    
if __name__ == "__main__":
    man_fitst = Human("Peter", "Ivchenko", "10.12.1999", "male")
    man_second = Human("Ivan", "Sobko", "10.12.2008", "male")
    man_third = Human("Alex", "Deverenko", "10.11.2001", "male")
    woman_first = Human("Ivanna", "Bogdach", "17.12.2000", "female")
    woman_second = Human("Vasilina", "Krut", "17.08.1994", "female")

    man_fitst.eat()
    man_second.sleep()
    man_second.go()
    man_fitst.sleep()
    woman_first.speak()
    woman_first.doHomework()
    man_third.go()
    woman_second.eat()
    man_third.speak()
    woman_second.doHomework()

    people = [man_fitst, man_second, man_third, woman_first, woman_second]
   
    
    
    max_energy = max(people, key=lambda x: x.energy)
    

    print(max_energy)



