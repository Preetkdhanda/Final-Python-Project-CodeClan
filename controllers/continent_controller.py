from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
from models.continent import Continent
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository

continents_blueprint = Blueprint("continents", __name__)

@continents_blueprint.route("/continents")
def continents():
    continents = continent_repository.select_all() 
    return render_template("continents/index.html", continents=continents)

