small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
for i in sorted(set(small_list)):
    print(i)


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print(sum(small_list))
print(len(small_list))
print(sum(small_list) // len(small_list))


# task 3. Перевірте, чи є в списку big_list дублікати
unique_set = set()
for i in big_list:
    if i in unique_set:
        print('duplicate', i)
    else:
        unique_set.add(i)


base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_dict = max(add_dict.values())
print(max_dict)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
origin_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Create a new dictionary with keys and values replaced by their positions
new_dict = {str(index): str(origin_dict[key]) for index, key in enumerate(origin_dict)}

print("Original_Dictionary:", origin_dict)
print("new_dictionary:", new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = {**add_dict, **base_dict}

for key in set(add_dict.keys()).union(base_dict.keys()):
    if key in add_dict and key in base_dict:
        sum_dict[key] = str(add_dict[key]) + str(base_dict[key])
    elif key in add_dict:
        sum_dict[key] = add_dict[key]
    elif key in base_dict:
        sum_dict[key] = base_dict[key]

print('combined_dictionary:', sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"

unique_characters = set(line)
print("Set of unique characters:", unique_characters)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
symmetric_difference_set = set_2 | set_1
print(symmetric_difference_set)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

set1 = set(list1)
set2 = set(list2)

result_set = set1.symmetric_difference(set2)

print("result_set:", result_set)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

age_dict = {'10-19': [], '20-29': [], '30-39': [], '40+': []}

for person in person_list:
    name, age = person
    if 10 <= age <= 19:
        age_dict['10-19'].append(name)
    elif 20 <= age <= 29:
        age_dict['20-29'].append(name)
    elif 30 <= age <= 39:
        age_dict['30-39'].append(name)
    else:
        age_dict['40+'].append(name)

print("result_dictionary:")
for age_range, names in age_dict.items():
    print(f"{age_range}: {names}")