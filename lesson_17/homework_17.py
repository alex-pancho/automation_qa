def log_factorial_calls(func):
    def wrapper(n):
        print(f"Calling {func.__name__}({n})")
        result = func(n)
        print(f"Result: {result}")
        return result
    return wrapper
@log_factorial_calls
def factorial(n):
    """
    Calculates the factorial of the number n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_generator(n):
    """
    Generates a sequence of factorials from 0 to n (inclusive)
    """
    for i in range(n + 1):
        yield factorial(i)

if __name__ == "__main__":
    n = 5
    factorial_sequence = list(factorial_generator(n))
    print(factorial_sequence)
