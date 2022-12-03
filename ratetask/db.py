import psycopg2


class DB:
    def __init__(self):
        self.conn = psycopg2.connect(
            user="postgres", password="ratestask", host="127.0.0.1", port="5432"
        )
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def execute(self, query):
        self.cursor.execute(query)

    def fetch_execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_formatted(self, query):
        res = self.fetch_execute(query)
        return list(map(lambda item:item[0], res))


db = DB()
