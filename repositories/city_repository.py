from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.continent import Continent
import repositories.continent_repository as continent_repository
import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT INTO cities (name, country_id, continent_id, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.continent.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city



def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        continent = continent_repository.select(result['id'])
        country = country_repository.select(result['id'])
        City = City(result['name'],country, continent,result['visited'], result['id'] )
    return city


def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        continent = continent_repository.select(row['continent_id'])
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, continent, row['visited'], row['id'])
        cities.append(city)
    return cities


def country(city):
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [city.country.id]
    results = run_sql(sql, values)[0]
    country = Country(results['name'], results['country_id'], results['continent_id'], results['visited'],results['id'])
    return country


def continent(city):
    sql = "SELECT * FROM continent WHERE id = %s"
    values = [city.continent.id]
    results = run_sql(sql, values)[0]
    continent = Continent(results['name'], results['id'])
    return continent


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET (name, visited, country_id, continent_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [city.name, city.visited, city.country.id, city.continent.id]
    run_sql(sql, values)