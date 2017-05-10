import mysql.connector

def connect_to_mysql(url, port, username, password, database):
    # Create DB connection
    conn = mysql.connector.connect(host=url, port=port, user=username, passwd=password, db=database)

    # Prepare a cursor
    cursor = conn.cursor()

    return conn


def get_business_stars_pittsburgh(conn, output_file):
    file = open(output_file, 'w')
    try:
        cur = conn.cursor()
        cur.execute("""
                        SELECT business_id, stars
                        FROM businesses
                        WHERE
                            latitude >= 40 AND latitude <= 41 AND
                            longitude >= -81 AND longitude <= -79;
                    """)

        rows = cur.fetchall()
        for row in rows:
            file.write(str(row[0]) + '\t' + str(row[1]) + '\n')

    except mysql.connector.Error as e:
        print "Error code:", e.errno  # error number
        print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
        print "Error message:", e.msg  # error message
        print "Error:", e  # errno, sqlstate, msg values
        s = str(e)
        print "Error:", s  # errno, sqlstate, msg values


def main():
    conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data_new")
    get_business_stars_pittsburgh(conn, "pittsburgh_business_stars.dat")

if __name__ == "__main__":
    main()
