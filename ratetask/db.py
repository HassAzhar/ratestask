import psycopg2


class DB:
    def __init__(self):
        self.conn = psycopg2.connect(
            user="postgres", password="ratestask", host="127.0.0.1", port="5432"
        )
        self.cursor = self.conn.cursor()

    def commit(self):
        self.cursor.commit()

    def execute(self, query):
        self.cursor.execute(query)

    def fetchExecute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()


db = DB()
