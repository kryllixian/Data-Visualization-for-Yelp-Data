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

    filename = table_name + '_data'
    f = open(filename, 'r')

    while True:
        line = str(f.readline())

        if not line:
            break

        words = line.split('\t')
        new_words = []

        if (len(words) != 10):
            print(words[0])
            break




        # for word in words:
        #     if word:
        #         new_words.append(word.replace('whdawnwanghaodawnwhdawn', '\t'))
        #     else:
        #         new_words.append('')
        #
        # try:
        #     # print(table_name)
        #     cur = conn.cursor()
        #     cur.execute("INSERT INTO " + table_name + " VALUES %r;" % (tuple(new_words),))
        #     conn.commit()
        #
        # except mysql.connector.Error as e:
        #     print("Error code:", e.errno)  # error number
        #     print("SQLSTATE value:", e.sqlstate)  # SQLSTATE value
        #     print("Error message:", e.msg)  # error message
        #     print("Error:", e)  # errno, sqlstate, msg values
        #     s = str(e)
        #     print("Error:", s)  # errno, sqlstate, msg values
        #     break


def main():
    local_conn = connect_to_mysql("localhost", 3306, "root", "", "yelp_data_new")
    # get_table_info(local_conn, "users")
    # get_table_info(local_conn, "businesses")
    # get_table_info(local_conn, "reviews")

    local_conn.close()


if __name__ == "__main__":
    main()
