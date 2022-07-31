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
    return render_template("cities/index.html", cities=cities)

@cities_blueprint.route("/cities/<id>")
def show(id):
    country = country_repository.select(id)
    continent = continent_repository.continent(country)
    return render_template("cities/show.html", country=country, continent=continent)