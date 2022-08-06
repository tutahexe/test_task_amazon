import psycopg2

from config_helper import read_value_from_config


def init_db():
    """Creates table inside DB for further work"""
    db = read_value_from_config('db_connection')
    conn = psycopg2.connect(db)
    with conn.cursor() as cursor:
        with open("item.sql", "r") as table_sql:
            cursor.execute(table_sql.read())
            conn.commit()
    conn.close()


if __name__ == "main":
    init_db()
