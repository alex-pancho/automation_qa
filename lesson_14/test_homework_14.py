import unittest
from homework_14 import SiteUser

class SiteUserTesting(unittest.TestCase):
    """ Testing of attributes and methods of class SiteUser """
    def setUp(self):
        # One SiteUser instance for all tests
        self.user_01 = SiteUser('Nikola', 'nikola_1990@te.st', 'Admin')
        self.user_02 = SiteUser('Alex', 'alex111@test.com', 'admin', 5)
        self.user_03 = SiteUser('Mark', '1999mark@te.st', 'USER')

    # POSITIVE TEST CASES

    def test_p01(self):
        """ Testing of correct display of name """
        expected_res = 'Nikola'
        actual_res = self.user_01.name
        self.assertEqual(expected_res, actual_res, msg="The expected name and actual are different!")

    def test_p02(self):
        """ Testing of correct display of email """
        expected_res = 'nikola_1990@te.st'
        actual_res = self.user_01.email
        self.assertEqual(expected_res, actual_res, msg="The expected email and actual are different!")

    def test_p03(self):
        """ Test of correct display of access level (including lowercase!) """
        expected_res = 'admin'
        actual_res = self.user_01.access
        self.assertEqual(expected_res, actual_res, msg="The expected level of access and actual are different!")

    def test_p04(self):
        """ Testing of correct display of count of logs """
        expected_res = 5
        actual_res = self.user_02.logcount
        self.assertEqual(expected_res, actual_res, msg="The expected logcount and actual are different!")

    def test_p05(self):
        """ Test if user able to change logcount (to bigger side) """
        expected_res = 6
        self.user_02.logcount = 6
        actual_res = self.user_02.logcount
        self.assertEqual(expected_res, actual_res, msg="The expected logcount and actual are different!")

    def test_p06(self):
        """ Test of equal method to compare two levels of access """
        expected_res = "Users have the same access level."
        actual_res = self.user_01 == self.user_02
        self.assertEqual(expected_res, actual_res, msg="The actual compare of users is wrong.")

    def test_p07(self):
        """ Test of equal method to compare two different access levels. """
        expected_res = "Users have different access levels."
        actual_res = self.user_01 == self.user_03
        self.assertEqual(expected_res, actual_res, msg="The actual compare of users is wrong.")

    def test_p08(self):
        """ Test to display correct info about user. """
        expected_res = "Site User: Mark,\nEmail: 1999mark@te.st,\nAccess level: user"
        actual_res = str(self.user_03)
        self.assertEqual(expected_res, actual_res, msg="The actual compare of output info is wrong.")

    # NEGATIVE TEST CASES

    def test_n01(self):
        """ Test if correct role of site user to access """
        expected_res = ValueError
        with self.assertRaises(ValueError):
            actual_result = SiteUser('Alex', 'alex111@test.com', 'CEO')

    def test_n02(self):
        """ Test if valid email of site user """
        invalid_emails = ['test1test.com', 'test1@testcom', 'test.1@testcom', ' test1@test.com',
                          'test-1@test.com', 'test@test.testtttt', 'test@test.test1']
        expected_res = ValueError
        for email in invalid_emails:
            with self.subTest(email=email):
                with self.assertRaises(ValueError):
                    SiteUser('Alex', email, 'moderator')

    def test_n03(self):
        """ Test of count of logs is int """
        expected_res = ValueError
        with self.assertRaises(ValueError):
            actual_result = SiteUser('Alex', 'alex111@test.com', 'user', '5')

    def test_n04(self):
        """ Test of new logcount can't be less than previous value. """
        expected_res = 5
        self.user_02.logcount = 4
        actual_res = self.user_02.logcount
        self.assertEqual(expected_res, actual_res, msg="The expected logcount and actual are different!")

    def tearDown(self):
        # Restore the original state of the object after each test
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)