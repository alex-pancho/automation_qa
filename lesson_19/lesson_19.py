import sqlite3

# створюємо конекшин
conn = sqlite3.connect('mynewdb.db')

# cursor
cursor = conn.cursor()

# Створення таблиці
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')

# Збереження змін у базі даних
conn.commit()

# Вставка даних
cursor.execute('''
    INSERT INTO users (username, email) VALUES (?, ?)
''', ('Fami Con', 'fami@example.com'))

# Збереження змін у базі даних
conn.commit()

# Вибірка даних
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Оновлення даних
cursor.execute('''
    UPDATE users SET email = ? WHERE username = ?
''', ('john.doe@example.com', 'JohnDoe'))

# Збереження змін у базі даних
conn.commit()

# Видалення даних
cursor.execute('DELETE FROM users WHERE id = ?', ('4',))

# Збереження змін у базі даних
conn.commit()

# Закриття підключення
conn.close()

