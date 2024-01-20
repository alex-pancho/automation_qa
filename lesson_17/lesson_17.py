# __iter__() i __next__()
# iter() next()
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Використання ітератора
my_iter = MyIterator(5)

# for num in my_iter:
#     print(num)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

print(list(my_iter))
# print(next(my_iter)) # StopIteration

my_list = ["a", "c", "c", "a"]
for i in my_list:
    print(i)


def my_for(iterable, callback_func):
    iterator = iter(iterable)
    while True:
        try:
            value = next(iterator)
            callback_func(value)
        except StopIteration:
            break

my_for('bye', print)

def mul(item):
    print(item * 10)

my_for('goodday', mul)

# generators

def simple_generator():
    yield 1
    yield 2
    yield 3

# Використання генератора
gen = simple_generator()
print("print:", next(gen))
for value in gen:
    print(value)

my_billion = range(1000000)
my_list = [0, 1, 2, ("..."), 1000000]

gen_expr = (x ** 200 for x in range(5))
print(gen_expr)
for n in gen_expr:
    print(n)

def exponent(x):
    return x ** 2.1415

my_nums = [1, 2, 4, 6]

ex_numbers = map(exponent, my_nums)

#print(next(ex_numbers))
for e in ex_numbers:
    print(e)


def check_input(user_input):
    if not isinstance(user_input, (int, float)):
        raise TypeError(f"Wrong type: {user_input} not int")

def a_plus_b(a:int, b:int, c=1, d=2, e=3) -> int:
    list(map(check_input, [a, b, c, d, e]))
    return (a + b) * (2 * a - b) + c - (d / e)

print("a+b1 =", a_plus_b(1,2))
#print("a+b2 =", a_plus_b(1,2,3,4,"5"))
print("a+b3 =", a_plus_b(1,2,3,4,5))

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped_data = zip(names, ages)
print(zipped_data)
# print(next(zipped_data))
# print(dict(zipped_data))
for key, value in zipped_data:
    print(f"{key} is {value} years old.")

# decorators
def my_decor(func):
    def wrapper(*args, **kwargs):
        print("Wow, great like for today")
        func(*args, **kwargs)
        print("after func")
    return wrapper

@my_decor
def say_int(my_int):
    print(my_int * 2)

say_int(4)

girl_list = ["aska", "miranda", "skype"]

@my_decor
def like_me(girl_list):
    print("like you:", *girl_list)
# my_decor(say_int(4))
like_me(girl_list)
