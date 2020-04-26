from requests.exceptions import HTTPError

import validators
import pandas as pd
import requests
import random
from datetime import datetime


class Api:

    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        valid = validators.url(value)
        if valid is False:
            raise ValueError(f'{value} this url is wrong')
        self._url = value

    def get(self, headers=None, query_params=None):
        try:
            response = requests.get(self.url, headers=headers, params=query_params)
            json_response = response.json()
        except HTTPError as http_err:
            raise Exception(http_err)
        except ValueError as error:
            raise ValueError(error.__str__())
        except Exception as error:
            raise Exception(error.__str__())
        else:
            if response.status_code == 400:
                raise Exception("not found")
            if response.status_code == 500:
                raise Exception("gateway error")
            return json_response, response.status_code


class RegionApi:

    # 1
    def list(self):
        headers = {
            "x-rapidapi-host": "restcountries-v1.p.rapidapi.com",
            "x-rapidapi-key": "3969ec0ff4msh2152c45d799402fp142809jsn73581a198ec1"
        }
        api = Api('https://restcountries-v1.p.rapidapi.com/all')
        response, code = api.get(headers=headers)

        response_df = pd.DataFrame(response)
        regions = list(response_df.region.unique())
        return [string for string in regions if string != ""]


class CountryApi:

    def get(self, region):
        response = requests.get(str(f'https://restcountries.eu/rest/v2/region/{region}'))
        return response.json()

    def get_one_by_region(self, region):
        before = datetime.now()
        response = self.get(region)
        #  2
        choice = random.choice(response)
        later = datetime.now()
        # 4
        choice['time'] = (later-before).microseconds
        print(f"Country: {choice}")
        return choice
