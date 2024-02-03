import sqlite3
import csv
import unittest
import os

class SQLiteDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()

    def create_table(self, table_name, columns):
        """
        Creates a table in a specified database with specified columns.
        columns should be a list of tuples (column_name, data_type, constraints)
        """
        try:
            create_table_query = f"CREATE TABLE {table_name} ("
            create_table_query += ", ".join([f"{col[0]} {col[1]} {col[2]}" for col in columns])
            create_table_query += ");"

            self.cursor.execute(create_table_query)
            self.connection.commit()
            print(f"Table {table_name} created successfully.")
        except sqlite3.Error as e:
            print(f"Error while table creating: {e}")

    def insert_record(self, table_name, data):
        """
        Insert records in DB
        data format: {'column1': value1, 'column2': value2, ...}
        """
        columns_str = ', '.join(data.keys())
        values_str = ', '.join(['?' for _ in data])

        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"

        try:
            self.cursor.execute(insert_query, list(data.values()))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error inserting record: {e}")

    def read_csv_and_insert(self, csv_file, table_name):
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            columns = [(field, 'TEXT', '') for field in reader.fieldnames]
            self.create_table(table_name, columns)
            for row in reader:
                self.insert_record(table_name, row)

    def select_all_records(self, table_name):
        select_all_records = f"SELECT * FROM {table_name}"
        self.cursor.execute(select_all_records)
        return self.cursor.fetchall()


    def delete_record(self, table_name, condition_column, condition_value):
        delete_query = f"DELETE FROM {table_name} WHERE {condition_column} = ?"
        try:
            self.cursor.execute(delete_query, (condition_value,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error deleting record: {e}")

import unittest
import os

class TestSQLiteDatabase(unittest.TestCase):
    def setUp(self):
        """
        Create an instance of SQLiteDatabase for testing
        """
        self.db_name = "test.db"
        self.db = SQLiteDatabase(self.db_name)

    def tearDown(self):
        """
        Close the database connection and delete the test database file
        """
        self.db.connection.close()
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_create_table(self):
        """
        Test table creation
        """
        table_name = "some_test_table"
        columns = [
            ("id", "INTEGER", "PRIMARY KEY"),
            ("name", "TEXT", ""),
            ("age", "INTEGER", "")
        ]

        self.db.create_table(table_name, columns)

        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name=?"
        self.db.cursor.execute(query, (table_name,))
        table_exists = self.db.cursor.fetchone() is not None
        self.assertTrue(table_exists)
    def test_insert_record(self):
        """
        Test inserting record in the test table
        """
        table_name = "some_test_table"
        columns = [("id", "INTEGER", "PRIMARY KEY"), ("name", "TEXT", ""), ("age", "INTEGER", "")]
        self.db.create_table(table_name, columns)

        record = {"id": 1, "name": "John Doe", "age": 25}
        self.db.insert_record(table_name, record)

        records = self.db.select_all_records(table_name)
        records_dict = [dict(zip([col[0] for col in columns], row)) for row in records]
        self.assertIn(record, records_dict)

    def test_read_csv_and_insert(self):
        """
        Testing with csv
        """
        table_name = "some_test_table"
        csv_file = "test_data.csv"

        with open(csv_file, 'w') as file:
            file.write("id,name,age\n1,John Doe,25\n2,Jane Doe,30\n")

        self.db.read_csv_and_insert(csv_file, table_name)

        records = self.db.select_all_records(table_name)
        self.assertEqual(len(records), 2)

    def test_delete_record(self):
        """
        Test deleting record from the table
        """
        table_name = "some_test_table"
        columns = [("id", "INTEGER", "PRIMARY KEY"), ("name", "TEXT", ""), ("age", "INTEGER", "")]
        self.db.create_table(table_name, columns)

        record = {"id": 1, "name": "John Doe", "age": 25}
        self.db.insert_record(table_name, record)

        self.db.delete_record(table_name, "id", 1)

        records = self.db.select_all_records(table_name)
        self.assertNotIn(record, records)

    def test_select_all_records_empty_table(self):
        """
        Test selecting all records from an empty table
        """
        table_name = "empty_table"
        columns = [("id", "INTEGER", "PRIMARY KEY"), ("name", "TEXT", ""), ("age", "INTEGER", "")]
        self.db.create_table(table_name, columns)

        records = self.db.select_all_records(table_name)
        self.assertEqual(len(records), 0)



if __name__ == '__main__':
    unittest.main()


