from pony.orm import *
from pony.orm.core import sql_logger

db = Database()

sqlite = dict(
              provider='sqlite',
              filename='person.db',
              create_db=True
              )


mysql = dict(
             provider='mysql',
             host="127.0.0.1",
             user="student",
             passwd="welcome2qauto",
             db="person"
             )

class Person(db.Entity):
    name = Required(str)
    age = Optional(int)
    cars = Set('Car')

class Car(db.Entity):
    make = Required(str)
    model = Optional(str)
    owner = Required(Person)

# db.bind(sqlite)
db.bind(mysql)
db.generate_mapping(create_tables=True)
set_sql_debug(True)

# @db_session
# def add_user():
#     p1 = Person(name='Isaak', age=20)
#     c1 = Car(make="Audi", model="ssdd", owner=p1)
#     db.commit()
# add_user()

@db_session
def output():
    print(Car.select().show())
    print(Person.select().show())
    result = select(p for p in Person if p.age > 20)
    print(result.show())
output()
