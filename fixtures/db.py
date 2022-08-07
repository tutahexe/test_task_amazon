import psycopg2

from models.item import Item


class Db:
    def __init__(self, db):
        self.db = db

    def write_single_item_to_db(self, item):
        """Writes item into the database"""
        db = self.db
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO items (name, release_date, rate) VALUES ('%s', '%s', %s);" % (
                item.get_name(), item.get_date(), item.get_rate()))
            conn.commit()
        conn.close()

    def write_items_to_db(self, items):
        """Writes many items into the database"""
        db = self.db
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            for item in items:
                try:
                    cursor.execute("INSERT INTO items (name, release_date, rate) VALUES ('%s', '%s', %s);" % (
                        item.get_name(), item.get_date(), item.get_rate()))
                except Exception as e:
                    print(e.args)
                    continue
                finally:
                    conn.commit()
        conn.close()

    def get_all_items_from_db(self):
        """Fetches all items into the database"""
        db = self.db
        items = []
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM items")
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
            cursor.execute("SELECT SUM (rate)/count(*) AS total FROM items;")
            medium_rate = cursor.fetchone()
        conn.close()
        return float(medium_rate[0])

    def get_items_with_title(self, title):
        """Searches for an item with specific title across all items into the database"""
        db = self.db
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM items WHERE name = '%s';" % (
                title))
            conn.commit()
            items = cursor.fetchall()
        conn.close()
        return items

    def get_newest_item(self):
        """Returns the newest item from database"""
        db = self.db
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM items ORDER BY release_date DESC;")
            conn.commit()
            row = cursor.fetchone()
            item = Item(name=row[1], date=row[2], rate=row[3])
        conn.close()
        return item

    def clean_up_table(self):
        """Delete all items from the item table in database"""
        db = self.db
        conn = psycopg2.connect(db)
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM items")
            conn.commit()
        conn.close()
        return True
