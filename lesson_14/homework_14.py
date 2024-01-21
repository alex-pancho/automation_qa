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


class SiteUser():
    def __init__(self, name=str, email=str, access_type=str, log_count=int):
        self.name = name
        self.email = email
        self._access_type = access_type
        self.log_count = log_count

    @property
    def logcount(self):
        """will get user`s logcount"""
        return self.log_count
        # print(f"User logcount is :{self.log_count}")

    @logcount.setter
    def logcount(self, value):
        """will set user`s  new logcount"""
        self.log_count = value

    def __str__(self):
        """will return user info"""
        return f"Користувач: {self.name}, Електронна пошта: {self.email}, Рівень доступу: {self._access_type}"

    def __eq__(self, other):
        if self._access_type == other._access_type:
            return "Користувачі однакові"
        else:
            return "Користувачі різні"


user_1 = SiteUser("Petro", "petro@gmail.com", "user", 12)
user_2: SiteUser = SiteUser("Wlad", "testeeth@yahoo.com", "moderator", 37)
user_3 = SiteUser("Antoine", "troycore@mail.com", "admin", 101)
user_4 = SiteUser("Alena", "alena@gmail.com", "user", 2)

print(user_1)  # will return user_1 info"
print(user_4 == user_2)  # will compare access type between user 4 and user 2

print(user_1.logcount)  # will return logcount of user_1
user_3.logcount = 321  # will set new logcount value
print(user_3.logcount)
