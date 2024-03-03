import unittest
from city_functions import country_city


class TestCities(unittest.TestCase):

    def test_city_country(self):
        """Are names like 'santiago' 'chile' formatted correctly?"""
        formated_string = country_city('santiago', 'chile')
        self.assertEqual(formated_string, 'Santiago, Chile')

    def test_city_country_population(self):
        """Are names like 'santiago' 'chile' '5000000' formatted correctly?"""
        formated_string = country_city('santiago', 'chile', '5 000 000')
        self.assertEqual(formated_string, 'Santiago, Chile - 5 000 000')
