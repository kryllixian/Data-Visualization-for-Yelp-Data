-- Business
-- Loaded
CREATE TABLE IF NOT EXISTS businesses (
    business_id VARCHAR(80) NOT NULL,
    name VARCHAR(80),
    address VARCHAR(200),
    city VARCHAR(80),
    state VARCHAR(80),
    latitude FLOAT,
    longitude FLOAT,
    stars FLOAT,
    review_count INT,
    type VARCHAR(80),
    neighborhood VARCHAR(80),
    PRIMARY KEY(business_id)
);

-- Loaded
CREATE TABLE IF NOT EXISTS attributes (
    business_id VARCHAR(80) NOT NULL,
    name VARCHAR(80) NOT NULL,
    value VARCHAR(80),
    PRIMARY KEY(business_id, name),
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);

-- Loaded
CREATE TABLE IF NOT EXISTS categories (
    business_id VARCHAR(80) NOT NULL,
    name VARCHAR(80),
    PRIMARY KEY(business_id, name),
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);
--
-- -- Loaded
-- CREATE TABLE IF NOT EXISTS neighborhoods (
--     business_id VARCHAR(80) NOT NULL,
--     name VARCHAR(80) NOT NULL,
--     PRIMARY KEY(business_id, name),
--     FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
-- );


CREATE TABLE IF NOT EXISTS hours (
);


-- User
-- Loaded
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(80) NOT NULL,
    name VARCHAR(80),
    review_count INT,
    yelping_since DATE,
    num_fans INT,
    average_stars FLOAT,
    type VARCHAR(80),
    num_votes_useful INT,
    num_votes_funny INT,
    num_votes_cool INT,
    num_compliment_hot INT,
    num_compliment_more INT,
    num_compliment_profile INT,
    num_compliment_cute INT,
    num_compliment_list INT,
    num_compliment_note INT,
    num_compliment_plain INT,
    num_compliment_cool INT,
    num_compliment_funny INT,
    num_compliment_writer INT,
    num_compliment_photos INT,
    PRIMARY KEY(user_id)
);

-- Sort the ids, smaller id comes first then bigger one
-- Assume friends are mutual
-- Loaded
CREATE TABLE IF NOT EXISTS friends (
    user_id1 VARCHAR(80) NOT NULL,
    user_id2 VARCHAR(80) NOT NULL,
    PRIMARY KEY(user_id1, user_id2),
    FOREIGN KEY(user_id1) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(user_id2) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Loaded
CREATE TABLE IF NOT EXISTS elites (
    user_id VARCHAR(80) NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY(user_id, year),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
);


-- Review
-- Loaded
CREATE TABLE IF NOT EXISTS reviews (
    review_id VARCHAR(80) NOT NULL,
    user_id VARCHAR(80) NOT NULL,
    business_id VARCHAR(80) NOT NULL,
    stars FLOAT,
    date DATE,
    text TEXT,
    useful INT,
    funny INT,
    cool INT,
    type VARCHAR(80),
    PRIMARY KEY(review_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);


-- Checkin
CREATE TABLE IF NOT EXISTS checkins (
    checkin_id INT NOT NULL AUTO_INCREMENT,
    business_id VARCHAR(80) NOT NULL,
    day VARCHAR(10),
    hour INT,
    num_checkins INT,
    type VARCHAR(80),
    PRIMARY KEY(checkin_id),
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);


-- Tip
-- Loaded
CREATE TABLE IF NOT EXISTS tips (
    tip_id INT NOT NULL AUTO_INCREMENT,
    business_id VARCHAR(80) NOT NULL,
    user_id VARCHAR(80) NOT NULL,
    text TEXT,
    date DATE,
    likes INT,
    type VARCHAR(80),
    PRIMARY KEY(tip_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);
