# Знайти та виправити помилку в стороньому модулі
**складність**: середня

1. Зробити форк від [форку](https://github.com/dntpanix/randominfo)

2. Скопіювати в папку на свій комп

3. Відкрити папку у новому проекті IDE

4. Створити у проекті файл з таким змістом:
    ```python
    import randominfo
    person = randominfo.Person()
    print(person.full_name, person.gender, person.country, person.address)
    ```
5. Запустити файл і отримати помилку

6. Створити бренч(гілку)

7. Виправити помилку і запушити у власний бренч у ваш форк

8. Створити ПР з вашого бренча/форка у main https://github.com/dntpanix/randominfo

9. Дати посилання на ПР у форму відповіді