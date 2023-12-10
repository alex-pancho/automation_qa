small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print("Всі унікальні елементи в списку small_list:", set(small_list))

# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
average_value = sum(small_list) / len(small_list) # или sum(small_list) // len(small_list) чтоб без десятичных
print("Cереднє арифметичне всіх елементів у списку small_list:", average_value)

# task 3. Перевірте, чи є в списку big_list дублікати
length_list = (len(big_list))
unique_values = set(big_list)
duplicates = (length_list == unique_values)
if duplicates != True :
    print("дублікати є")
else:
    print("дублікатів нема")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print("ключ з максимальним значенням у словнику add_dict:", max(add_dict.values()))

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
new_dict = {}
for key, value in add_dict.items():
  new_dict[value] = key
print("Новий словник, в якому ключі та значення замінені місцями у заданому словнику:",new_dict)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх

sum_dict = {}
sum_dict = (base_dict | add_dict)
sum_dict = list(zip(base_dict.values(), add_dict.values()))
print("task 6",sum_dict)
#Не совсем понял как обьединить значения когда ключи одиннаковы и проверить формат

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
print("Множина всіх символів", set(line))

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}

new_set = sum(set_1 ^ set_2)
print("Cума елементів двох множин, які не є спільними:", new_set)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]



list_1 = [('Alice', 25), ('Boby', 19), ('Charlie', 32), ('Vanessa', 37), ('Robert', 23)]
list2 = [('Vanessa', 37), ('Robert', 23),('David', 28), ('Emma', 22), ('Frank', 45)]
person_list_2 = list(set(list_1) ^ set(list2))
print(person_list_2)

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
new_dict = dict(person_list)
my_values = list(new_dict.values())
print(my_values)
#Данную задачу тоже не смог осилить пока