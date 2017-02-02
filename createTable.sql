-- Business
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
    PRIMARY KEY(business_id)
);

CREATE TABLE IF NOT EXISTS attributes (
    business_id VARCHAR(80) NOT NULL,
    name VARCHAR(80) NOT NULL,
    value VARCHAR(80),
    PRIMARY KEY(business_id, name),
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS categories (
    business_id VARCHAR(80) NOT NULL,
    name VARCHAR(80),
    PRIMARY KEY(business_id, name),
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS neighborhoods (
    business_id VARCHAR(80) NOT NULL,
    name VARCHAR(80) NOT NULL,
    PRIMARY KEY(business_id, name),
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS hours (
);


-- User
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(80) NOT NULL,
    name: VARCHAR(80),
    review_count INT,
    yelping_since DATE,
    useful INT,
    funny INT,
    cool INT,
    fans INT,
    average_stars FLOAT,
    compliment_hot INT,
    compliment_more INT,
    compliment_profile INT,
    compliment_cute INT,
    compliment_list INT,
    compliment_note INT,
    compliment_plain INT,
    compliment_cool INT,
    compliment_funny INT,
    compliment_writer INT,
    compliment_photos INT,
    type VARCHAR(80),
    PRIMARY KEY(user_id)
);

-- Sort the ids, smaller id comes first then bigger one
CREATE TABLE IF NOT EXISTS friends (
    user_id1 VARCHAR(80) NOT NULL,
    user_id2 VARCHAR(80) NOT NULL,
    PRIMARY KEY(user_id1, user_id2),
    FOREIGN KEY(user_id1) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(user_id2) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS elites (
    user_id VARCHAR(80) NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY(user_id, year),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
);


-- Review
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
    business_id VARCHAR(80) NOT NULL,
    time VARCHAR(80),
    type VARCHAR(80),
    PRIMARY KEY(business_id, time),
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);


-- Tip
CREATE TABLE IF NOT EXISTS tips (
    business_id VARCHAR(80) NOT NULL,
    user_id VARCHAR(80) NOT NULL,
    text TEXT,
    date DATE,
    likes INT,
    type VARCHAR(80),
    PRIMARY KEY(business_id, user_id, date)
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);
