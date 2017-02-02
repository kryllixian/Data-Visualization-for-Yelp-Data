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
        business_id     = data['business_id']
        name            = data['name']
        address         = data['full_address'].replace('\n', '\t')
        city            = data['city']
        state           = data['state']
        latitude        = data['latitude']
        longitude       = data['longitude']
        stars           = data['stars']
        review_count    = data['review_count']
        type            = data['type']

        # Insert into database
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO businesses
                        (business_id, name, address, city, state, latitude, longitude, stars, review_count, type)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """, (business_id, name, address, city, state, latitude, longitude, stars, review_count, type))
            conn.commit()
        except mysql.connector.Error as e:
            print "Error code:", e.errno        # error number
            print "SQLSTATE value:", e.sqlstate # SQLSTATE value
            print "Error message:", e.msg       # error message
            print "Error:", e                   # errno, sqlstate, msg values
            s = str(e)
            print "Error:", s                   # errno, sqlstate, msg values
            conn.rollback()



def main():
    conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data")
    readfile_business(conn, 'yelp-data/business.json')

    conn.close()








if __name__ == "__main__":
    main()
