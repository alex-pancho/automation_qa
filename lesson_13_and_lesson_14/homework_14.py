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
    def __init__(self, name, email, access_level):
        self._name = name
        self._email = email
        self._access_level = access_level
        self._logcount = 0

    
    def name(self):
        return self._name

    
    def name(self, value):
        self._name = value

    
    def email(self):
        return self._email

    
    def email(self, value):
        self._email = value

    
    def access_level(self):
        return self._access_level

    
    def access_level(self, value):
        self._access_level = value

    
    def logcount(self):
        return self._logcount

    def increment_logcount(self):
        self._logcount += 1

    def __str__(self):
        return f"Користувач: {self._name}, Електронна пошта: {self._email}, Рівень доступу: {self._access_level}"





if __name__ == "__main__":
    user1 = SiteUser("John Doe", "john.doe@example.com", "user")
    user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")

    print(user1)
    
    if user1 == user2:
        print("Користувачі однакові")
    else:
        print("Користувачі різні")

    user1.increment_logcount()
    print(user1.logcount)  

