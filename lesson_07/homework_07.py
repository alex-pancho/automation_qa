# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    while multiplier in range (1, 10):
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел."""
def suma(x, y):
     print(x + y)

suma(24, 1)

#task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg(*args):
    print(sum(args) / len(args))

avg(2, 4, 2, 2, 0)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(x):
    print(str(x[::-1]))

reverse("Це треба перекрутити")


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
arg_list = []
def long_word(*args):
    for arg in args:
        arg_list.append(arg)
    print(max(arg_list, key=len))

long_word("Slovo", "Slovooooooo", "Slovoo")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
'''У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?'''

def trees_total(apple, peer, plum):
    '''Функція приймає кількість яблукб груш і слив, та виводить загальну кількусть дерев у саду'''
    print(apple + peer + plum)

apple = 45
peer = 21
plum = 18
trees_total(apple, peer, plum)

# task 8
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами."""

def space_delete(text):
    """Приймає текст і видаляє у ньому зайві пробіли"""
    while "  " in text:
        text = text.replace('  ', ' ')
        print(text)

text = "Pfj   jfekk efk  jejfl            ejfkejhlkj;jorsg fehfqi  jhefqhk"
space_delete(text)

# task 9
""" Виведіть кількість слів останнього речення з текста.
"""

def words_count_in_sentence(text_, sentence_number):
    """Приймає текст та номер речення, після чого виводить кількість слів у заданому реченні"""
    sentence_num = sentence_number - 1 #роблю номер речення більш звичним
    text_ = text_.split(".")
    text_ = text_[sentence_num]
    text_ = text_.split()
    return len(text_)

text_ = "Тут буде чотири слова. Тут три слова. А тут вже п'ять слів."
print(words_count_in_sentence(text_, 2))


# task 10
"""Створіть новий словник, в якому ключі та значення будуть замінені місцями у заданому словнику"""

def dict_switch(dict1):
    "Функція, що зміняю значення та ключі місцями у заданому словнику"
    keys = list(dict1.values())
    values = list(dict1.keys())
    dict1 = dict(zip(keys, values))
    print(dict1)

dict1 = {"a":11, "b":22, "c":222, "d":33, 'size': 12}
dict_switch(dict1)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
