#Project_Travel_Bucketlist

This application allows user to track their travel bucketlist. The user of this application can add cities and countries they would like to visit. It further allows them to be able to mark if they have visited that particular place or they are still waiting to go. It also allows users to remove the destination off their bucketlist.

The application has been tested. Results of the test can be found here: https://img.shields.io/badge/Ran%208%20tests%20in%200.000s-OK-green


This application uses the following: Python3, Flask, SQL, HTML and CSS.

In order to use the application the following must be done:

1) Create database - createdb travel_bucketlist
2) Create the tables and columns for the database which are the following:
    City - Name, Country, Continent, Visited, ID
    Country - Name, Continent, Visited, ID
    Continent - Name, Visited, ID
    
    You must drop the databases in this order for the application to run and create the tables in the order of continent, country, city.

3) Run database - psql -d travel_bucketlist -f db/travel_bucketlist.sql
4) Run the command python3 run_tests.py to ensure all tests pass.
5) Run the command python3 console.py to ensure the data is added to the database.
6) Run the command flask run.
7) Open browser to http://localhost:5000/
8) Browse application

For further support contact Harpreet Dhanda CodeClan.

I would like to acknowledge Ally McGilloway, Ashley Healy, Ben Roberts and Aqib Javaid for their support in this project. Alongside Alejandro Carino Garcia for his continued support too.

This project is an opensource project which contributions are welcome.
