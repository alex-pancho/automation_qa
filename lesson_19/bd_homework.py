import sqlite3
import csv

class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name):
        create_table_query = (f"CREATE TABLE {table_name} "
                              f"(user_id INTEGER PRIMARY KEY, "
                              f"name TEXT, "
                              f"lastname TEXT)")
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_record(self, table_name, data):
        insert_record_query = (f"INSERT INTO {table_name} "
                               f"VALUES "
                               f"(?,?,?)")
        self.cursor.execute(insert_record_query, data)
        self.connection.commit()

    def select_all_records(self, table_name):
        select_all_query = f"SELECT * FROM {table_name}"
        self.cursor.execute(select_all_query)
        return self.cursor.fetchall()

    def read_csv_into_table(self, csv_file):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)

            create_table_query = f"CREATE TABLE {csv_file[:-4]} ({', '.join([f'{header} TEXT' for header in headers])})"
            self.create_table(csv_file[:-4])

            for row in reader:
                self.insert_record(csv_file[:-4], row)

    def delete_record(self, table_name, condition):
        delete_record_query = (f"DELETE FROM {table_name} "
                               f"WHERE {condition}")
        self.cursor.execute(delete_record_query)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()


if __name__ == "__main__":
    db_manager = DatabaseManager("data_users.db")

    db_manager.create_table("users")

    db_manager.insert_record("users", (1, "John", "Doe"))
    db_manager.insert_record("users", (2, "Jane", "Smith"))

    all_records = db_manager.select_all_records("users")
    print("All Records:", all_records)

    db_manager.delete_record("users", "user_id=1")

    all_records_after_delete = db_manager.select_all_records("users")
    print("All Records after deletion:", all_records_after_delete)

    db_manager.read_csv_into_table("users_db.csv")

    all_records = db_manager.select_all_records("users")
    print("All Records:", all_records)

    db_manager.close_connection()
