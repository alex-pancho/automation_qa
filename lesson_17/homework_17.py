def log_factorial_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} {args[0]}")
        result = func(*args, **kwargs)
        print(f"Result {result}")

    return wrapper


@log_factorial_calls
def factorial(n):
    """Обчислює факторіал числа n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        yield factorial(i)



if __name__ == "__main__":
    for i in factorial_generator(5):
        pass

