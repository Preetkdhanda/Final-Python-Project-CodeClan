DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS continents;

CREATE TABLE continents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN
);


CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent INT REFERENCES continents(id) ON DELETE CASCADE,
    visited BOOLEAN

);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    country INT REFERENCES countries(id) ON DELETE CASCADE,
    continent INT REFERENCES continents(id) ON DELETE CASCADE
    

);