import psycopg2

from config_helper import read_value_from_config

sql = "CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY,name VARCHAR(150) NOT NULL,release_date date NOT NULL," \
      "rate DOUBLE PRECISION NOT NULL); "


def init_db():
    """Creates table inside DB for further work"""
    db = read_value_from_config('db_connection')
    conn = psycopg2.connect(db)
    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
