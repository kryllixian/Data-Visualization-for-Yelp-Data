#!/usr/bin/python
import json
import mysql.connector


def connect_to_mysql(url, port, username, password, database):
    # Create DB connection
    conn = mysql.connector.connect(host=url, port=port, user=username, passwd=password, db=database)

    # Prepare a cursor
    cursor = conn.cursor()

    return conn


def readfile_business(conn, filename):
    f = open(filename, 'r')

    # Traverse the file
    while 1:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        data = json.loads(line)

        # Prepare the data
        business_id = data['business_id'].strip()
        name = data['name'].strip()
        address = data['address'].strip().replace('\n', '\t')
        city = data['city'].strip()
        state = data['state'].strip()
        latitude = data['latitude']
        longitude = data['longitude']
        stars = data['stars']
        review_count = data['review_count']
        type = data['type'].strip()
        neighborhood = data['neighborhood'].strip()

        # Insert into businesses
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO businesses
                        (business_id, name, address, city, state, latitude, longitude, stars, review_count, type, neighborhood)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """, (business_id, name, address, city, state, latitude, longitude, stars, review_count, type, neighborhood))
            conn.commit()
        except mysql.connector.Error as e:
            print "Error code:", e.errno        # error number
            print "SQLSTATE value:", e.sqlstate # SQLSTATE value
            print "Error message:", e.msg       # error message
            print "Error:", e                   # errno, sqlstate, msg values
            s = str(e)
            print "Error:", s                   # errno, sqlstate, msg values
            conn.rollback()

        # Insert into categories
        categories = data['categories']
        if categories:
            for item in categories:
                try:
                    cur = conn.cursor()
                    cur.execute("""
                                INSERT INTO categories
                                (business_id, name)
                                VALUES (%s, %s);
                                """, (business_id, item))
                    conn.commit()
                except mysql.connector.Error as e:
                    print "Error code:", e.errno        # error number
                    print "SQLSTATE value:", e.sqlstate # SQLSTATE value
                    print "Error message:", e.msg       # error message
                    print "Error:", e                   # errno, sqlstate, msg values
                    s = str(e)
                    print "Error:", s                   # errno, sqlstate, msg values
                    conn.rollback()

        # # Insert into attributes
        attributes = data['attributes']
        if attributes:
            for item in attributes:
                name = item.split(': ')[0]
                value = item.split(': ')[1]
                try:
                    cur = conn.cursor()
                    cur.execute("""
                                INSERT INTO attributes
                                (business_id, name, value)
                                VALUES (%s, %s, %s);
                                """, (business_id, name, value))
                    conn.commit()
                except mysql.connector.Error as e:
                    print "Error code:", e.errno        # error number
                    print "SQLSTATE value:", e.sqlstate # SQLSTATE value
                    print "Error message:", e.msg       # error message
                    print "Error:", e                   # errno, sqlstate, msg values
                    s = str(e)
                    print "Error:", s                   # errno, sqlstate, msg values
                    conn.rollback()


def readfile_user(conn, filename):
    f = open(filename, 'r')

    # Traverse the file
    while 1:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        data = json.loads(line)

        # Prepare the data
        user_id             = data['user_id'].strip()
        name                = data['name'].strip()
        review_count        = data.get('review_count', 0)
        yelping_since       = data['yelping_since'].strip()
        num_fans            = data.get('fans', 0)
        average_stars       = data['average_stars']
        type                = data['type'].strip()

        # Compliments
        if 'compliments' in data:
            num_compliment_hot      = data['compliments'].get('hot', 0)
            num_compliment_more     = data['compliments'].get('more', 0)
            num_compliment_profile  = data['compliments'].get('profile', 0)
            num_compliment_cute     = data['compliments'].get('cute', 0)
            num_compliment_list     = data['compliments'].get('list', 0)
            num_compliment_note     = data['compliments'].get('note', 0)
            num_compliment_plain    = data['compliments'].get('plain', 0)
            num_compliment_cool     = data['compliments'].get('cool', 0)
            num_compliment_funny    = data['compliments'].get('funny', 0)
            num_compliment_writer   = data['compliments'].get('writer', 0)
            num_compliment_photos   = data['compliments'].get('photos', 0)
        else :
            num_compliment_hot      = 0
            num_compliment_more     = 0
            num_compliment_profile  = 0
            num_compliment_cute     = 0
            num_compliment_list     = 0
            num_compliment_note     = 0
            num_compliment_plain    = 0
            num_compliment_cool     = 0
            num_compliment_funny    = 0
            num_compliment_writer   = 0
            num_compliment_photos   = 0

        # votes
        if 'votes' in data:
            num_votes_useful  = data['votes'].get('useful', 0)
            num_votes_funny   = data['votes'].get('funny', 0)
            num_votes_cool    = data['votes'].get('cool', 0)
        else:
            num_votes_useful  = 0
            num_votes_funny   = 0
            num_votes_cool    = 0

        # Insert into users
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO users
                        (user_id, name, review_count, yelping_since, num_fans, average_stars, type,
                         num_compliment_hot, num_compliment_more, num_compliment_profile, num_compliment_cute,
                         num_compliment_list, num_compliment_note, num_compliment_plain, num_compliment_cool,
                         num_compliment_funny, num_compliment_writer, num_compliment_photos, num_votes_useful,
                         num_votes_funny, num_votes_cool)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """,
                        (user_id, name, review_count, yelping_since, num_fans, average_stars, type,
                         num_compliment_hot, num_compliment_more, num_compliment_profile, num_compliment_cute,
                         num_compliment_list, num_compliment_note, num_compliment_plain, num_compliment_cool,
                         num_compliment_funny, num_compliment_writer, num_compliment_photos, num_votes_useful,
                         num_votes_funny, num_votes_cool))
            conn.commit()
        except mysql.connector.Error as e:
            print "Error code:", e.errno  # error number
            print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
            print "Error message:", e.msg  # error message
            print "Error:", e  # errno, sqlstate, msg values
            s = str(e)
            print "Error:", s  # errno, sqlstate, msg values
            conn.rollback()

        # # Insert into friends
        if 'friends' in data:
            friends = data['friends']
            for friend_id in friends:
                # Ensure user_id1 < user_id2
                if friend_id > user_id:
                    user_id1 = user_id
                    user_id2 = friend_id
                else:
                    user_id1 = friend_id
                    user_id2 = user_id
                try:
                    cur = conn.cursor()
                    cur.execute("""
                                INSERT INTO friends
                                (user_id1, user_id2)
                                 VALUES (%s, %s);
                                """,
                                (user_id1, user_id2))
                    conn.commit()
                except mysql.connector.Error as e:
                    # print "Error code:", e.errno  # error number
                    # print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
                    # print "Error message:", e.msg  # error message
                    # print "Error:", e  # errno, sqlstate, msg values
                    # s = str(e)
                    # print "Error:", s  # errno, sqlstate, msg values
                    # conn.rollback()
                    a = 1

        # Insert into elites
        if 'elite' in data:
            elites = data['elite']
            for year in elites:
                if year.isnumeric():
                    try:
                        cur = conn.cursor()
                        cur.execute("""
                                    INSERT INTO elites
                                    (user_id, year)
                                     VALUES (%s, %s);
                                    """,
                                    (user_id, year))
                        conn.commit()
                    except mysql.connector.Error as e:
                        # print "Error code:", e.errno  # error number
                        # print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
                        # print "Error message:", e.msg  # error message
                        # print "Error:", e  # errno, sqlstate, msg values
                        s = str(e)
                        # print "Error:", s  # errno, sqlstate, msg values
                        # conn.rollback()


def readfile_review(conn, filename):
    f = open(filename, 'r')

    # Traverse the file
    while 1:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        data = json.loads(line)

        review_id   = data['review_id'].strip()
        user_id     = data['user_id'].strip()
        business_id = data['business_id'].strip()
        stars       = data.get('stars', 0)
        date        = data['date']
        text        = data['text'].strip().replace('\n', '\t')
        type        = data['type']

        num_useful  = data.get('useful', 0)
        num_funny   = data.get('funny', 0)
        num_cool    = data.get('cool', 0)

        # Insert into reviews
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO reviews
                        (review_id, user_id, business_id, stars, date, text, num_useful, num_funny, num_cool, type)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """,
                        (review_id, user_id, business_id, stars, date, text, num_useful, num_funny, num_cool, type))
            conn.commit()
        except mysql.connector.Error as e:
            # print "Error code:", e.errno  # error number
            # print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
            # print "Error message:", e.msg  # error message
            # print "Error:", e  # errno, sqlstate, msg values
            # s = str(e)
            # print "Error:", s  # errno, sqlstate, msg values
            conn.rollback()


def readfile_checkin(conn, filename):
    f = open(filename, 'r')

    # Traverse the file
    while 1:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        data = json.loads(line)

        business_id = data['business_id'].strip()
        type        = data['type']

        if 'time' in data:
            times = data['time']
            for item in times:
                num_checkins = item.split(':')[1]
                day = item.split(':')[0].split('-')[0]
                hour = item.split(':')[0].split('-')[1]
                # Insert into checkins
                try:
                    cur = conn.cursor()
                    cur.execute("""
                                INSERT INTO checkins
                                (business_id, day, hour, num_checkins, type)
                                VALUES (%s, %s, %s, %s, %s);
                                """,
                                (business_id, day, hour, num_checkins, type))
                    conn.commit()
                except mysql.connector.Error as e:
                    print "Error code:", e.errno  # error number
                    print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
                    print "Error message:", e.msg  # error message
                    print "Error:", e  # errno, sqlstate, msg values
                    s = str(e)
                    print "Error:", s  # errno, sqlstate, msg values
                    conn.rollback()


def readfile_tip(conn, filename):
    f = open(filename, 'r')

    # Traverse the file
    while 1:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        data = json.loads(line)

        business_id = data['business_id'].strip()
        user_id     = data['user_id'].strip()
        text        = data['text'].strip().replace('\n', '\t')
        date        = data['date'].strip()
        num_likes   = data.get('likes', 0)
        type        = data['type']

        # Insert into reviews
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO tips
                        (business_id, user_id, text, date, num_likes, type)
                        VALUES (%s, %s, %s, %s, %s, %s);
                        """,
                        (business_id, user_id, text, date, num_likes, type))
            conn.commit()
        except mysql.connector.Error as e:
            print "Error code:", e.errno  # error number
            print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
            print "Error message:", e.msg  # error message
            print "Error:", e  # errno, sqlstate, msg values
            s = str(e)
            print "Error:", s  # errno, sqlstate, msg values
            conn.rollback()


def add_count_review(conn, filename):
    f = open(filename, 'r')

    # Traverse the file
    while 1:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        data = json.loads(line)
        num_useful  = data.get('useful', 0)
        num_funny   = data.get('funny', 0)
        num_cool    = data.get('cool', 0)

        # Update counts
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO reviews
                        (review_id, user_id, business_id, stars, date, text, num_useful, num_funny, num_cool, type)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """,
                        (review_id, user_id, business_id, stars, date, text, num_useful, num_funny, num_cool, type))
            conn.commit()
        except mysql.connector.Error as e:
            print "Error code:", e.errno  # error number
            print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
            print "Error message:", e.msg  # error message
            print "Error:", e  # errno, sqlstate, msg values
            s = str(e)
            print "Error:", s  # errno, sqlstate, msg values
            conn.rollback()



def main():
    conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data_new")
    # readfile_business(conn, 'yelp-data-new/business.json')
    # readfile_user(conn, 'yelp-data-new/user.json')
    readfile_review(conn, 'yelp-data-new/review.json')
    # readfile_tip(conn, 'yelp-data-new/tip.json')
    # readfile_checkin(conn, 'yelp-data-new/checkin.json')

    conn.close()


if __name__ == "__main__":
    main()
