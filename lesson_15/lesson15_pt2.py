from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    @abstractmethod
    def calc_area(self):
        pass

    @abstractmethod
    def calc_perimetr(self):
        pass

class Square(GeometricFigure):
    def __init__(self, border) -> None:
        self.border = border

    def calc_area(self):
        return self.border ** 2

    def calc_perimetr(self):
        return self.border * 4

    def fortune():
        return "Yor luck is here!!!"

class TestPattern(ABC):
    @abstractmethod
    def setUp(self):
        """Setup for test"""
        pass

    @abstractmethod
    def test_main(self):
        """Execute test here"""
        pass

    @abstractmethod
    def tearDown(self):
        """End of test"""
        pass

class MyNewTest(TestPattern):
    pass # its raise Error  !!!!



if __name__ == "__main__":
    new_square = Square(5)
    print(new_square.calc_area())
    print(new_square.calc_perimetr())
