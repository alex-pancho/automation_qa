small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

# task 1. Знайдіть всі унікальні елементи в списку small_list
uniq_v = set(small_list)
print(uniq_v)  # {1, 2, 3, 4, 5}

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average = int(sum(small_list) / len(small_list))
print(f"The arithmetic mean of the numbers in the list: {average}")

# task 3. Перевірте, чи є в списку big_list дублікати
big_set = set(big_list)
if len(big_set) == len(big_list):
    print("There are no duplicates in list!")
else:
    print("Opps...There are duplicates in list!")


base_dict = {'contry': 'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a": 1, "b": 2, "c": 2, "d": 3, 'size': 12}

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_key = max(add_dict, key=add_dict.get)
print(f"The key with biggest value is '{max_key}'.")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
new_dict = {}
for key, value in add_dict.items():
    new_dict[value] = key

print(new_dict)

# task 6. Об'єднайте два словники base_dict та add_dict в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = base_dict.copy()

for k, v in add_dict.items():
    if k in sum_dict:
        sum_dict[k] = f"{str(sum_dict[k])}, {str(v)}"
    else:
        sum_dict[k] = v

print(sum_dict)


# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
multiset = set(line)
print(multiset)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
set_sum = sum(set(set_1 | set_2))
print(set_sum)


# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
my_fav_animals = ['cat', 'dog', 'lion', 'mouse']
your_fav_animals = ['cat', 'elefant', 'monkey', 'dog']
our_symmetric_fav_animals = set(my_fav_animals) ^ set(your_fav_animals)
print(our_symmetric_fav_animals)


# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

result_dict = {}
# my_dict = dict((name, age) for name, age in person_list)
# print(my_dict)
# это мне почти ничего не дало, но решила оставить для себя

for name, age in person_list:
    age_range = f"{age // 10 * 10}-{age // 10 * 10 + 9}"

    if age_range not in result_dict:
        result_dict[age_range] = []

    result_dict[age_range].append(name)

print(result_dict)