import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City("Cape Town", "South Africa", "Africa", True)


    def test_city_has_a_name(self):
        self.assertEqual("Cape Town", self.city.name)

    def test_city_has_country(self):
        self.assertEqual('South Africa', self.city.country_id)

    def test_city_has_continent(self):
        self.assertEqual('Africa', self.city.continent_id)

    def test_city_has_been_visited(self):
        self.assertEqual(True, self.city.visited)