import sqlite3


class SqliteDriver:

    def __init__(self, database):
        # database = 'local.sqlite'
        self.database = database

    def connect(self):
        conn = sqlite3.connect(self.database)
        # conn = sqlite3.connect(database)
        return conn

    def exec(self, sql):
        conn = self.connect()
        cursor = conn.cursor()
        return cursor.execute(sql)

    def get(self, sql):
        cursor = self.exec(sql)
        rows = []
        for row in cursor:
            rows.append(row)
        return rows

    def insert(self, sql, values):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        return cursor.lastrowid


class Orm:

    def __init__(self, driver, database, user=None, password=None):
        if driver == 'sqlite':
            self.driver = SqliteDriver(database)
        else:
            Exception('not valid driver')

    def exec(self, sql):
        self.driver.exec(sql)

    def get(self, sql):
        self.driver.get(sql)

    def insert(self, sql, values):
        self.driver.insert(sql, values)
