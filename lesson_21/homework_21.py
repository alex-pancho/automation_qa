from pony.orm import *


sqlite_params = {
    'provider': 'sqlite',
    'filename': 'uakino.db',
    'create_db': True
}

mysql_params = {
    'provider': 'mysql',
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'uakino'
}


db = Database()


class Items(db.Entity):
    id = PrimaryKey(int, auto=True)
    title_ua = Required(str)
    title_or = Required(str)
    type_src = Required(str)
    year = Required(int)
    director = Required(str)
    description = Required(str)
    poster = Required(str)
    json = Required(str)
    imdb = Required(str)
    links = Set("Links")


class Seasons(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Required(int)
    name = Required(str)
    season = Required(str)
    title = Required(str)
    links = Set("Links")


class Links(db.Entity):
    id = PrimaryKey(int, auto=True)
    source_id = Required(int)
    series_id = Optional(int)
    quality = Required(str)
    its_work = Required(str)
    type_src = Required(str)
    m3u_links = Required(str)
    subs = Required(str)
    item = Required(Items)
    season = Required(Seasons)

def setup_database(provider, **kwargs):
    db.bind(provider, **kwargs)
    db.generate_mapping(create_tables=True)
    set_sql_debug(True)

@db_session
def add_to_db(item_data):
    item = Items(**item_data)
    commit()
    return item.id

@db_session
def check_in_base(item_id):
    return Items.exists(id=item_id)

@db_session
def add_m3u(link_data):
    link = Links(**link_data)
    commit()
    return link.id


@db_session
def save(item_data, link_data):
    item_id = add_to_db(item_data)
    link_data['source_id'] = item_id
    add_m3u(link_data)


setup_database(**mysql_params)
setup_database(**sqlite_params)