from bd_homework import DatabaseManager

import unittest
import os

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db_name = "test_database.db"
        self.db_manager = DatabaseManager(self.db_name)

    def tearDown(self):
        self.db_manager.close_connection()

        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_create_table(self):
        table_name = "test_table"
        self.db_manager.create_table(table_name)

        cursor = self.db_manager.connection.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        self.assertEqual(len(columns), 3)

    def test_insert_and_select_records(self):
        table_name = "test_table"
        self.db_manager.create_table(table_name)

        self.db_manager.insert_record(table_name, (1, "John", "Doe"))
        self.db_manager.insert_record(table_name, (2, "Jane", "Smith"))

        records = self.db_manager.select_all_records(table_name)

        self.assertEqual(len(records), 2)

        self.assertIn((1, "John", "Doe"), records)
        self.assertIn((2, "Jane", "Smith"), records)

    def test_delete_record(self):

        table_name = "test_table"
        self.db_manager.create_table(table_name)

        self.db_manager.insert_record(table_name, (1, "John", "Doe"))
        self.db_manager.insert_record(table_name, (2, "Jane", "Smith"))

        self.db_manager.delete_record(table_name, "user_id=1")

        records_after_delete = self.db_manager.select_all_records(table_name)

        self.assertEqual(len(records_after_delete), 1)

        self.assertIn((2, "Jane", "Smith"), records_after_delete)

if __name__ == "__main__":
    unittest.main()
