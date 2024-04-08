

class MyFirstClass:
    age = 43
    def __init__(self, name) -> None:
        self.name = name

alex = MyFirstClass('Alex')
katya = MyFirstClass('Katya')

print(alex.age, katya.age)
print(alex.name, katya.name)


class Car:
    def __init__(self, label, model, year) -> None:
        self.label = label
        self.model = model
        self.year = year


my_car = Car("Toyota", "Camry", 2022)

print(f"Марка: {my_car.label}")
print(f"Модель: {my_car.model}")
print(f"Рік: {my_car.year}")

class Bank:
    bank = "UtorBANK"
    @classmethod
    def change_name(cls, new_name):
        cls.bank = new_name


class Operation(Bank):
    def __init__(self) -> None:
        self.balance = 0

    @staticmethod
    def plus(a, b):
        return a + b

    def add(self, sum):
        """Add money to acc"""
        self.balance = self.plus(sum, self.balance)

    def withdraw(self, sum):
        self.balance -= sum


class Account(Operation):
    def __init__(self, name:str, balance:float) -> None:
        self.name = name
        self.balance = balance

    def __repr__(self) -> str:
        return f"Валюта: {self.name}, Баланс: {self.balance}"


grn_acc = Account("grn", 1000)

print(grn_acc.name, grn_acc.balance, grn_acc.bank)
grn_acc.add(1)
print(grn_acc.balance)
print(grn_acc)

usd_acc = Account("usd", 10000)

usd_acc.add(100000000000000000)
usd_acc.withdraw(100)
print(usd_acc)


class BlockedAccount(Operation):

    def __init__(self, account) -> None:
        self.balance = account.balance
        self.name = account.name

    def add(self, sum):
        """Add money to acc"""
        print("Account locked")

    def withdraw(self, sum):
        print("Account locked")

    def __repr__(self) -> str:
        return f"Валюта: {self.name}, Баланс: {self.balance}"

block_usd_acc = BlockedAccount(usd_acc)
print(block_usd_acc)
block_usd_acc.add(100)
block_usd_acc.withdraw(100)

block_usd_acc.change_name("PrivatBamk")
print(block_usd_acc.bank)
usd_acc.change_name("Aval")
print(usd_acc.bank)
print(grn_acc.bank)
print(Operation.plus(1, 3))