import pdb
from models.country import Country
from models.continent import Continent
from models.city import City

import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()
continent_repository.delete_all()



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

country=Country("South Africa", continent)
country_repository.save(country)
country2=Country("Nigeria", continent)
country_repository.save(country2)
country3=Country("Kenya", continent)
country_repository.save(country3)
country4=Country("Ghana", continent)
country_repository.save(country4)
country5=Country("Egypt", continent)
country_repository.save(country5)
country6=Country("USA", continent3)
country_repository.save(country6)
country7=Country('Brazil', continent4)
country_repository.save(country7)

city=City('New York',country6, continent3)
city_repository.save(city)
city1=City('Rio De Janerio', country7, continent4)
city_repository.save(city1)
city=City("Cape Town", country, continent)
city_repository.save(city)
city=City('San Francisco',country6, continent3)
city_repository.save(city)
city=City('Houston',country6, continent3)
city_repository.save(city)
city=City('Chicago',country6, continent3)
city_repository.save(city)
city=City('Las Vegas',country6, continent3)
city_repository.save(city)
city1=City('Sao Paulo', country7, continent4)
city_repository.save(city1)
city=City("Johannesburg", country, continent)
city_repository.save(city)
city=City("Accra", country4, continent)
city_repository.save(city)

