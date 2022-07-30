import pdb
from models.country import Country
from models.continent import Continent
from models.city import City

import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
continent_repository.delete_all()
country_repository.delete_all()


continent=Continent("Africa")
continent_repository.save(continent)
continent1=Continent("Europe")
continent_repository.save(continent1)
continent2=Continent("Asia")
continent_repository.save(continent2)
continent3=Continent("North America")
continent_repository.save(continent3)
continent4=Continent("South America")
continent_repository.save(continent4)
continent5=Continent("Australia")
continent_repository.save(continent5)
continent6=Continent("Antartica")
continent_repository.save(continent6)

country=Country("South Africa", continent, False)
country_repository.save(country)
