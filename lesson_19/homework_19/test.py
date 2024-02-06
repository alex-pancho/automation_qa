import unittest
import hometask_19

table_name = hometask_19.table_name
columns = hometask_19.columns
data_types = hometask_19.data_types


class TestDatabase(unittest.TestCase):
    my_db = None

    @classmethod
    def setUpClass(cls):
        cls.my_db = hometask_19.SQLiteDatabase()  # Use in memory DB
        cls.my_db.create_table(table_name, columns, data_types)

    def test_insert_select(self):
        expected = [(1, 'John', 'Smith', None, 'john@example.com', 22, '2022-01-01 12:00:00')]
        self.my_db.insert_record(table_name, {
            "username": "John",
            "last_name": "Smith",
            "email": "john@example.com",
            "age": 22,
            "created_at": "2022-01-01 12:00:00"
        })
        res_select = self.my_db.select_all_records("*", "users", username="John", last_name="Smith")
        self.assertEqual(expected, res_select)

    def test_delete(self):
        expected = []
        self.my_db.insert_record(table_name, {
            "username": "John",
            "last_name": "Smith",
            "email": "john@example.com",
            "age": 22,
            "created_at": "2022-01-01 12:00:00"
        })
        self.my_db.delete_record(table_name, username='John')
        res_select = self.my_db.select_all_records("*", "users", username="John")
        self.assertEqual(expected, res_select)


if __name__ == '__main__':
    unittest.main()
