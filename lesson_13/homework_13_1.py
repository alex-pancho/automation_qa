class Human:
    def __init__(self, name, surname, DOB, gender):
        self.name = name
        self.surname = surname
        self.DOB = DOB
        self.gender = gender
        self.energy = 100

    def eat(self):
        self.energy += 5

    def sleep(self):
        self.energy += 10

    def talk(self):
        self.energy -= 5

    def walk(self):
        self.energy -= 10

    def homework(self):
        self.energy -= 90

if __name__ == "__main__":
    human1 = Human("Oleg", "Petrov", "01.01.1990", "male")
    human2 = Human("Maria", "Ivanova", "15.05.1985", "female")
    human3 = Human("Olexandr", "Sidorov", "20.09.2000", "male")
    human4 = Human("Olga", "Kovalenko", "10.11.1995", "female")
    human5 = Human("Petro", "Melnyk", "05.03.1988", "male")

    human1.eat()
    human2.sleep()
    human3.talk()
    human4.walk()
    human5.homework()

    list_human = [human1, human2, human3, human4, human5]

    # Знаходимо людину з найбільшою енергією
    biggest_energy = max(list_human, key=lambda human: human.energy)

    # Виводимо результат
    print(f"У {biggest_energy.name} {biggest_energy.surname} залишилося найбільше енергії: {biggest_energy.energy}")
