# 11
import unittest
import random
import os

from apis import CountryApi, RegionApi
from main import Main
from reports import CountryReport
from constants import REGIONS


class RegionApiTest(unittest.TestCase):

    def get_test(self):
        region_api = RegionApi()
        result = region_api.list()
        self.assertGreater(len(result), 0)


class CountryApiTest(unittest.TestCase):

    def get_test(self):
        country_api = CountryApi()
        region = random.choice(REGIONS)
        result = country_api.get_one_by_region(region[0])
        self.assertGreater(len(result), 0)


class CountryReportTest(unittest.TestCase):

    def init_test(self):
        main = Main()
        countries = main.get_list_of_countries()
        report = CountryReport(countries)
        self.assertIsNotNone(report.avg)
        self.assertIsNotNone(report.max)
        self.assertIsNotNone(report.min)
        self.assertIsNotNone(report.sum)

    def export_test(self):
        os.remove("data.json")
        main = Main()
        countries = main.get_list_of_countries()
        report = CountryReport(countries)
        report.export()
        try:
            f = open("data.json")
        except IOError:
            self.assertFalse(True)
        else:
            f.close()


if __name__ == "__main__":
    unittest.main()
