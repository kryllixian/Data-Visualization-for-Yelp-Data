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
    PRIMARY KEY(business_id)
);

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

-- Loaded
CREATE TABLE IF NOT EXISTS neighborhoods (
    business_id VARCHAR(80) NOT NULL,
    name VARCHAR(80) NOT NULL,
    PRIMARY KEY(business_id, name),
    FOREIGN KEY(business_id) REFERENCES businesses(business_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS hours (
);


-- User
-- Loaded
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(80) NOT NULL,
    name VARCHAR(80),
    review_count INT,
    yelping_since_year INT,
    yelping_since_month INT,
    fans INT,
    average_stars FLOAT,
    type VARCHAR(80),
    PRIMARY KEY(user_id)
);

-- Loaded
CREATE TABLE IF NOT EXISTS votes (
    user_id VARCHAR(80) NOT NULL,
    useful INT,
    funny INT,
    cool INT,
    PRIMARY KEY(user_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Loaded
CREATE TABLE IF NOT EXISTS compliments (
    user_id VARCHAR(80) NOT NULL,
    hot INT,
    more INT,
    profile INT,
    cute INT,
    list INT,
    note INT,
    plain INT,
    cool INT,
    funny INT,
    writer INT,
    photos INT,
    PRIMARY KEY(user_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
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
    business_id VARCHAR(80) NOT NULL,
    day INT,
    hour INT,
    checkin_number INT,
    type VARCHAR(80),
    PRIMARY KEY(business_id, day, hour),
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
