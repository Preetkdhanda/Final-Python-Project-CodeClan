from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all() 
    return render_template("cities/show.html", cities=cities)

@cities_blueprint.route("/cities/<id>")
def show(id):
    id = city_repository.select(id)
    return render_template("cities/index.html")

@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    continents = continent_repository.select_all()
    countries = country_repository.select_all()
    return render_template("cities/new.html", continents=continents, countries = countries)

# @cities_blueprint.route("/cities", methods=['POST'])
# def add_city():
#     city_name = request.form['city']
#     continent_id = request.form['continents_id']
#     country_id= request.form['countries_id']
#     continent = continent_repository.select(continent_id)
#     country = country_repository.select(country_id)

#     city = City (city_name, country, continent, False)
#     city_repository.save(city)
#     return redirect('/cities')
    

@cities_blueprint.route("/cities",  methods=['POST'])
def add_to_bucketlist():
    city_name       = request.form['city']
    continent_id    = request.form['continent_id']
    country    = request.form['country_id']
    visited   = request.form['visited']
    continent       = (continent_repository.select(continent_id))
    city      = City(city_name, visited, country, continent)
    city_repository.save(city)
    return redirect('/cities')