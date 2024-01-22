import unittest
import hometask_14


class TestSiteUser(unittest.TestCase):
    def setUp(self):
        self.user1 = hometask_14.SiteUser("Oleg Petrov", "oleg.petrov@test.com", "user")
        self.user2 = hometask_14.SiteUser("Ira Bila", "ira.bila@test.com", "admin")
        self.user3 = hometask_14.SiteUser("Inna Tyma", "inna.tyma@test.com", "moderator")

    def test_attributes(self):
        self.assertEqual(self.user1.name, "Oleg Petrov")
        self.assertEqual(self.user1.email, "oleg.petrov@test.com")
        self.assertEqual(self.user1.access_level, "user")
        self.assertEqual(self.user1.logcount, 0)

    def test_setters(self):
        self.user1.name = "New Name"
        self.assertEqual(self.user1.name, "New Name")

        self.user1.email = "new.email@test.com"
        self.assertEqual(self.user1.email, "new.email@test.com")

        self.user1.access_level = "moderator"
        self.assertEqual(self.user1.access_level, "moderator")

    def test_increase_logcount(self):
        self.user1.increase_logcount()
        self.assertEqual(self.user1.logcount, 1)

    def test_str_representation(self):
        expected_str = "User: Oleg Petrov, Email: oleg.petrov@test.com, Access Level: user, Log Count: 0"
        self.assertEqual(str(self.user1), expected_str)

    def test_eq_method(self):
        self.assertTrue(self.user1 == self.user1)
        self.assertFalse(self.user1 == self.user2)

    def test_invalid_access_level(self):
        with self.assertRaises(hometask_14.AccessLevelException):
            self.user1.access_level = "invalid_level"

    def test_invalid_eq_comparison(self):
        with self.assertRaises(AttributeError):
            _ = self.user1 == 42


if __name__ == '__main__':
    unittest.main()
