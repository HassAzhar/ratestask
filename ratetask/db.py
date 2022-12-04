import psycopg2


class DB:
    def __init__(self):
        self.conn = psycopg2.connect(
            user="postgres", password="ratestask", host="127.0.0.1", port="5432"
        )
        self.cursor = self.conn.cursor()

    def reinit(self):
        self.conn = psycopg2.connect(
            user="postgres", password="ratestask", host="127.0.0.1", port="5432"
        )
        self.cursor = self.conn.cursor()

    def fetch_execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # To convert a list of lists to a single list. Useful for similar data type results
    def fetch_formatted(self, query):
        res = self.fetch_execute(query)
        return list(map(lambda item: item[0], res))


db = DB()
