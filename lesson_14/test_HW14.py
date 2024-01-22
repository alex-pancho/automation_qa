import unittest
from homework_14 import SiteUser

class PositiveTests(unittest.TestCase):
    
    def test_logcount(self):
        """testing adding of user logcount"""
        user1 = SiteUser("Petro", "test@gmail,com", "admin")
        user1.logcount = 5
        act_result = 5
        exp_result = user1.logcount
        self.assertEqual(act_result, exp_result, msg=f"testing adding of user logcount is failed {act_result} = {exp_result}")
    

    def test_users_by_access(self):
        """user comparison testing by access level""" 
        user1 = SiteUser("Petro", "test@gmail,com", "admin")
        user2 = SiteUser("Panda", "trdt@gmail,com", "admin")
        self.assertTrue(user1==user2, msg=f"user comparison testing by access level is failed {user1.access_level} = {user2.access_level}")

    def test_access(self):
        """access level testing for validity"""
        user1 = SiteUser("Petro", "test@gmail,com", "admin")
        exp_result = "admin" or "user" or "moderator"
        act_result = user1.access_level
        self.assertEqual(exp_result, act_result, msg=f"invalid access level {exp_result} = {act_result}") 

   



if __name__ == "__main__":
    unittest.main(verbosity=2)