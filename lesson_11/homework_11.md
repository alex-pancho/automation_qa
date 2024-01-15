**Управління Імперією (завдання підвищеної складності)**

Створити міні гру "Управління Імперією":

```python
# Початкові дані імперії
imperial_citizens = ["John", "Jane", "Bob", "Alice"]
resources = {"gold": 100, "wood": 50, "stone": 30}
```

Написати функції: 

```python
# Додати нового жителя до імперії
# Додаткова умова: додавати лише з унікальним ім'ям
def add_citizen(name):
```

```python
# Видалити жителя з імперії
def remove_citizen(name):
```

```python
# Додати ресурси до імперії
def add_resources(resource, amount):
```

Напишіть для цієї гри функцію market_place (resource_in, resource_out)
де здійсюється обмін ресурсів
5 stone = 1 gold
1 stone = 5 wood
25 wood = 1 gold

не забудьте додати перевірки і зміну наявних resources після обміну