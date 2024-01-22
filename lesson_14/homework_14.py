"""
Створіть class SiteUser() для представлення користувача в системі.
Кожен користувач має ім'я, електронну пошту та рівень доступу (admin, moderator, user).
Також користувач має лічильник кількість логінів - logcount (int)
Реалізуйте необхідні методи та атрибути, використовуючи магічні методи для поліпшення
функціональності.

Вимоги:

    Клас Користувач має мати атрибути: ім'я, електронна_пошта, рівень_доступу, кількість логінів (logcount).
    Реалізуйте методи для отримання та встановлення значень атрибутів (гетери та сетери).
    Перевизначте метод __str__, щоб при виведенні об'єкта на екран 
    виводилася інформація про користувача.
    Реалізуйте метод __eq__, який дозволяє порівнювати два об'єкта за рівнем доступу.
    Реалізуйте щоб SiteUser.logcount можна було збільшувати

Приклад використання:

user1 = Користувач("John Doe", "john.doe@example.com", "user")
user2 = Користувач("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Виведе: Користувач: John Doe, Електронна пошта: john.doe@example.com, Рівень доступу: user

# Порівняння користувачів
if user1 == user2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")

Написати на це все тести
"""

class SiteUser:
    def __init__ (self, name, mail, access_level) -> None:
        self.name = name
        self.mail = mail 
        self.__logcount = 0 
        self.access_level = access_level
        #if access_level in ["user", "moderator", "admin"]:
        #    self.access_level = access_level
        #else:
        #    raise ValueError ("Invalid value")

    def __str__(self) -> str:
        return f"Користувач: {self.name}, Електронна пошта: {self.mail}, Рівень доступу: {self.access_level} "
    
    @property
    def logcount(self):
        return self.__logcount
    
    @logcount.setter
    def logcount(self, logcount):
        if logcount > self.__logcount:
            self.__logcount += logcount 

    def __eq__(self, other) -> bool:
        if isinstance(other, SiteUser):
            return self.access_level == other.access_level
        return
        
if __name__ == "__main__":       
    user1 = SiteUser("Petro", "test@gmail,com", "amin")
    user2 = SiteUser("Anna", "tet@gmail,com", "admin")
    user3 = SiteUser("Alla", "tt@gmail,com", "user")

    user1.logcount = 4

    if user1 == user2:
        print("Користувачі однакові")
    else:
        print("Користувачі різні")
    print(user1 == user2)
    print(user1.logcount)
    print(user1)





