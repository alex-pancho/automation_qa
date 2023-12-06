small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list

unique_elements = set(small_list)
print("Унікальні елементи в small_list:", unique_elements)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list

average = sum(small_list) / len(small_list)

print("Середнє арифметичне у small_list:", average)

# task 3. Перевірте, чи є в списку big_list дублікати

has_duplicates = len(big_list) != len(set(big_list))

if has_duplicates:
    print("У списку big_list є дублікати.")
else:
    print("У списку big_list немає дублікатів.")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict

max_key = max(add_dict, key=add_dict.get)
max_value = add_dict[max_key]
print(f"Ключ з максимальним значенням: {max_key}, його значення: {max_value}")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику

some_dict = {'key_1':123, 'key_2':'value_2', 'key_3':'value_3'}
reversed_dict = {v:k for k, v in some_dict.items()}
print(f"Новий словник зі зміненими ключами та значеннями:, {reversed_dict}")

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = base_dict.copy()
sum_dict.update((key, str(base_dict[key]) + str(add_dict[key])) for key in add_dict.keys() if key in base_dict)
sum_dict.update((key, value) for key, value in add_dict.items() if key not in base_dict)
print("Об'єднаний словник sum_dict:", sum_dict)

# task 7.

line = "Створіть множину всіх символів, які входять у заданий рядок"
character_set = set(line)
print("Множина всіх символів у рядку:", character_set)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
sum_of_unique_elements = sum(set_1.union(set_2) - set_1.intersection(set_2))
print("Сума елементів двох множин, які не є спільними:", sum_of_unique_elements)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

unique_set = set(list_1) ^ set(list_2)

print("Сет унікальних елементів:", unique_set)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

age_ranges_dict = {}
for name, age in person_list:
    age_range_start = (age // 10) * 10
    age_range_end = age_range_start + 9
    age_range = f"{age_range_start}-{age_range_end}"

    if age_range in age_ranges_dict:
        age_ranges_dict[age_range].append(name)
    else:
        age_ranges_dict[age_range] = [name]

print(age_ranges_dict)