import json
import mysql.connector


def connect_to_mysql(url, port, username, password, database):
    # Create DB connection
    conn = mysql.connector.connect(host=url, port=port, user=username, passwd=password, db=database)

    # Prepare a cursor
    cursor = conn.cursor()

    return conn


def get_review_of_top_categories(conn, category_name):
    try:
        cur = conn.cursor()
        cur.execute("""
                        SELECT r.review_id, r.text
                        FROM businesses b, reviews r, categories c
                        WHERE b.latitude >= 40 AND b.latitude <= 41 AND
                              b.longitude >= -81 AND b.longitude <= -79 AND
                              c.name = '%s' AND r.business_id = b.business_id AND
                              c.business_id = b.business_id;
                    """,
                    category_name)

        # Write the result into local file
        target_file = open(category_name, 'w')
        for (review_id, text) in cursor:
            target_file.write(text)
            target_file.write('\n')
        target_file.close()

    except mysql.connector.Error as e:
        print "Error code:", e.errno  # error number
        print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
        print "Error message:", e.msg  # error message
        print "Error:", e  # errno, sqlstate, msg values
        s = str(e)
        print "Error:", s  # errno, sqlstate, msg values


def main():
    conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data_new")
    # get_review_of_top_categories(conn, 'Restaurants')
    get_review_of_top_categories(conn, 'Shopping')
    get_review_of_top_categories(conn, 'Food')
    get_review_of_top_categories(conn, 'Beauty & Spas')
    get_review_of_top_categories(conn, 'Home Services')
    get_review_of_top_categories(conn, 'Nightlife')
    get_review_of_top_categories(conn, 'Health & Medical')
    get_review_of_top_categories(conn, 'Bars')
    get_review_of_top_categories(conn, 'Automotive')
    get_review_of_top_categories(conn, 'Local Services')
    conn.close()


if __name__ == "__main__":
    main()
