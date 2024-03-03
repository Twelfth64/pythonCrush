import unittest
from city_functions import country_city

class TestCities(unittest.TestCase):

    def test_city_country(self):
        """Are names like 'santiago' 'chile' formatted correctly?"""
        formated_string = country_city('santiago', 'chile')
        self.assertEqual(formated_string, 'Santiago, Chile')
