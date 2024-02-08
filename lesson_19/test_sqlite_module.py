import pytest
import csv
from pathlib import Path
from SQLite_Module import SQLiteModule

current_file = Path(__file__)
current_dir = current_file.parent


@pytest.fixture
def db():
    """ Create database instance for all next tests """
    database = SQLiteModule("test_database")
    yield database
    database.conn.close()


@pytest.fixture(autouse=True)
def cleanup_table(db):
    """ Delete table after use for each test """
    table_name = 'test_table'
    yield
    db.cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    db.conn.commit()


@pytest.fixture
def sample_data(db):
    """ Default data for create table and insert some data into it """
    table_name = 'test_table'
    columns = ("id", "name")
    data = [(1, 'John'), (2, 'Drake')]

    db.create_table(table_name, columns)
    db.insert_data(table_name, columns, data)
    return {'test_table': [(1, 'John'), (2, 'Drake')]}


@pytest.fixture
def sample_csv_data(tmpdir):
    """ Default data for work with csv files """
    csv_file_path = current_dir / "test_database_CSV" / "test_table.csv"

    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['id', 'name'])
        csv_writer.writerow(['1', 'John'])
        csv_writer.writerow(['2', 'Drake'])

    return {'csv_file_path': csv_file_path}


def test_create_database():
    """Test for check is db was created"""
    db = SQLiteModule("test_database")
    assert db is not None


def test_create_table_with_columns(db):
    """Test for check if table with columns was created"""
    table_name = "test_table"
    columns = ["id INTEGER", "name TEXT"]

    db.create_table(table_name, columns)
    assert db.table_exists(table_name)


def test_create_table_without_columns(db):
    """Test for check id table without columns was created"""
    table_name = "test_table"
    expected_column = ['ID']

    db.create_table(table_name)
    assert db.table_exists(table_name)
    assert db.get_table_columns(table_name) == expected_column


def test_insert_data(db):
    """Test for check if rows were added to exist table in db"""
    table_name = 'test_table'
    columns = ("id", "name")
    data = [(1, 'John'), (2, 'Drake')]

    db.create_table(table_name, columns)
    db.insert_data(table_name, columns, data)

    result = db.fetch_all_records(table_name)
    assert len(result) == 2
    assert result[0] == (1, "John")
    assert result[1] == (2, 'Drake')


def test_insert_data_error(db):
    """Test for check ValueError if table is not exist"""
    with pytest.raises(ValueError, match=f"Table non_existent_table does not exist"):
        table_name = "non_existent_table"
        columns = ("id", "name")
        data = [(1, 'John')]
        db.insert_data(table_name, columns, data)


def test_delete_records(db, sample_data):
    """Test for deleting rows with correct condition"""
    table_name = 'test_table'

    db.delete_record(table_name, 'id', 2)
    result = db.fetch_all_records(table_name)
    assert len(result) == 1


def test_delete_fake_records(db, sample_data):
    """Test for deleting rows with incorrect condition"""
    table_name = 'test_table'

    db.delete_record(table_name, 'id', 3)
    result = db.fetch_all_records(table_name)
    assert len(result) == 2


def test_fetch_all_records(db, sample_data):
    """Test for check if func fetch correct all records"""
    table_name = 'test_table'
    expected_data = sample_data['test_table']
    actual_data = db.fetch_all_records(table_name)

    assert len(actual_data) == len(expected_data)
    assert actual_data == expected_data


def test_import_csv(db, sample_data):
    """Test for check if import from table in DB to csv file was correct"""
    csv_file_path = current_dir / "test_database_CSV" / "test_table.csv"
    result_csv = db.import_csv(db, 'test_table')

    assert csv_file_path.exists()

    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        assert header == ['id', 'name']

        rows = list(reader)
        assert len(rows) == 2

        expected_data = [str(row[0]) for row in sample_data['test_table']]
        actual_data = [row[0] for row in rows]
        assert actual_data == expected_data


def test_export_csv(db, sample_data, sample_csv_data):
    """Test for check if export from csv file to table in DB was correct"""
    csv_file_path = sample_csv_data['csv_file_path']
    table_name = "test_table_from_csv"
    result = db.export_csv(csv_file_path, db)

    assert db.table_exists(table_name)

    records = db.fetch_all_records(table_name)
    assert len(records) == 2
    assert records == [("1", 'John'), ("2", 'Drake')]

    db.cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
    db.conn.commit()


if __name__ == '__main__':
    pytest.main()
