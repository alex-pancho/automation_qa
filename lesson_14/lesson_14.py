# Базис ООП
# успадкування
# інкапсуляція
# поліморфізм
# абстракція

# Життєвий цикл екземпляра класа
# __new__(cls, [...])
# __init__(self, [...])
# __del__(self)
# Інкапсуляція
class Person():

    def __init__(self, age:int) -> None:
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age:int):
        if not isinstance(age, (int, float)):
            raise ValueError("Age must be int")
        if age > self.__age:
            self.__age = age


p = Person(35)
print(p.age)
p.age = 34
print("34<35 !=", p.age)
p.age = 36
print(p.age)
# p.age = "aaa"
# print(p.age)
# Приховування атрибутів
# Сетери, гетери і делетери
# Корисні магічні методи
# __getitem__()
class MyList():
    def __init__(self) -> None:
        self.items = []

    # @property
    # def add(self):
    #     return self.items

    # @add.setter
    def add(self, item):
        self.items.append(item)

    def __getitem__(self, index):
        return self.items[index]

my_new_list = MyList()
# my_new_list.add = "a"  # if use property
my_new_list.add("b")
my_new_list.add("a")
print(my_new_list[1])
# __call__()

class Multiplicator():
    """Простий клас для виконання математичних операцій."""

    def __init__(self, value:int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)

    def __call__(self, b):
        """Приймає лише інт бо я так хочу і всьо!!"""
        if not isinstance(b, int):
            raise ValueError(self.__call__.__doc__)
        self.value = self.value * b
        return self.value

multi = Multiplicator(5)
print(multi(2))
# __doc__
## print(multi("asd"))

# Емуляція числових типів

class Money():

    def __init__(self, amount: float) -> None:
        self.amount = amount

    def __str__(self):
        return f"{self.amount:.2f} item(s)"

    def __add__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.amount + other.amount)
        elif isinstance (other, (int, float)):
            return type(self)(self.amount + other)
        else:
            raise ValueError("Неправильний тип для операції додавання")

    def __sub__(self, other):
        if isinstance(other, Money) and type(self) == type(other):
            return type(self)(self.amount - other.amount)
        elif isinstance (other, (int, float)):
            return type(self)(self.amount - other)
        else:
            raise ValueError("Неправильний тип для операції віднімання")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return type(self)(self.amount * scalar)
        else:
            raise ValueError("Неправильний тип для операції множення")

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)) and scalar != 0:
            return type(self)(self.amount / scalar)
        else:
            raise ValueError("Неправильний тип або ділення на нуль")



class UAH(Money):
    def __init__(self, amount: float) -> None:
        super().__init__(amount)

    def __str__(self):
        return f"{self.amount:.2f} грн"


class USD(Money):
    def __init__(self, amount: float) -> None:
        super().__init__(amount)

    def __str__(self):
        return f"${self.amount:.2f}"

class ForEx():
    def __init__(self, exchange_rate_by, exchange_rate_sell):
        self.exchange_rate_by = exchange_rate_by
        self.exchange_rate_sell = exchange_rate_sell

    def convert_to_usd(self, uah_amount):
        if isinstance(uah_amount, UAH):
            usd_amount = uah_amount.amount / self.exchange_rate_sell
            return USD(usd_amount)
        else:
            raise ValueError("Неправильний тип для конвертації")

    def convert_to_uah(self, usd_amount):
        if isinstance(usd_amount, USD):
            uah_amount = usd_amount.amount * self.exchange_rate_by
            return UAH(uah_amount)
        else:
            raise ValueError("Неправильний тип для конвертації")

if __name__ == "__main__":

    my_uah_cash = UAH(3456)
    my_wife_uah_cash = UAH(30456)
    my_usd_cash = USD(100)
    print(my_uah_cash)
    print(my_usd_cash)
    my_total_cash = my_uah_cash + my_wife_uah_cash
    print(my_total_cash)

    privatbank = ForEx(37.05, 37.57)
    pb_to_uah = privatbank.convert_to_uah(my_usd_cash)
    pb_to_usd = privatbank.convert_to_usd(my_uah_cash)

    akordbank = ForEx(37.37, 38.00)
    ak_to_uah = akordbank.convert_to_uah(my_usd_cash)
    ak_to_usd = akordbank.convert_to_usd(my_uah_cash)

    print(f"Продати {my_usd_cash}:", pb_to_uah, "|", ak_to_uah)
    print(f"Купити на {my_uah_cash}:", pb_to_usd, "|", ak_to_usd)

    print(my_uah_cash + 345)
    """
    object.__add__(self, other)
    object.__sub__(self, other)
    object.__mul__(self, other)
    object.__matmul__(self, other)
    object.__truediv__(self, other)
    object.__floordiv__(self, other)
    object.__mod__(self, other)
    object.__divmod__(self, other)
    object.__pow__(self, other[, modulo])
    object.__lshift__(self, other)
    object.__rshift__(self, other)
    object.__and__(self, other)
    object.__xor__(self, other)
    object.__or__(self, other)
    """
