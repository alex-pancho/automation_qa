def log_factorial_calls(func):
    def wrapper(n):
        print(f"Calling {func.__name__}({n})")
        res = func(n)
        print(f"Result: {res}")
        return res

    return wrapper


@log_factorial_calls
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def factorial_generator(n):
    for i in range(n + 1):
        yield factorial(i)


if __name__ == "__main__":
    for result in factorial_generator(5):
        pass

    # Calling factorial(0)
    # Result: 1
    # Calling factorial(1)
    # Result: 1
    # Calling factorial(2)
    # Result: 2
    # Calling factorial(3)
    # Result: 6
    # Calling factorial(4)
    # Result: 24
    # Calling factorial(5)
    # Result: 120
