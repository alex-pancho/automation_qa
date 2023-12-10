small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list_unique = set(small_list)
print(small_list_unique)

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
small_list_avg = sum(small_list) / len(small_list)
print(small_list_avg)

# task 3. Перевірте, чи є в списку big_list дублікати
if len(big_list) == len(set(big_list)):
    print( "В списку немає дублікатів")
else:
    print("В списку є дублікати")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
add_dict_values = set(add_dict.values())
print(max(add_dict_values))

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
keys = list(base_dict.values())
values = list(base_dict.keys())
new_dict = dict(zip(keys, values))
print(new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
for key, value in base_dict.items():
    if key in add_dict.keys():
        for key2, value2 in add_dict.items():
            if key2 == key:
                add_dict[key2] = str(value) + str(value2)
sum_dict = base_dict | add_dict
print(sum_dict)

# task 7.
set_line = []
line = "Створіть множину всіх символів, які входять у заданий рядок"
line = line.replace(" ","")
for s in line:
    set_line.append(s)
set_line = set(set_line)
print(set_line)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
set_3 = set_1 ^ set_2
print(sum(set_3))

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

first_list = [2, 4, 5, 7, 3]
second_list = [4, 5, 1, 9, 3]
return_set = set(first_list) ^ set(second_list)
print(return_set)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
final_dict = {}
key_list_1 = []
key_list_2 = []
key_list_3 = []
key_list_4 = []
person_dict = dict(person_list)
for key, value in person_dict.items():
    if value in range(10, 20):
        key_list_1.append(key)
        final_dict["10-19"] = key_list_1
    elif value in range(20, 30):
        key_list_2.append(key)
        final_dict["20-29"] = key_list_2
    elif value in range(30, 40):
        key_list_3.append(key)
        final_dict["30-39"] = key_list_3
    else:
        if value in range(40, 50):
            key_list_4.append(key)
            final_dict["40-49"] = key_list_4
print(final_dict)