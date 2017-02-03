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

-- Average Stars Given by Users in Pittsburgh
SELECT COUNT(u.user_id)
FROM businesses b, reviews r, users u
WHERE b.latitude >= 40 AND b.latitude <= 41 AND
      b.longitude >= -81 AND b.longitude <= -79 AND
      r.business_id = b.business_id AND r.user_id = u.user_id AND
      average_stars >= 1.0 AND average_stars < 1.5;
