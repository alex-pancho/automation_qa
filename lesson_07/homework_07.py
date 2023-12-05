# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
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
def addit(a:int, b:int) -> int:
    #Add two variables
    addit_result = a + b

    return addit_result


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def list_avg(nums_of_list:int) -> int:
    #Calculate sum of all numbers
    total_sum = sum(nums_of_list)
    #Calculate average of numbers
    avg = total_sum/len(nums_of_list)

    return avg

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def revers_string(strg:str) -> str:
    #Make type reversed
    str_r = reversed(strg)
    #Return to string
    reversed_str = ''.join(str_r)

    return reversed_str

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def long_word(words:str) -> str:
    #Create empty variable type str
    longest_word = ""
    #Loop for found the longest word
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1:str, str2:str) -> int:
    #Returns index of the first match
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def uniq_elements(list_elements:list) -> set:
    #Return unique elements
    return set(list_elements)
big_list = [3, 1, 4, 5, 2, 5, 3]
print(uniq_elements(big_list))
# task 8
def revers_keys_value(key_value:dict) -> dict:
    #Create empty dict
    revers_new_dict = {}
    #Change key to value
    for v, k in key_value.items():
        revers_new_dict[k] = v

    return revers_new_dict

# task 9
def add_sets(set1:set, set2:set) -> set:
    #Add unique sets element in sets_unique
    sets_unique = set1 ^ set2

    #Retorns sum of all elements in sets_unique
    return sum(sets_unique)
#task 10

def sum_of_input_digits() -> int:
    dig = input("Add digit: ")
    sumNum = 0
    if not dig.isdigit():
        print("Enter digit!!!")
    elif int(dig) == 0:
        print("Digit must be above 0!")
    else:
        for i in dig:
            sumNum = sumNum + int(i)
    return sumNum
print(sum_of_input_digits())
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""