from db.run_sql import run_sql

from models.continent import Continent
from models.country import Country

def save(country):
    sql = "INSERT INTO countries ( name, continent_id) VALUES ( %s, %s) RETURNING id"
    values = [country.name, country.continent_id]
    results = run_sql( sql, values )
    country.id = results[0]['id']
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['visited'], row['continent_id'], row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    
    if results:
        result = results[0]
        country = Country(result['name'], result['visited'], result['country_id'], result['id'] )
    return country


def continents(city):
    continents = []

    sql = "SELECT continents.* FROM continents INNER JOIN countries ON countries.id = continents.id WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        continent = Continent(row['name'], row['visited'], row['id'])
        continents.append(continent)

    return continents


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)