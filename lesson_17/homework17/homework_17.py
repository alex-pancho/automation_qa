def log_factorial_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called with parameters: {args} and result: {result}")
        return result
    return wrapper

@log_factorial_calls
def factorial(n):
    """Обчислює факторіал числа n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_generator(n):
    for i in range(n + 1):
        yield factorial(i)

# Використовуємо генератор для обчислення факторіалів для числа 5
for result in factorial_generator(5):
    pass  # Просто проходимо по всіх значеннях генератора, щоб викликати функцію та вивести лог
