#!/usr/bin/python
import json
import mysql.connector
import io


def connect_to_mysql(url, port, username, password, database):
    # Create DB connection
    conn = mysql.connector.connect(host=url, port=port, user=username, passwd=password, db=database)

    # Prepare a cursor
    cursor = conn.cursor()

    return conn


def get_table_info(conn, table_name):
    try:
        # print(table_name)
        cur = conn.cursor()
        cur.execute("SELECT r.* FROM reviews r, businesses b WHERE b.latitude >= 40 AND b.latitude <= 41 AND b.longitude >= -81 AND b.longitude <= -79 AND  r.business_id = b.business_id;")

        # Write the result into local file
        target_file = io.open(table_name + '_data_pittsburgh', 'w', encoding='utf8')

        while True:
            line = cur.fetchone()
            if not line:
                break

            res = ''
            i = 0
            for word in line:
                word = unicode(word).replace('\t', 'whdawnwanghaodawnwhdawn')
                res += word
                if i != len(line) - 1:
                    res += '\t'
                i += 1

            res = res + '\n'

            # print(res)
            target_file.write(res)
        target_file.close()

    except mysql.connector.Error as e:
        print("Error code:", e.errno)  # error number
        print("SQLSTATE value:", e.sqlstate)  # SQLSTATE value
        print("Error message:", e.msg)  # error message
        print("Error:", e)  # errno, sqlstate, msg values
        s = str(e)
        print("Error:", s)  # errno, sqlstate, msg values


def main():
    local_conn = connect_to_mysql("localhost", 3306, "root", "", "yelp_data_new")
    # get_business_data(local_conn)
    # get_table_info(local_conn, "businesses")
    get_table_info(local_conn, "reviews")
    # get_table_info(local_conn, "Attributes")
    # get_table_info(local_conn, "categories")

    local_conn.close()


if __name__ == "__main__":
    main()
