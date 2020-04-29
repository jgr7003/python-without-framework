import pandas as pd
import simplejson as json

from orm import Orm
from constants import CURRENT_DATABASE_DRIVER, CURRENT_DATABASE_HOST


class CountryReport:

    def __init__(self, countries):
        self.countries = pd.DataFrame(countries)
        print(f"Table: {self.countries}")
        # 6
        self.avg = self.countries['time'].mean()
        self.sum = self.countries['time'].sum()
        self.min = self.countries['time'].min()
        self.max = self.countries['time'].max()

    def export(self):
        # 8
        file = open("./data.json", "w+")
        file.write(json.dumps(self.countries.to_dict('records')))
        file.close()

    def print(self):
        print(f"Avg: {self.avg}")
        print(f"Sum: {self.sum}")
        print(f"Min: {self.min}")
        print(f"Max: {self.max}")

    def save(self):
        orm = Orm(CURRENT_DATABASE_DRIVER, CURRENT_DATABASE_HOST)
        for index, row in self.countries.iterrows():
            sql = "INSERT INTO report (region, capital, language, time) VALUES (?, ?, ?, ?)"
            values = [row['_region'], row['capital'], row['_language'], row['time']]
            insert_id = orm.insert(sql, values)
            print(f"Insert id: {insert_id}")
