from db.run_sql import run_sql
from models.continent import Continent
from models.country import Country


def save(continent):
    sql = "INSERT INTO continents(name, visited) VALUES ( %s, %s ) RETURNING id"
    values = [continent.name, continent.visited]
    results = run_sql( sql, values )
    continent.id = results[0]['id']
    return continent


def select_all():
    continents = []

    sql = "SELECT * FROM continents"
    results = run_sql(sql)

    for row in results:
        continent = Continent(row['name'], row['visited'], row['id'])
        continents.append(continent)
    return continents


def select(id):
    continent = None
    sql = "SELECT * FROM continents WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        continent = Continent(result['name'], result['visited'], result['id'] )
    return continent


def countries(continent):
    countries = []

    sql = "SELECT countries.* FROM countries INNER JOIN continents ON continents.id = country.id WHERE continent_id = %s"
    values = [continent.id]
    results = run_sql(sql, values)

    for row in results:
        country = Country(row['name'], row['continent_id'], row['visited'], row['id'])
        countries.append(country)

    return countries


def delete_all():
    sql = "DELETE FROM continents"
    run_sql(sql)