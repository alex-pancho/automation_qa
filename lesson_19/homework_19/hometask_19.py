import sqlite3
import csv
import uuid
from pathlib import Path


table_name = "users"
columns = ["id", "username", "last_name",
           "gender",
           "email", "age", "created_at"]
data_types = ["INTEGER PRIMARY KEY", "TEXT NOT NULL", "TEXT NOT NULL",
              "INTEGER",
              "TEXT UNIQUE", "INTEGER CHECK (age >= 18)", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"]


class SQLiteDatabase:
    cursor = None
    connection = None

    def __init__(self, db_name=None):
        self.create_database(db_name)

    def create_database(self, db_name=None):
        self.connection = sqlite3.connect(':memory:') if db_name is None else sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table, columns, data_types):
        create_table_query = f'''
            CREATE TABLE IF NOT EXISTS {table} (
                {", ".join(f"{col} {data_types[i]}" for i, col in enumerate(columns))}
            );
        '''

        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_record(self, table, data):
        insert_query = f'''
            INSERT INTO {table} ({", ".join(data.keys())})
            VALUES ({", ".join("'" + str(a) + "'" for a in data.values())});
        '''

        self.cursor.execute(insert_query)
        self.connection.commit()

    def select_all_records(self, colum, table, **kwargs):
        select_string = f'SELECT {colum} FROM {table}'
        where_args = ""
        for key, value in kwargs.items():
            where_args += f" WHERE {key} = '{value}'" if where_args == "" else f" AND {key} = '{value}'"
        self.cursor.execute(select_string + where_args)
        return self.cursor.fetchall()

    def delete_record(self, table, **kwargs):
        sql = f"DELETE FROM {table} WHERE "
        where_args = ""
        for key, value in kwargs.items():
            where_args += f"{key} = '{value}'" if where_args == "" else f" AND {key} = '{value}'"
        self.cursor.execute(sql + where_args)
        self.connection.commit()

    def insert_from_csv(self, table, csv_data):
        for csv in csv_data:
            username, last_name = csv[0], csv[1]
            self.insert_record(table, {
                "username": username,
                "last_name": last_name,
            })


def read_csv(filename: Path) -> list:
    with filename.open("r", encoding="utf-8") as csvfile:
        data_read = csv.reader(csvfile, delimiter=",", quotechar='"')
        return list(data_read)


if __name__ == "__main__":
    my_db = SQLiteDatabase('mynewdb.db')

    columns = ["id", "username", "last_name",
               "gender",
               "email", "age", "created_at"]
    data_types = ["INTEGER PRIMARY KEY", "TEXT NOT NULL", "TEXT NOT NULL",
                  "INTEGER",
                  "TEXT UNIQUE", "INTEGER CHECK (age >= 18)", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"]
    my_db.create_table(table_name, columns, data_types)

    my_db.insert_record(table_name, {
        "username": "John",
        "last_name": "Smith",
        "email": f"{str(uuid.uuid4())}@example.com",
        "age": 22,
        "created_at": "2022-01-01 12:00:00"
    })
    my_db.insert_record(table_name, {
        "username": "Dave",
        "last_name": "Smith",
        "email": f"{str(uuid.uuid4())}@example.com",
        "age": 25,
        "created_at": "2022-01-01 12:00:00"
    })

    print("Select before delete:", my_db.select_all_records("*", "users", username="John", last_name="Smith"))
    my_db.delete_record(table_name, username='John')
    print("Select after delete:", my_db.select_all_records("*", "users", username="John", last_name="Smith"))

    # CSV read and insert
    filename = Path(__file__).parent / "users.csv"
    print(filename)
    print(filename.exists())
    data = read_csv(filename)
    my_db.insert_from_csv(table_name, data)
    print("Select all:", my_db.select_all_records("*", "users"))
