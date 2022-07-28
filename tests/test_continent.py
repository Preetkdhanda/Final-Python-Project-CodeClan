import unittest
from models.continent import Continent

class TestContinent(unittest.TestCase):
    def setUp(self):
        self.continent = Continent("Africa")


    def test_continent_has_name(self):
        self.assertEqual('Africa', self.continent.name)

    