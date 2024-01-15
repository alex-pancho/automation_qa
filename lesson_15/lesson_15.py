# LEGB
# local

PDV = 20

def somedef():
    a = 1
    print(a)

somedef()


# enclosing
class SomeKind():
    b = 1

    def somedef(self):
        print(self.b)
        print("ПДВ:", PDV)

# global
a = 2

def new_print(a=None):
    # global a
    a = 3
    print(a)
    return a

new_print()
print(a)
# built-in
my_children = SomeKind()
my_children.new_attr = 5
print(my_children.new_attr)
my_children.somedef()

def outer_function():
    y = 20
    def inner_function():
        print(y)
    inner_function()

outer_function()

print(len("Hello"))

# множинне спадкування

class Horse:
    def run(self):
        return "Я біжу!"
    
    def say(self):
        return "Кінь, просто кінь. Дуже приємно, кінь!"
    

class Eagle:
    def fly(self):
        return "I can fly!!"
    
    def say(self):
        return "Юний орел, юний орел що летить від джерел до..."

class Pegasus(Horse, Eagle):
    pass

pinky_pie = Pegasus()
print(pinky_pie.run())
print(pinky_pie.fly())
print(pinky_pie.say())

class Person():
    def __init__(self, name):
        self.name = name.title()
    def say_hello(self):
        print('Hi, I am', self.name)

homo_sap = Person("ALICE")
homo_sap.say_hello()

# class Employee(Person):
#     def __init__(self, name, salary):
#         Person.__init__(self, name)
#         self.salry = salary

#     def say_hello(self):
#         Person.say_hello(self)
#         print("My salary is:", self.salry)

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salry = salary

    def say_hello(self):
        super().say_hello()
        print("My salary is:", self.salry)

worked_man = Employee("mary", 20000)
worked_man.say_hello()

class Animal():
    # someattr = 4
    def __init__(self) -> None:
        self.can_run = False
        self.can_fly = False

class NewHorse(Animal):
    # someattr = 2
    def __init__(self) -> None:
        super().__init__()
        self.can_run = True

class NewEagle(Animal):
    # someattr = 3
    def __init__(self) -> None:
        super().__init__()
        self.can_fly = True

class NewPegasus(NewHorse, NewEagle):
    # someattr = 1
    pass

ranibow_dash = NewPegasus()
print(NewPegasus.mro())
# print(ranibow_dash.someattr)




