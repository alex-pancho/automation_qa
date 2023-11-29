small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

# task 1. Знайдіть всі унікальні елементи в списку small_list

unique_elements = set(small_list)
print(unique_elements)
# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

average = sum(small_list) / len(small_list)
print(average)
# task 3. Перевірте, чи є в списку big_list дублікати

has_duplicates = len(big_list) != len(set(big_list))
print(has_duplicates)

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

max_key = max(add_dict, key=add_dict.get)
print(max_key)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

# мій рандомний словник

random_dict = {'name': 'Stepan', 'surname': 'Bandera', 'age': 42, 'city': 'Lviv'}

# Фліпаємо 
flipped_dict = {}

for key, value in random_dict.items():
    flipped_dict[value] = key
print(flipped_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}

for key in set(base_dict) | set(add_dict):
    base_value = base_dict.get(key, "")
    add_value = add_dict.get(key, "")
    sum_dict[key] = str(base_value) + str(add_value)

print(sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
print(set(line))

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

# task 8
sum_of_unique_elements = sum(set_1 ^ set_2)
print(sum_of_unique_elements)


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
unique_elements_set = set(list_1) ^ set(list_2)
print(unique_elements_set)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

# Створеня діапозонів
age_ranges = {
    '0-20': [],
    '21-30': [],
    '31-40': [],
    '41-99': []
}

for name, age in person_list:
    if 10 < age < 20:
        age_ranges['0-20'].append(name)
    elif 21 < age  < 30:
        age_ranges['21-30'].append(name)
    elif 31 < age < 40:
        age_ranges['31-40'].append(name)
    elif 41 < age < 99:
        age_ranges['41-99'].append(name)

print(age_ranges)