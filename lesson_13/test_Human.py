import unittest
from homework_13 import Human 
 
class PositiveTests(unittest.TestCase):
    def test_eat (self):
        """testing energy changes if a person has eaten"""
        man = Human("Peter", "Ivchenko", "11.12.1999", "male")
        man.eat()
        axpR = 105
        actR = man.energy
        self.assertEqual(axpR, actR, msg=f"energy changes if a person has eaten is failed {axpR}={actR}" )

    def test_sleep(self):
        """testing energy changes if a person slept"""
        man = Human("Peter", "Ivchenko", "11.12.1999", "male")
        man.sleep()
        axpR = 110
        actR = man.energy
        self.assertEqual(axpR, actR, msg=f"energy changes if a person slept is failed {axpR}={actR}" )

    def test_doHomework (self):
        """testing energy changes if a person did homework"""
        man = Human("Peter", "Ivchenko", "11.12.1999", "male")
        man.doHomework()
        axpR = 10
        actR = man.energy
        self.assertEqual(axpR, actR, msg=f"energy changes if a person did homework is failed {axpR}={actR}" )

    def test_go (self):
        """testing energy changes if a person go"""
        man = Human("Peter", "Ivchenko", "11.12.1999", "male")
        man.go()
        axpR = 90
        actR = man.energy
        self.assertEqual(axpR, actR, msg=f"energy changes if a person go is failed {axpR}={actR}" )

    def test_speak (self):
        """testing energy changes if a person spoken"""
        man = Human("Peter", "Ivchenko", "11.12.1999", "male")
        man.speak()
        axpR = 95
        actR = man.energy
        self.assertEqual(axpR, actR, msg=f"energy changes if a person spoken is failed {axpR}={actR}" )






    
if __name__ == '__main__':
    unittest.main(verbosity=2)