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
import unittest

class SiteUser:
    def __init__(self, name, email, access_level = "user"):
        """
        Constructor method to initialize user attributes
        """
        valid_access_levels = ["admin", "moderator", "user"]

        self.name = name
        self.email = email
        self.access_level = access_level
        self.logcount = 0

    def __str__(self):
        """
        String representation of the user for easy printing
        """
        return f"The user {self.name}, Email: {self.email}, Access lvl: {self.access_level}"

    def __eq__(self, other):
        """
        Equality comparison based on access levels
        """
        return self.access_level == other.access_level
    def increment_logcount(self):
        """
        Method to increment the log count for the user
        """
        self.logcount += 1

class TestSiteUser(unittest.TestCase):

    user1 = SiteUser("John Doe", "john.doe@example.com", "user")
    user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
    user3 = SiteUser("Bob Johnson", "bob.johnson@example.com")

    def test_string_representation_method(self):
        expected_output = "The user John Doe, Email: john.doe@example.com, Access lvl: user"
        self.assertEqual(str(self.user1), expected_output)

    def test_eq_method_user_equal_to_itself(self):
        self.assertTrue(self.user1 == self.user1)

    def test_eq_method_users_with_different_access_levels(self):
        self.assertFalse(self.user1 == self.user2)

    def test_eq_method_users_with_same_access_levels(self):
        user1_copy = SiteUser("John Doe", "john.doe@example.com", "user")
        self.assertTrue(self.user1 == user1_copy)

    def test_eq_method_users_with_default_access_level(self):
        self.assertTrue(self.user1 == self.user3)

    def test_increment_logcount_method(self):
        self.assertEqual(self.user1.logcount, 0)
        self.user1.increment_logcount()
        self.assertEqual(self.user1.logcount, 1)
        self.user1.increment_logcount()
        self.assertEqual(self.user1.logcount, 2)

if __name__ == '__main__':
    unittest.main()

