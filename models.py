import hashlib

from constants import *


class Region:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value not in REGIONS:
            raise ValueError(f'{value} not a valid region')
        self._name = value


class Country:

    def __init__(self, name, alpha2code, alpha3code, capital, region, language, time):
        self.name = name
        self.alpha2code = alpha2code
        self.alpha3code = alpha3code
        self.capital = capital
        self.region = region
        self.language = language
        self.time = time

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        region = Region(name=value)
        self._region = region.name

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        enc = hashlib.new('SHA1')
        enc.update(str(value[0]['nativeName']).encode('utf-8'))
        # 3
        self._language = enc.hexdigest()
