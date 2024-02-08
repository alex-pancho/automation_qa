import csv
import uuid
import sqlite3
from pathlib import Path
import os

current_file = Path(__file__)
current_dir = current_file.parent


class SQLiteModule:
    """
    Class SQLiteModule is a simple class to work with SQLite.
    Create SQLite DB at initialization.
    """
    def __init__(self, db_file):
        self.db_file = f'{db_file}.db'
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, table_columns=None):
        """
        Create a table and the table columns (optional)
        :param table_name: str
        :param table_columns: list of strings
        """
        if table_columns is None:
            table_columns = []

        if table_columns:
            columns_str = ', '.join(table_columns)
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str});"
        else:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} (ID INTEGER PRIMARY KEY);"

        self.cursor.execute(query)
        self.conn.commit()

        return self.cursor

    def insert_data(self, table_name, columns, data):
        """
        Insert new data into the exist table
        :param table_name: str, name of the table
        :param columns: tuple
        :param data: list of tuples [(), (), ...]
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))

        existing_table = self.cursor.fetchone()

        if existing_table:
            placeholders = ', '.join('?' for _ in data[0])
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders});"
            self.cursor.executemany(query, data)
        else:
            raise ValueError(f"Table {table_name} does not exist")

        self.conn.commit()
        return self.cursor

    def delete_record(self, table_name, condition_column, condition_value):
        """
        Delete records from the table based on a specified condition
        :param table_name: str, name of the table
        :param condition_column: str, column to check for the condition
        :param condition_value: Any, value to match in the specified column
        """
        query = f"DELETE FROM {table_name} WHERE {condition_column} = ?;"
        self.cursor.execute(query, (condition_value,))
        rows_deleted = self.cursor.rowcount
        self.conn.commit()

        if rows_deleted > 0:
            return f"{rows_deleted} rows were deleted from {table_name} successfully!"
        else:
            return f"No rows matching the condition were found in {table_name}."

    def fetch_all_records(self, table_name) -> list:
        """
        Fetch all records from the specified table
        :param table_name: str
        :return: list of tuples [(record1), (record2), ...]
        """
        self.cursor.execute(f"SELECT * FROM {table_name};")
        return self.cursor.fetchall()

    def get_table_columns(self, table_name):
        """
        Get column names for the specified table
        :param table_name: str, name of the table
        :return: List of column names
        """
        self.cursor.execute(f"PRAGMA table_info({table_name});")
        columns_info = self.cursor.fetchall()
        column_names = [column[1] for column in columns_info]
        return column_names

    def table_exists(self, table_name):
        """
        Check if a table with the given name exists in the database
        :param table_name: str, name of the table
        :return: bool, True if table exists, False otherwise
        """
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (table_name,))
        existing_table = self.cursor.fetchone()
        return existing_table is not None

    def import_csv(self, db_instance, tab_name):
        """
        Import data from a CSV file into a table with the same name as the CSV file
        :param db_instance: instance of class
        :param tab_name: str
        """
        csv_d = f'{Path(db_instance.db_file).stem}_CSV'
        csv_f = f'{tab_name}.csv'

        if not os.path.exists(csv_d):
            os.makedirs(csv_d)

        file_path = os.path.join(csv_d, csv_f)

        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?;", (tab_name,))
        existing_table = self.cursor.fetchone()

        if existing_table:
            self.cursor.execute(f"SELECT * FROM {tab_name};")
            rows = self.cursor.fetchall()

            with open(file_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([description[0] for description in self.cursor.description])
                csv_writer.writerows(rows)

            return f"Import from '{tab_name}' to CSV file '{file_path}' completed!"
        else:
            return f"The table '{tab_name}' doesn't found."

    @staticmethod
    def export_csv(csv_file, db_instance):
        """
        Export data from csv to table in DB
        :param csv_file: Path
        :param db_instance: instance of class
        """
        if not Path(csv_file).exists():
            raise FileNotFoundError(f"File {csv_file} is not found")

        table_name = Path(csv_file).stem

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            header = [col for col in (next(reader))]

            if db_instance.table_exists(table_name):
                new_table = f"{table_name}_from_csv"
                db_instance.create_table(new_table, header)

            table_columns = db_instance.get_table_columns(new_table)

            if header != table_columns:
                raise ValueError(f"CSV header does not match table columns for {table_name}")

            data = [tuple(row) for row in reader]
            db_instance.insert_data(new_table, header, data)

        return f"File {csv_file} was exported successfully to table {new_table}"

    @staticmethod
    def generate_uniq_id():
        """Generate a random id"""
        full_uuid = uuid.uuid4().int
        short_id = str(full_uuid)[:10]
        return short_id


if __name__ == "__main__":

    new_db = SQLiteModule("test_database")
    csv_file_path = current_dir / "test_database_CSV" / "car_models.csv"

    # new_db.create_table('car_models',
    #                     ['id INTEGER', 'brand TEXT', 'model TEXT', 'year INTEGER', 'price FLOAT'])

    # new_db.insert_data('car_models', ('id', 'brand', 'model', 'year', 'price'),
    #                    [
    #                        (f'{new_db.generate_uniq_id()}', 'AUDI', 'A7', 2022, 73845.00),
    #                        (f'{new_db.generate_uniq_id()}', 'BMW', 'X5', 2021, 53250.00),
    #                        (f'{new_db.generate_uniq_id()}', 'MERCEDES-BENZ', 'E-Class', 2023, 83845.00),
    #                     ])

    # new_db.insert_data('car_models', ('id', 'brand', 'model', 'year', 'price'),
    #                    [
    #                        # (f'{new_db.generate_uniq_id()}', 'Tayota', 'C-HR', 2023, 59900.00),
    #                        (f'{new_db.generate_uniq_id()}', 'AUDI', 'A4', 2019, 48921.00)
    #                    ])

    # for record in new_db.fetch_all_records('car_models'):
    #     print(record)

    # new_db.import_csv(new_db, 'car_models')

    # print(new_db.export_csv(csv_file_path, new_db))

    # print(new_db.delete_record('car_models', 'year', 2000))
