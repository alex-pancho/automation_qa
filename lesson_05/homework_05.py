small_list = [3, 1, 4, 5, 2, 5, 3]
#big_list = [3, 2, 1, 4]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("task 1, унікальні елементи в списку -", set(small_list))
# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
summ = 0
for i in big_list:
    summ = summ + i
print("task 2, середнє арифметичне списку big_list ", summ/len(big_list))
# task 3. Перевірте, чи є в списку big_list дублікати
if len(big_list)!=len(set(big_list)):
    print("task 3, так, в списку є дублікати")
else:
    print("task 3, ні, дублікатів немає")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
max_value = max(add_dict)
print("task 4, ключ з максимальним значенням - ", max_value)

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
new_dict = {}
for k, v in base_dict.items():
    new_dict[v] = k
print("task 5", new_dict)


# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
sum_dict = {}
for key, value in base_dict.items():
    if key in add_dict:
        sum_dict[key] = str(value) + str(add_dict[key])
    else:
        sum_dict[key] = value

for key, value in add_dict.items():
    if key not in sum_dict:
        sum_dict[key] = value

print("task 6", sum_dict)

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_line = set(line)
print("task 7", set_line)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
print("task 8, сума не спільних множин", sum(set_1 ^ set_2))

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
list_1 = set(list_1)
list_2 = set(list_2)
set_list = list_1 ^ list_2
print("task 9", set_list)


person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
new_dict = dict(person_list)
print(new_dict)
age_dict = {"10-19":[], "20-39":[], "30-39":[], "40-49":[]}
for key, value in person_list:
    if 10<v<19: 
        key = "10-19"
    elif 20<v<29:
        key = "20-29"
    elif 30<v<39:
        key = "30-39"
    elif 40<v<49:
        key = "40-49"
    else:
        continue
 
 #age_dict.append(value)
 
