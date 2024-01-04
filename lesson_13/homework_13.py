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


class EnergyError(Exception):
    """ Class for assert Energy error """
    def __init__(self, *args, **kwargs):
        pass


class Human:
    """
    This class for creating a person with some qualities.
    Expected str:
    f_name: first name;
    s_name: second name;
    dob: date of birth;
    sex = sex (male/female) default = other;
    energy = default 100 (can change after using functions).
    """
    def __init__(self, f_name, s_name, dob, sex='other'):
        self.f_name = f_name
        self.s_name = s_name
        self.dob = dob
        self.sex = sex
        self.energy = 100

        if not all(isinstance(arg, str) for arg in (f_name, s_name, dob, sex)):
            raise TypeError("The type of each param must be string!")

        if sex.lower() not in ['male', 'female', 'other']:
            raise ValueError("Sex must be 'male' or 'female'")

    def check_energy(self):
        if self.energy <= 0:
            raise EnergyError(f"The person {self.f_name} {self.s_name} should sleep or eat to reenergize! "
                              f"Level of energy is {self.energy}")

    def eating(self):
        self.energy += 5

    def sleaping(self):
        self.energy += 10

    def speaking(self):
        self.energy -= 5

    def walking(self):
        self.energy -= 10

    def doing_hw(self):
        self.energy -= 90


man_1 = Human('John', 'Packer', '12.09.1989', 'male')
man_2 = Human('Peter', 'Nilson', '29.05.1992', 'male')
man_3 = Human('Albert', 'Trold', '15.12.1999', 'male')
woman_1 = Human('Dalores', 'Naker', '06.06.2000')
woman_2 = Human('Nikola', 'Smith', '01.07.1981', 'female')

man_1.eating()
man_1.doing_hw()

man_2.walking()
man_2.speaking()

man_3.doing_hw()
man_3.eating()
man_3.sleaping()

woman_1.speaking()
woman_1.walking()
woman_1.speaking()

woman_2.doing_hw()
woman_2.walking()
woman_2.sleaping()

people = [man_1, man_2, man_3, woman_1, woman_2]

most_energetic_person = max(people, key=lambda person: person.energy)
print(f"The most energetic person is {most_energetic_person.f_name} {most_energetic_person.s_name} "
      f"with {most_energetic_person.energy} energy!")
# The most energetic person is Peter Nilson with 85 energy!