import unittest
from models.country import Country

class TestCountry(unittest.TestCase):
    def setUp(self):
        self.country = Country("South Africa","Africa", True)


    def test_country_has_name(self):
        self.assertEqual("South Africa", self.country.name)

    def test_country_has_continent(self):
        self.assertEqual("Africa", self.country.continent_id)

    def test_country_has_been_visited(self):
        self.assertEqual(True, self.country.visited)