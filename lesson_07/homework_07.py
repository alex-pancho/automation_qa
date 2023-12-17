# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 0
    # Complete the while loop condition.
    while result <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_numbers(a, b):
    '''Calculating the sum of two numbers'''
    return a + b
print(sum_of_numbers(9, 15))
    


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calc_average(numbers):
    '''Calculating the average'''
    average = sum(numbers)/len(numbers)
    return(average)
list_nambers = [1, 3, 4, 4] 
print(calc_average(list_nambers))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reversed_sentences(sentences:str)-> str:
    '''return reversed sentences'''
    new_sentences = sentences[::-1]
    return(new_sentences)
sent = "Свято наближається!!!"
print(reversed_sentences(sent))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(list_word):
    '''return longest word from list'''
    lon_word = max(list_word, key=len)
    return(lon_word)
list_wor = ["Сніг", "свято", "ялинка", "подарунки", "перемога"]
print(longest_word(list_wor))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    '''returns the index of the first occurrence of the second string in the first line'''
    if str2 in str1:
        result = str1.index(str2)
    else:
        result = -1
    return(result)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# Обчисліть суму елементів двох множин, які не є спільними
def find_sum_of_different_items (set1, set2):
    """calculate the sum of not common elements of a set"""
    sum_of_different_items = sum(set1 ^ set2)
    return(sum_of_different_items)
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
print("сума не спільних множин", find_sum_of_different_items(set_1, set_2))

# task 8
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
def upper_counter (test_text):
    '''finds the number of capitalized words'''
    count = 0
    for i in test_text:
        if i.istitle():
            count = count + 1
    return(count)
teext = "Нове Речення З великими Літерами"
print(upper_counter(teext))

# task 9

"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
def find_square(numbers):
    '''calculates squares for even numbers from the list'''
    square_list = [i**2 for i in numbers if i%2==0]
    return(square_list)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_square(numbers)) 
# task 10
"""Виведіть, скількі разів у тексті зустрічається літера "h"
"""
def number_of_letters(text, i):
    '''counts how many times a certain letter occurs'''
    num_of_letter = text.count(i)
    return(num_of_letter)
text = "By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair"
print(number_of_letters(text, "y"))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""