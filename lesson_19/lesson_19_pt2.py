import csv
import sqlite3

from pathlib import Path


class DB_one():

    def __init__(self, filename) -> None:
        self.conn_to_db(filename)
        self.create_table("users")

    def conn_to_db(self, filename=None):
        self.connection = sqlite3.connect(':memory:') # filename
        self.cursor = self.connection.cursor()

    def select(self, colum, table, **kwargs):
        select_string = f'SELECT {colum} FROM {table} WHERE '
        where_args = ""
        for key, value in kwargs.items():
            where_args += f"{key} = '{value}'"
        self.cursor.execute(select_string + where_args)
        return self.cursor.fetchall()

    def create_table(self, tab_name):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tab_name}
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        last_name,
        gender  INTGER,
        hobbies,
        street,
        area,
        landmark,
        province,
        city,
        zip
        );''')
        self.connection.commit()

    def insert(self, table, *args):
        for line in args:
            for csv in line:
                username, last_name = csv[1], csv[2]
                sql = f"INSERT INTO {table} (username, last_name) VALUES ('{username}', '{last_name}') "
                # print(sql)
                self.cursor.execute(sql)
        self.connection.commit()

def read_csv(filename: Path) -> list:
    with filename.open("r", encoding="utf-8") as csvfile:
        # dialect = csv.Sniffer().sniff(csvfile.read(1024))
        data_read = csv.reader(csvfile, delimiter=",", quotechar='"', )# dialect=dialect
        return list(data_read)


if __name__ == "__main__":
    filename = Path(__file__).parent.parent / "ideas_for_test" / "work_with_csv" / "random-michaels.csv"
    print(filename)
    print(filename.exists())
    data = read_csv(filename)
    print(data)
    my_db = DB_one('mynewdb.db')
    add_data = my_db.insert("users", data)
    first_select = my_db.select("*", "users", username= "FirstName")
    print("select>", first_select)
