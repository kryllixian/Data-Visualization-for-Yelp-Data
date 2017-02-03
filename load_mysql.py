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
        business_id = data['business_id']
        name = data['name']
        address = data['full_address'].replace('\n', '\t')
        city = data['city']
        state = data['state']
        latitude = data['latitude']
        longitude = data['longitude']
        stars = data['stars']
        review_count = data['review_count']
        type = data['type']

        # # Insert into businesses
        # try:
        #     cur = conn.cursor()
        #     cur.execute("""
        #                 INSERT INTO businesses
        #                 (business_id, name, address, city, state, latitude, longitude, stars, review_count, type)
        #                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        #                 """, (business_id, name, address, city, state, latitude, longitude, stars, review_count, type))
        #     conn.commit()
        # except mysql.connector.Error as e:
        #     print "Error code:", e.errno        # error number
        #     print "SQLSTATE value:", e.sqlstate # SQLSTATE value
        #     print "Error message:", e.msg       # error message
        #     print "Error:", e                   # errno, sqlstate, msg values
        #     s = str(e)
        #     print "Error:", s                   # errno, sqlstate, msg values
        #     conn.rollback()

        # # Insert into categories
        # categories = data['categories']
        # for item in categories:
        #     try:
        #         cur = conn.cursor()
        #         cur.execute("""
        #                     INSERT INTO categories
        #                     (business_id, name)
        #                     VALUES (%s, %s);
        #                     """, (business_id, item))
        #         conn.commit()
        #     except mysql.connector.Error as e:
        #         print "Error code:", e.errno        # error number
        #         print "SQLSTATE value:", e.sqlstate # SQLSTATE value
        #         print "Error message:", e.msg       # error message
        #         print "Error:", e                   # errno, sqlstate, msg values
        #         s = str(e)
        #         print "Error:", s                   # errno, sqlstate, msg values
        #         conn.rollback()

        # # Insert into neighborhoods
        # neighborhoods = data['neighborhoods']
        # for item in neighborhoods:
        #     try:
        #         cur = conn.cursor()
        #         cur.execute("""
        #                     INSERT INTO neighborhoods
        #                     (business_id, name)
        #                     VALUES (%s, %s);
        #                     """, (business_id, item))
        #         conn.commit()
        #     except mysql.connector.Error as e:
        #         print "Error code:", e.errno        # error number
        #         print "SQLSTATE value:", e.sqlstate # SQLSTATE value
        #         print "Error message:", e.msg       # error message
        #         print "Error:", e                   # errno, sqlstate, msg values
        #         s = str(e)
        #         print "Error:", s                   # errno, sqlstate, msg values
        #         conn.rollback()


def num_or_zero(num):
    if not num:
        num = 0
    return num


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
        user_id             = data['user_id']
        name                = data['name']
        review_count        = num_or_zero(data['review_count'])
        yelping_since_year  = data['yelping_since'][0 : 4]
        yelping_since_month = data['yelping_since'][5 : 7]
        fans                = num_or_zero(data['fans'])
        average_stars       = data['average_stars']
        type                = data['type']

        # # Insert into users
        # try:
        #     cur = conn.cursor()
        #     cur.execute("""
        #                 INSERT INTO users
        #                 (user_id, name, review_count, yelping_since_year, yelping_since_month, fans, average_stars, type)
        #                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        #                 """,
        #                 (user_id, name, review_count, yelping_since_year, yelping_since_month, fans, average_stars, type))
        #     conn.commit()
        # except mysql.connector.Error as e:
        #     print "Error code:", e.errno  # error number
        #     print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
        #     print "Error message:", e.msg  # error message
        #     print "Error:", e  # errno, sqlstate, msg values
        #     s = str(e)
        #     print "Error:", s  # errno, sqlstate, msg values
        #     conn.rollback()

        # Insert into votes
        # useful              = num_or_zero(data['votes']['useful'])
        # funny               = num_or_zero(data['votes']['funny'])
        # cool                = num_or_zero(data['votes']['cool'])
        #
        # try:
        #     cur = conn.cursor()
        #     cur.execute("""
        #                 INSERT INTO votes
        #                 (user_id, useful, funny, cool)
        #                 VALUES (%s, %s, %s, %s);
        #                 """,
        #                 (user_id, useful, funny, cool))
        #     conn.commit()
        # except mysql.connector.Error as e:
        #     print "Error code:", e.errno  # error number
        #     print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
        #     print "Error message:", e.msg  # error message
        #     print "Error:", e  # errno, sqlstate, msg values
        #     s = str(e)
        #     print "Error:", s  # errno, sqlstate, msg values
        #     conn.rollback()

        # # Insert into compliments
        # hot      = data['compliments'].get('hot', 0)
        # more     = data['compliments'].get('more', 0)
        # profile  = data['compliments'].get('profile', 0)
        # cute     = data['compliments'].get('cute', 0)
        # list     = data['compliments'].get('list', 0)
        # note     = data['compliments'].get('note', 0)
        # plain    = data['compliments'].get('plain', 0)
        # cool     = data['compliments'].get('cool', 0)
        # funny    = data['compliments'].get('funny', 0)
        # writer   = data['compliments'].get('writer', 0)
        # photos   = data['compliments'].get('photos', 0)
        #
        # try:
        #     cur = conn.cursor()
        #     cur.execute("""
        #                 INSERT INTO compliments
        #                 (user_id, hot, more, profile, cute, list, note, plain, cool, funny, writer, photos)
        #                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        #                 """,
        #                 (user_id, hot, more, profile, cute, list, note, plain, cool, funny, writer, photos))
        #     conn.commit()
        # except mysql.connector.Error as e:
        #     print "Error code:", e.errno  # error number
        #     print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
        #     print "Error message:", e.msg  # error message
        #     print "Error:", e  # errno, sqlstate, msg values
        #     s = str(e)
        #     print "Error:", s  # errno, sqlstate, msg values
        #     conn.rollback()

        # # Insert into friends
        # friends = data['friends']
        # for friend_id in friends:
        #     # Ensure user_id1 < user_id2
        #     if friend_id > user_id:
        #         user_id1 = user_id
        #         user_id2 = friend_id
        #     else:
        #         user_id1 = friend_id
        #         user_id2 = user_id
        #     try:
        #         cur = conn.cursor()
        #         cur.execute("""
        #                     INSERT INTO friends
        #                     (user_id1, user_id2)
        #                      VALUES (%s, %s);
        #                     """,
        #                     (user_id1, user_id2))
        #         conn.commit()
        #     except mysql.connector.Error as e:
        #         # print "Error code:", e.errno  # error number
        #         # print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
        #         # print "Error message:", e.msg  # error message
        #         # print "Error:", e  # errno, sqlstate, msg values
        #         # s = str(e)
        #         # print "Error:", s  # errno, sqlstate, msg values
        #         conn.rollback()

        # Insert into elites
        elites = data['elite']
        for year in elites:
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
                print "Error code:", e.errno  # error number
                print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
                print "Error message:", e.msg  # error message
                print "Error:", e  # errno, sqlstate, msg values
                s = str(e)
                print "Error:", s  # errno, sqlstate, msg values
                conn.rollback()


def readfile_review(conn, filename):
    f = open(filename, 'r')

    # Traverse the file
    while 1:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        data = json.loads(line)

        review_id   = data['review_id']
        user_id     = data['user_id']
        business_id = data['business_id']
        stars       = data.get('stars', 0)
        date        = data['date']
        text        = data['text'].replace('\n', '\t')
        useful      = data['votes'].get('useful', 0)
        funny       = data['votes'].get('funny', 0)
        cool        = data['votes'].get('cool', 0)
        type        = data['type']

        # Insert into reviews
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO reviews
                        (review_id, user_id, business_id, stars, date, text, useful, funny, cool, type)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """,
                        (review_id, user_id, business_id, stars, date, text, useful, funny, cool, type))
            conn.commit()
        except mysql.connector.Error as e:
            print "Error code:", e.errno  # error number
            print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
            print "Error message:", e.msg  # error message
            print "Error:", e  # errno, sqlstate, msg values
            s = str(e)
            print "Error:", s  # errno, sqlstate, msg values
            conn.rollback()


# def readfile_checkins(conn, filename):
#     f = open(filename, 'r')
#
#     # Traverse the file
#     while 1:
#         line = str(f.readline())
#         # If line is null
#         if not line:
#             break
#
#         data = json.loads(line)
#
#         business_id = data['business_id']
#         checkin_info = data['checkin_info']
#         type        = data['type']
#
#         for item in checkin_info:
#
#             # Insert into checkins
#             try:
#                 cur = conn.cursor()
#                 cur.execute("""
#                             INSERT INTO checkins
#                             (business_id, user_id, text, date, likes, type)
#                             VALUES (%s, %s, %s, %s, %s, %s);
#                             """,
#                             (business_id, user_id, text, date, likes, type))
#                 conn.commit()
#             except mysql.connector.Error as e:
#                 print "Error code:", e.errno  # error number
#                 print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
#                 print "Error message:", e.msg  # error message
#                 print "Error:", e  # errno, sqlstate, msg values
#                 s = str(e)
#                 print "Error:", s  # errno, sqlstate, msg values
#                 conn.rollback()


def readfile_tip(conn, filename):
    f = open(filename, 'r')

    # Traverse the file
    while 1:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        data = json.loads(line)

        business_id = data['business_id']
        user_id     = data['user_id']
        text        = data['text'].replace('\n', '\t')
        date        = data['date']
        likes       = data.get('likes', 0)
        type        = data['type']

        # Insert into reviews
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO tips
                        (business_id, user_id, text, date, likes, type)
                        VALUES (%s, %s, %s, %s, %s, %s);
                        """,
                        (business_id, user_id, text, date, likes, type))
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
    conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data")
    # readfile_business(conn, 'yelp-data/business.json')
    # readfile_user(conn, 'yelp-data/user.json')
    # readfile_review(conn, 'yelp-data/review.json')
    readfile_tip(conn, 'yelp-data/tip.json')

    conn.close()


if __name__ == "__main__":
    main()
