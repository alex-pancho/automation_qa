small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
# task 1. Знайдіть всі унікальні елементи в списку small_list
print(f"Task #1:"
      f"\nUnique elements in list:\n{set(small_list)}")
# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
print("Task #2:")
number = 0
for i in big_list:
    number = number + i
print(f"Avg:\n{number}/{len(big_list)} = {number/len(big_list)}")
# task 3. Перевірте, чи є в списку big_list дублікати
print("Task #3:")
if big_list != set(big_list):
    print(f"There is duplicate in {big_list}"
          f"\nList without duplicates: {set(big_list)}")
else:
    print("No duplicate")

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
print(f"Task #4:"
      f"\nThe most big value is: {max(add_dict.values())}")

# task 5. Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
new_dict = {'login':'user', 'password': 123456}
print("Task #5")
revers_new_dict = {}
for v, k in new_dict.items():
    revers_new_dict[k] = v
print(f"Reversed dict: {revers_new_dict}")
# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
print("Task #6:")
sum_dict = base_dict
sum_dict.update(add_dict)
print(f"base_dict + add_dict = {sum_dict}")
# task 7.
print("Task #7:")
line = "Створіть множину всіх символів, які входять у заданий рядок"
print(f"Set of all symbols: {set(line)}")
# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
print("Task #8")
sets_unique = set_1 ^ set_2
print(f"Sum of uniq elements is {sum(sets_unique)}")

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
print("Task #9:")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
set1 = set(list1)
set2 = set(list2)
print(set1 ^ set2)

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
newList = {'10-19': [], '20-29': [], '30-39': [], '40-49': []} #я багато гуглив, але так і не знайшов як автоматично поміняти місцями ключі та значення у цьому віподку, бо в умовах воно очікує стрінгу
for n, a in person_list:
# newList[a] = n
    if 10 <= a <= 19:
        newList['10-19'].append(n)
    elif 20 <= a <= 29:
        newList['20-29'].append(n)
    elif 30 <= a <= 39:
        newList['30-39'].append(n)
    elif 40 <= a <= 49:
        newList['40-49'].append(n)
print(newList)