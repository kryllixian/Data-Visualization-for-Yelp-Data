import io
import mysql.connector
import re

# Get word count
dic = {}
stop_words = {}

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



def get_review_of_category_all_locations(conn, category_name):
    try:
        cur = conn.cursor()
        cur.execute("""
                        SELECT r.review_id, r.text
                        FROM businesses b, reviews r, categories c
                        WHERE c.name = %s AND r.business_id = b.business_id AND
                              c.business_id = b.business_id;
                    """,
                    (category_name,))

        # print(cur.fetchone())
        while True:
            line = cur.fetchone()
            if not line:
                break

            words = re.sub("[^\w]", " ",  line[1]).split()
            for word in words:
                if dic.has_key(word):
                    dic[word] += 1
                else:
                    dic[word] = 1

    except mysql.connector.Error as e:
        print("Error code:", e.errno)  # error number
        print("SQLSTATE value:", e.sqlstate)  # SQLSTATE value
        print("Error message:", e.msg)  # error message
        print("Error:", e)  # errno, sqlstate, msg values
        s = str(e)
        print("Error:", s)  # errno, sqlstate, msg values



def printDic():
    target_file = open('word_freq', 'w')
    for key in dic:
        target_file.write(str(key) + '\t' + str(dic[key]) + '\n')
    target_file.close()



def readFile():
    file = open('stop_words', 'r')
    while True:
        line = file.readline()
        if not line:
            break

        stop_words[line.strip()] = 1

    file = open('sorted_word_freq', 'r')
    while True:
        line = file.readline()
        if not line:
            break

        key = str(line.split('\t')[0])
        value = int(line.split('\t')[1])

        if stop_words.has_key(key):
            continue

        dic[key] = value



    # sortD = sorted(dic.items(), key=lambda value: -value[1])
    #
    target_file = open('test', 'w')
    for key in dic:
        target_file.write(str(key) + '\t' + str(dic[key]) + '\n')
    target_file.close()





def main():
    conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data_new")

    # get_review_of_category(conn, 'Vietnamese')

    readFile()
    # get_review_of_category_all_locations(conn, 'Restaurants')
    # dic['a'] = 1
    # printDic()
    # get_review_of_category(conn, 'Shopping')
    # get_review_of_category(conn, 'Food')
    # get_review_of_category(conn, 'Beauty & Spas')
    # get_review_of_category(conn, 'Home Services')
    # get_review_of_category(conn, 'Nightlife')
    # get_review_of_category(conn, 'Health & Medical')
    # get_review_of_category(conn, 'Bars')
    # get_review_of_category(conn, 'Automotive')
    # get_review_of_category(conn, 'Local Services')
    conn.close()


if __name__ == "__main__":
    main()
