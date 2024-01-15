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
    PERMISSION_LEVELS = {"user", "moderator", "admin"}

    def __init__(self, name, email, permission_lvl="user"):
        self._name = name
        self._email = email
        self.permission_lvl = permission_lvl
        self._logcount = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def permission_lvl(self):
        return self._permission_lvl

    @permission_lvl.setter
    def permission_lvl(self, value):
        self._permission_lvl = self._check_permission(value)

    @property
    def logcount(self):
        return self._logcount

    def logcount_increase(self):
        self._logcount += 1

    def _check_permission(self, value):
        if value in self.PERMISSION_LEVELS:
            return value
        else:
            ValueError("Invalid permission level!")

    def __str__(self):
        return (f"User: {self._name}; "
                f"\nEmail: {self._email}; "
                f"\nPermission level: {self._permission_lvl}; "
                f"\nCount of login for {self._name}: {self._logcount}")

    def __eq__(self, check_lvl_permission):
        return self._permission_lvl == check_lvl_permission.permission_lvl

if __name__ == "__main__":

    user1 = SiteUser("John", "john13@tst.tst", "user")
    user2 = SiteUser("Jack", "jac@tst.tst", "user")
    moder = SiteUser("Billy", "bil777@tst.tst","moderator")
    admin = SiteUser("Admin", "admin@tst.tst", "admin")
    print(user1)

    admin.logcount_increase()
    print(admin)

    if user1 == admin:
        print("Users has the same permission level")
    else:
        print("Users has different permission level!")
