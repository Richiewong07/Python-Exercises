import unittest
from city_function import get_city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_function.py'."""

    def test_city_country(self):
        city_country = get_city_country('houston', 'united states')
        self.assertEqual(city_country, 'Houston, United States')

    def test_city_country_population(self):
        city_country_population = get_city_country('toronto', 'canada', '60000000')
        self.assertEqual(city_country_population, 'Toronto, Canada: 60000000')

unittest.main()
