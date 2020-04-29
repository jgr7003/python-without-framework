from apis import RegionApi, CountryApi
from models import Country
from reports import CountryReport


class Main:

    def start(self):
        countries = self.get_list_of_countries()
        self.create_countries_report(countries)

    def get_list_of_countries(self):
        region_api = RegionApi()
        regions = region_api.list()
        countries = []
        for region in regions:
            country_api = CountryApi()
            any_country = country_api.get_one_by_region(region)
            country = Country(
                name=any_country['name'],
                alpha2code=any_country['alpha2Code'],
                alpha3code=any_country['alpha3Code'],
                capital=any_country['capital'],
                region=any_country['region'],
                language=any_country['languages'],
                time=any_country['time']
            )
            countries.append(country.__dict__)
        return countries

    def create_countries_report(self, countries):
        report = CountryReport(countries)
        report.print()
        report.export()
        # report.save()


if __name__ == "__main__":
    main = Main()
    main.start()

