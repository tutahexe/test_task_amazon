import psycopg2

from models.item import Item


def write_data_to_db():
    item = Item(name='kek', rate=0.5, date="Aug 3, 0001")
    db = "postgres://postgres:postgrespw@localhost:49153"
    conn = psycopg2.connect(db)
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO items55 (name, release_date, rate) VALUES ('%s', '%s', %s);" % (
            item.get_name(), item.get_date(), item.get_rate()))
        conn.commit()
    conn.close()


def init_db():
    """Creates table inside DB for further work"""
    db = "postgres://postgres:postgrespw@localhost:49153"
    conn = psycopg2.connect(db)
    with conn.cursor() as cursor:
        with open("item.sql", "r") as table_sql:
            cursor.execute(table_sql.read())
            conn.commit()
    conn.close()


def get_db_data():
    db = "postgres://postgres:postgrespw@localhost:49153"
    conn = psycopg2.connect(db)
    with conn.cursor() as cursor:
        cursor.execute("select * from items55")
        items_records = cursor.fetchall()
        for row in items_records:
            date2 = str(row[2])
            print(row)
            print(Item(name=row[1], date=date2, rate=row[3]))
    conn.close()


def get_medium_rate():
    db = "postgres://postgres:postgrespw@localhost:49153"
    conn = psycopg2.connect(db)
    with conn.cursor() as cursor:
        #cursor.execute("SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY rate) AS median FROM items55")
        cursor.execute("SELECT SUM (rate)/count(*) AS total FROM items55;")
        items_records = cursor.fetchall()
        print(items_records)
    conn.close()
