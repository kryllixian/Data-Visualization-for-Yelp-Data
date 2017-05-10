# Data-Visualization-for-Yelp-Data
Data Visualization for Yelp Data


----------------------------------------------------------------------------------
How to set up the server:
1) Download the Node.js installer and install from:
https://nodejs.org/en/download/
or on Linux:
sudo apt-get install nodejs
sudo apt-get install npm

2) Verify that Node.js was properly installed or not:
node -v

3) Upgrade current npm version:
sudo npm install npm --global

4) Install all required packages:
npm install

5) After all the data have been imported into database, run the following scripts to generate data files:
python get_review_text_with_separate_lins_pittsburgh.py
python get_review_text_restaurants_pittsburgh.py
python get_business_stars_pittsburgh.py
python get_all_attributes.py
python group_attributes_by_business_id.py

5) Start the server with the default port as 3000:
node server.js
----------------------------------------------------------------------------------


----------------------------------------------------------------------------------
How to load the data into database:
1) Download the data from:
https://www.yelp.com/dataset_challenge

2) Install python mysql.connector, here is the command using pip:
pip install mysql-connector

3) Download MySQL from, then install:
https://dev.mysql.com/downloads/mysql/

4) Update the host, user, password, database in server.js and all python scripts according to your server.

5) Use SQL statements in createTable.sql

5) Run python script load_mysql.py to load the JOSN files downloaded from the link above into mysql


----------------------------------------------------------------------------------
server.js:
The javascript file using express framework to handle all requests.

model.js:
All useful functions needed to have access to database directly. Usually we import
this file in server.js and then use the functions in model.js.

helper.js:
Other useful functions in backend.

createTable.sql:
SQL statements used to create Tables in MySQL database.

filter-pittsburgh.py:
Get all useful data in Pittsburgh from database.

get_all_attrubutes.py:
Get all attributes of a business according to the data.

get_business_stars_pittsburgh.py:
Get the business_id, name, and stars from data in Pittsburgh.

get_review_of_top_categories.py:
Get the reviews of several popular categories.

get_review_text_restaurants_pittsburgh.py:
Get the review text from all restaurants in Pittsburgh from Database the reviews of the same restaurants are in the same row.

get_review_text_restaurants_with_separate_lines_pittsburgh.py:
Get the review text from all restaurants in Pittsburgh from Database, different reviews are in different rows

group_attributes_by_business_id.py:
Group the attributes according to their business_id from the data in database.

load_mysql.py:
Load the data from JSON file into MySQL database.

load-into-database.py:
Load the data form JSON file into MongoDB database.

loadIntoAWS.py:
Used in AWS servers, insert the data to database from exported files.

queries.sql:
Some commonly used SQL queries to have access to the database in MySQL database.

public/css/style.css:
All local CSS are in the file.

views/restaurants_recommendation_by_name.hbs:
Use restaurant name and key words to give users recommendation of restaurants.
