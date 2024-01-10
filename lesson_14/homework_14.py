import re
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
    """
    Class to creating site user:
    name (req): str;
    email (req): str;
    access (req): str (admin/moderator/user);
    logcount (optional): int.
    """
    def __init__(self, name, email, access, logcount=0):
        self.name = name.title()
        self.email = email
        self.access = access.lower()
        self.__logcount = logcount

        # Check if correct role of site user to access
        if access.lower() not in ['admin', 'moderator', 'user']:
            raise ValueError("The level of access for user must be 'admin', 'moderator' or 'user'!")

        # Check if email is valid
        if re.fullmatch(r"\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", email):
            self.email = email
        else:
            raise ValueError("Email isn't correct! Please, enter a valid email.")

        # Check if logcount is int
        if not isinstance(logcount, int):
            raise ValueError("Count of login must be int!")

    @property
    def logcount(self):
        return self.__logcount

    @logcount.setter
    def logcount(self, logcount: int):
        """ Use int to set count of login. The count cannot be less than previous value. """
        if not isinstance(logcount, int):
            raise ValueError("Count of login must be int!")
        if logcount > self.__logcount:
            self.__logcount = logcount

    def __eq__(self, other):
        """ This function compares two site users by level of access. """
        if self.access == other.access:
            return "Users have the same access level."
        else:
            return "Users have different access levels."

    def __str__(self):
        """ This function return info about site user. """
        return f"Site User: {self.name},\nEmail: {self.email},\nAccess level: {self.access}"


if __name__ == "__main__":
    user = SiteUser("test name", "test@te.st", 'Admin')
    user.logcount = 5
    user.logcount = 4  # Нічого не змінюється, бо менше вже не може бути
    print(user)
    # Site User: Test Name,
    # Email: test@te.st,
    # Access level: admin
    user2 = SiteUser('user', 'emnao@jh.dwe', 'moderator')
    print(user == user2)  # Users have different access levels.
