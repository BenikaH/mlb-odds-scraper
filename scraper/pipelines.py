import sqlite3 as sl


class SQLitePipeline(object):
    def __init__(self):
        self.setup_conn()
        self.drop_events()
        self.create_events()

    def __del__(self):
        self.close_conn()

    def process_item(self, item, spider):
        self.store_event(item)
        return item

    def setup_conn(self):
        self.conn = sl.connect('events.db')
        self.cur = self.conn.cursor()

    def drop_events(self):
        self.cur.execute(
            "DROP TABLE IF EXISTS events")

    def create_events(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS \
             events (id INTEGER)")

    def store_event(self, item):
        self.cur.execute(
            "INSERT INTO events (id) VALUES (?)",
            (item.get('id',''),))
        self.conn.commit()

    def close_conn(self):
        self.conn.close()
