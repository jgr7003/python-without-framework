import sqlite3


class SqliteDriver:

    def __init__(self, database):
        conn = sqlite3.connect(database)
        self.cursor = conn.cursor()

    def exec(self, sql):
        self.cursor.execute(sql)

    def get(self, sql):
        self.exec(sql)
        rows = []
        for row in self.cursor:
            rows.append(row)
        return rows

    def insert(self, sql, values):
        self.cursor(sql, values)

    def confirm(self):
        self.cursor.close()


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

    def confirm(self):
        self.driver.confirm()
