from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all() 
    return render_template("countries/index.html", countries=countries)

@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    continents = continent_repository.select_all()
    return render_template("countries/new.html", continents=continents)

@countries_blueprint.route("/countries",  methods=['POST'])
def add_to_bucketlist():
    country_name       = request.form['country']
    continent_id    = request.form['continent_id']
    visited   = request.form['visited']
    continent       = (continent_repository.select(continent_id))
    country     = Country(country_name, visited, continent)
    country_repository.save(country)
    return redirect('/countries')