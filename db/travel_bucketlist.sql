DROP TABLE cities;
DROP TABLE countries;
DROP TABLE continents;

CREATE TABLE continents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN
);


CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    continent_id INT REFERENCES continents(id)

);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id),
    continent_id INT REFERENCES continents(id)
    

);