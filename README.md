# Data-Visualization-for-Yelp-Data
Data Visualization for Yelp Data

server.js:
The javascript file using express framework to handle all requests.

model.js:
All useful functions needed to have access to database directly.

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

get_review_of_top_categories.pu:
Get the reviews of several popular categories.

get_review_text_restaurants_pittsburgh.py:
Get the review text from all restaurants in Pittsburgh from Database.

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

views/restaurants_recommendation_by_name:
Use restaurant name and key words to give users recommendation of restaurants.
