import unittest
from homework_14 import SiteUser

class TestSiteUser(unittest.TestCase):

    def setUp(self):
        self.user1 = SiteUser("John Doe", "john.doe@example.com", "user")
        self.user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")
        self.moderator = SiteUser("Moderator", "moderator@example.com", "moderator")

    def test_name(self):
        self.assertEqual(self.user1.name, "John Doe")

    def test_set_name(self):
        self.user1.name = "John New Doe"
        self.assertEqual(self.user1.name, "John New Doe")

    def test_email(self):
        self.assertEqual(self.user1.email, "john.doe@example.com")

    def test_set_email(self):
        self.user1.email = "john.new.doe@example.com"
        self.assertEqual(self.user1.email, "john.new.doe@example.com")

    def test_permission_lvl(self):
        self.assertEqual(self.user1.permission_lvl, "user")

    def test_set_permission_lvl(self):
        self.user1.permission_lvl = "moderator"
        self.assertEqual(self.user1.permission_lvl, "moderator")

    def test_logcount_increase(self):
        self.user1.logcount_increase()
        self.assertEqual(self.user1.logcount, 1)

    def test_str_representation(self):
        expected_str = ("User: John Doe; "
                        "\nEmail: john.doe@example.com; "
                        "\nPermission level: user; "
                        "\nCount of login for John Doe: 0")
        self.assertEqual(str(self.user1), expected_str)

    def test_equality(self):
        self.assertTrue(self.user1 == self.user1)
        self.assertFalse(self.user1 == self.user2)

    if __name__ == '__main__':
        unittest.main()