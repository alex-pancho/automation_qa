import unittest
from homeworks import add_numbers

class TestAddNumbers(unittest.TestCase):
        
    def test_add_number5(self):
        """Test number 5"""
        result = add_numbers(2, 3)
        self.assertEqual(result, 5,msg=f"Additional operation FAIL")

    def test_add_number6(self):
        
        result = add_numbers(3, 3)
        self.assertEqual(result, 6,msg=f"Additional operation FAIL")

    def test_add_number7(self):
        
        result = add_numbers(0, 0)
        self.assertEqual(result, 0,msg=f"Additional operation FAIL")

    def test_add_number8(self):
        
        result = add_numbers(8, 8)
        self.assertEqual(result, 16,msg=f"Additional operation FAIL")

    def test_add_number9(self):
        
        result = add_numbers(5, 7)
        self.assertEqual(result, 12,msg="Operation FAIL")
if __name__ == '__main__':
    unittest.main(verbosity=5)



    