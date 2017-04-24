-- CREATE indexes
CREATE INDEX review_business_id ON reviews(business_id);
CREATE INDEX category_name_index ON categories(name);
CREATE INDEX latitude_index ON businesses(latitude);
CREATE INDEX longitude_index ON businesses(longitude);
CREATE INDEX review_user_id ON reviews(user_id);

-- Distribution of Stars of Business in Pittsburgh
SELECT COUNT(*)
FROM businesses
WHERE latitude >= 40 AND latitude <= 41 AND
      longitude >= -81 AND longitude <= -79 AND
      stars = 1.0;

-- Distribution of Review Count of Business in Pittsburgh
SELECT MIN(review_count), AVG(review_count), MAX(review_count)
FROM businesses
WHERE latitude >= 40 AND latitude <= 41 AND
      longitude >= -81 AND longitude <= -79;

SELECT COUNT(business_id)
FROM businesses
WHERE latitude >= 40 AND latitude <= 41 AND
      longitude >= -81 AND longitude <= -79 AND
      review_count >= 0 AND review_count < 9;

-- Distribution of cities of businesses in Pittsburgh
SELECT DISTINCT(city), COUNT(city)
FROM businesses
WHERE latitude >= 40 AND latitude <= 41 AND
      longitude >= -81 AND longitude <= -79
GROUP BY city
ORDER BY city;

-- Distribution of neighborhoods of businesses in Pittsburgh
SELECT DISTINCT(n.name), COUNT(n.name)
FROM businesses b, neighborhoods n
WHERE latitude >= 40 AND latitude <= 41 AND
      longitude >= -81 AND longitude <= -79 AND
      b.business_id = n.business_id
GROUP BY name
ORDER BY name;

-- Distribution of stars of Reviews of Businesses in Pittsburgh
SELECT COUNT(r.review_id)
FROM businesses b, reviews r
WHERE b.latitude >= 40 AND b.latitude <= 41 AND
      b.longitude >= -81 AND b.longitude <= -79 AND
      r.business_id = b.business_id AND r.stars = 1;

-- Distribution of Date of Reviews
SELECT YEAR(date), COUNT(review_id)
FROM businesses b, reviews r
WHERE b.latitude >= 40 AND b.latitude <= 41 AND
      b.longitude >= -81 AND b.longitude <= -79 AND
      r.business_id = b.business_id AND r.stars = 1
GROUP BY YEAR(date)
ORDER BY YEAR(date);

SELECT MONTH(date), COUNT(review_id)
FROM businesses b, reviews r
WHERE b.latitude >= 40 AND b.latitude <= 41 AND
      b.longitude >= -81 AND b.longitude <= -79 AND
      r.business_id = b.business_id AND r.stars = 1
GROUP BY MONTH(date)
ORDER BY MONTH(date);

-- Average Stars Given by Users in Pittsburgh
SELECT COUNT(u.user_id)
FROM businesses b, reviews r, users u
WHERE b.latitude >= 40 AND b.latitude <= 41 AND
      b.longitude >= -81 AND b.longitude <= -79 AND
      r.business_id = b.business_id AND r.user_id = u.user_id AND
      u.average_stars >= 1.0 AND u.average_stars < 1.5;

-- -- Users and Number of Friends
-- SELECT u.user_id, COUNT(u.user_id)
-- FROM businesses b, reviews r, users u, friends f
-- WHERE b.latitude >= 40 AND b.latitude <= 41 AND
--       b.longitude >= -81 AND b.longitude <= -79 AND
--       r.business_id = b.business_id AND r.user_id = u.user_id AND
--       (f.user_id1 = u.user_id OR f.user_id2 = u.user_id)
-- GROUP BY u.user_id
-- ORDER BY COUNT(u.user_id);

-- Number of Fans for Each User
SELECT MIN(u.fans), AVG(u.fans), MAX(u.fans)
FROM businesses b, reviews r, users u
WHERE b.latitude >= 40 AND b.latitude <= 41 AND
      b.longitude >= -81 AND b.longitude <= -79 AND
      r.business_id = b.business_id AND r.user_id = u.user_id;


SELECT COUNT(u.user_id)
FROM businesses b, reviews r, users u
WHERE b.latitude >= 40 AND b.latitude <= 41 AND
      b.longitude >= -81 AND b.longitude <= -79 AND
      r.business_id = b.business_id AND r.user_id = u.user_id AND
      u.fans >= 100;


-- Get reviews for a category
SELECT r.review_id, r.text
FROM businesses b, reviews r, categories c
WHERE b.latitude >= 40 AND b.latitude <= 41 AND
      b.longitude >= -81 AND b.longitude <= -79 AND
      c.name = 'Restaurants' AND r.business_id = b.business_id AND
      c.business_id = b.business_id;


-- Get reviews in restaurants
SELECT r.review_id, r.text
FROM businesses b, reviews r, categories c
WHERE c.name = 'Restaurants' AND r.business_id = b.business_id AND
      c.business_id = b.business_id;

SELECT * FROM (
    SELECT * FROM businesses
    WHERE latitude >= 40 AND latitude <= 41 AND
          longitude >= -81 AND longitude <= -79
) b LEFT JOIN attributes a
    ON b.business_id = a.business_id
    ORDER BY stars DESC, review_count DESC
    LIMIT 20;



-- Create index
CREATE INDEX ATTR_INDEX ON Attributes(attribute);

CREATE INDEX VALUE_INDEX ON Attributes(value);


SELECT business_id, name, review_count FROM businesses
WHERE latitude >= 40 AND latitude <= 41 AND
      longitude >= -81 AND longitude <= -79
ORDER BY review_count DESC LIMIT 10;



-- Get all restaurants in Pittsburgh
SELECT b.business_id FROM businesses b, categories c
WHERE b.latitude >= 40 AND b.latitude <= 41 AND
      b.longitude >= -81 AND b.longitude <= -79 AND
      b.business_id = c.business_id AND c.name = 'Restaurants';

-- Given a restaurant, recommend other restaurants by number of users reviewed both of them
SELECT b.business_id, b.name, b.address, b.city, b.state, b.latitude, b.longitude, b.stars, b.review_count, b.type, b.neighborhood, COUNT(DISTINCT(u.user_id)) AS COUNT
FROM reviews r1, reviews r2, users u, businesses b
WHERE r1.business_id = 'JLbgvGM4FXh9zNP4O5ZWjQ' AND r2.business_id != r1.business_id AND
      r1.user_id = u.user_id AND r2.user_id = u.user_id AND r2.business_id = b.business_id
GROUP BY b.business_id, b.name, b.address, b.city, b.state, b.latitude, b.longitude, b.stars, b.review_count, b.type, b.neighborhood
ORDER BY COUNT(DISTINCT(u.user_id)) DESC, b.stars DESC, b.review_count DESC LIMIT 10;


SELECT review_id, (LENGTH(text) - LENGTH(replace(text ,'great','')))/LENGTH('great') AS COUNT
FROM reviews
GROUP BY review_id
ORDER BY COUNT DESC LIMIT 10;


SELECT b.business_id, (
    SELECT r.review_id, SUM(CASE WHEN r.text LIKE '%great%' THEN 1 ELSE 0 END)
    FROM reviews r
    WHERE r.business_id = b.business_id
    GROUP BY r.review_id
) AS COUNT
FROM businesses b
ORDER BY COUNT DESC LIMIT 10;
