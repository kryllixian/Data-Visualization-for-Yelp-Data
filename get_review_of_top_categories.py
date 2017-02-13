import io
import mysql.connector


def connect_to_mysql(url, port, username, password, database):
    # Create DB connection
    conn = mysql.connector.connect(host=url, port=port, user=username, passwd=password, db=database)

    # Prepare a cursor
    cursor = conn.cursor()

    return conn


def get_review_of_category(conn, category_name):
    try:
        cur = conn.cursor()
        cur.execute("""
                        SELECT r.review_id, r.text
                        FROM businesses b, reviews r, categories c
                        WHERE b.latitude >= 40 AND b.latitude <= 41 AND
                              b.longitude >= -81 AND b.longitude <= -79 AND
                              c.name = %s AND r.business_id = b.business_id AND
                              c.business_id = b.business_id;
                    """,
                    (category_name,))

        # Write the result into local file
        target_file = io.open(category_name, 'w', encoding='utf8')
        # print(cur.fetchone())
        while True:
            line = cur.fetchone()
            if not line:
                break

            # print(line[1])
            target_file.write(line[1] + '\n')
        target_file.close()

    except mysql.connector.Error as e:
        print("Error code:", e.errno)  # error number
        print("SQLSTATE value:", e.sqlstate)  # SQLSTATE value
        print("Error message:", e.msg)  # error message
        print("Error:", e)  # errno, sqlstate, msg values
        s = str(e)
        print("Error:", s)  # errno, sqlstate, msg values


def main():
    conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data_new")
    # get_review_of_category(conn, 'Vietnamese')

    get_review_of_category(conn, 'Restaurants')
    get_review_of_category(conn, 'Shopping')
    get_review_of_category(conn, 'Food')
    get_review_of_category(conn, 'Beauty & Spas')
    get_review_of_category(conn, 'Home Services')
    get_review_of_category(conn, 'Nightlife')
    get_review_of_category(conn, 'Health & Medical')
    get_review_of_category(conn, 'Bars')
    get_review_of_category(conn, 'Automotive')
    get_review_of_category(conn, 'Local Services')
    conn.close()


if __name__ == "__main__":
    main()
