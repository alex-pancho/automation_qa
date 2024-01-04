import unittest
import sys
import pathlib
from homework_13 import Human, EnergyError

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

class HumanAttributesTesting(unittest.TestCase):
    """
    Testing of atributes of class Human.
    """
    def test_positive_01(self):
        """ Testing of correct display of first name """
        man_1 = Human('John', 'Packer', '12.09.1989', 'male')
        expected_res = 'John'
        actual_res = man_1.f_name
        self.assertEqual(expected_res, actual_res, msg=f"The fisrt name isn't match!")

    def test_positive_02(self):
        """ Testing of correct display of second name """
        man_1 = Human('John', 'Packer', '12.09.1989', 'male')
        expected_res = 'Packer'
        actual_res = man_1.s_name
        self.assertEqual(expected_res, actual_res, msg=f"The second name isn't match!")

    def test_positive_03(self):
        """ Testing of correct display of date of birth """
        man_1 = Human('John', 'Packer', '12.09.1989', 'male')
        expected_res = '12.09.1989'
        actual_res = man_1.dob
        self.assertEqual(expected_res, actual_res, msg=f"The date of birth isn't match!")

    def test_positive_04(self):
        """ Testing of correct display of sex """
        man_1 = Human('John', 'Packer', '12.09.1989', 'male')
        expected_res = 'male'
        actual_res = man_1.sex
        self.assertEqual(expected_res, actual_res, msg=f"The sex of person isn't match!")

    def test_negative_01(self):
        """ Test using uncorrected data: list instead of str """
        expected_res = TypeError
        with self.assertRaises(TypeError):
            result = Human(['John'], 'Packer', '12.09.1989', 'male')

    def test_negative_02(self):
        """ Test with incorrect value for 'sex' attribute """
        expected_res = ValueError
        with self.assertRaises(ValueError):
            result = Human('John', 'Packer', '12.09.1989', 'test')


class HumanMethodsTesting(unittest.TestCase):
    """
    Testing og methods of class Human.
    """
    def test_action_positive_01(self):
        """ Testing level of energy after eating (eating func) """
        person = Human('John', 'Packer', '12.09.1989')
        person.eating()
        expected_res = 105
        actual_res = person.energy
        self.assertEqual(expected_res, actual_res, msg="Enegry of person is not match after eating.")

    def test_action_positive_02(self):
        """ Testing level of energy after sleaping (sleaping func) """
        person = Human('John', 'Packer', '12.09.1989')
        person.sleaping()
        expected_res = 110
        actual_res = person.energy
        self.assertEqual(expected_res, actual_res, msg="Enegry of person is not match after sleaping.")

    def test_action_positive_03(self):
        """ Testing level of energy after walking (walking func) """
        person = Human('John', 'Packer', '12.09.1989')
        person.walking()
        expected_res = 90
        actual_res = person.energy
        self.assertEqual(expected_res, actual_res, msg="Enegry of person is not match after walking.")

    def test_action_positive_04(self):
        """ Testing level of energy after speaking (speaking func) """
        person = Human('John', 'Packer', '12.09.1989')
        person.speaking()
        expected_res = 95
        actual_res = person.energy
        self.assertEqual(expected_res, actual_res, msg="Enegry of person is not match after speaking.")

    def test_action_positive_05(self):
        """ Testing level of energy after doing homework (doing_hw func) """
        person = Human('John', 'Packer', '12.09.1989')
        person.doing_hw()
        expected_res = 10
        actual_res = person.energy
        self.assertEqual(expected_res, actual_res, msg="Enegry of person is not match after doing hw.")

    def test_action_positive_06(self):
        """ Testing level of energy after called multiply functions (actions) """
        person = Human('John', 'Packer', '12.09.1989')
        person.speaking()
        person.walking()
        person.eating()
        person.sleaping()
        expected_res = 100
        actual_res = person.energy
        self.assertEqual(expected_res, actual_res, msg="Enegry of person is not match after doing multiple activities.")

    def test_action_negative_01(self):
        """ Test to call EnegryError (when energy <=0) """
        person = Human('John', 'Packer', '12.09.1989')
        person.doing_hw()
        person.walking()

        expected_res = EnergyError
        with self.assertRaises(EnergyError):
            result = person.check_energy()


if __name__ == '__main__':
    unittest.main(verbosity=2)
