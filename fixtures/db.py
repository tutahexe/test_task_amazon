import psycopg2

from config_helper import read_value_from_config
from models.item import Item


class Db:
    def __init__(self):
        self.db = read_value_from_config('db_connection')

    def write_data_to_db(self, item):
        """Writes item into the database"""
        db = self.db
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO items55 (name, release_date, rate) VALUES ('%s', '%s', %s);" % (
                item.get_name(), item.get_date(), item.get_rate()))
            conn.commit()
        conn.close()

    def get_all_items_from_db(self):
        """Fetches all items into the database"""
        db = self.db
        items = []
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("select * from items55")
            items_records = cursor.fetchall()
            for row in items_records:
                items.append(Item(name=row[1], date=row[2], rate=row[3]))
        conn.close()
        return items

    def get_medium_rate(self):
        """Calculates and return medium rate across all items into the database"""
        db = self.db
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("SELECT SUM (rate)/count(*) AS total FROM items55;")
            medium_rate = cursor.fetchall()
        conn.close()
        return medium_rate

    def get_item_with_title(self, title):
        """Searches for an item with specific title across all items into the database"""
        db = self.db
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("SELECT * from items55 where name = '%s';" % (
                title))
            conn.commit()
            item = cursor.fetchall()
        conn.close()
        return item

    def get_newest_item(self):
        """Returns the newest item from database"""
        db = self.db
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("SELECT * from items55 ORDER BY release_date DESC;")
            conn.commit()
            row = cursor.fetchone()
            item = Item(name=row[1], date=row[2], rate=row[3])
        conn.close()
        return item
