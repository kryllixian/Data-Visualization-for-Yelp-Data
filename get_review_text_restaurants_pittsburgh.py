import mysql.connector
import re


def connect_to_mysql(url, port, username, password, database):
    # Create DB connection
    conn = mysql.connector.connect(host=url, port=port, user=username, passwd=password, db=database)

    # Prepare a cursor
    cursor = conn.cursor()
    return conn



def group_review_text_by_business_id(conn, output_file):
    file = open(output_file, 'w')
    dic = {}
    try:
        cur = conn.cursor()
        cur.execute("""
                        SELECT r.review_id, r.business_id, r.text
                        FROM businesses b, categories c, reviews r
                        WHERE
                            c.name = 'Restaurants' AND b.latitude >= 40 AND b.latitude <= 41 AND
                            b.longitude >= -81 AND b.longitude <= -79 AND
                            b.business_id = c.business_id AND
                            r.business_id = b.business_id;
                    """)

        rows = cur.fetchall()
        for row in rows:
            key = row[1]
            data = re.sub('[^A-Za-z0-9 ]+','' , row[2].encode('ascii', errors='ignore').lower().replace('\t', ' '))
            data = re.sub(' +', ' ', data)
            if dic.has_key(key):
                dic[key] += data
            else:
                dic[key] = data

        for key in dic.keys():
            file.write(key + '\t' + dic[key] + '\n')

    except mysql.connector.Error as e:
        print "Error code:", e.errno  # error number
        print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
        print "Error message:", e.msg  # error message
        print "Error:", e  # errno, sqlstate, msg values
        s = str(e)
        print "Error:", s  # errno, sqlstate, msg values


def get_word_count_each_item(stopword_filename, input_filename, output_filename):
    input_file = open(input_filename, 'r')
    output_file = open(output_filename, 'w')
    stopword_file= open(stopword_filename, 'r')

    stop_word_dic = {}
    # Read stop words
    while True:
        line = stopword_file.readline().strip()
        if not line:
            break

        stop_word_dic[line] = 1

    # print(str(stop_word_dic))


    while True:
        line = input_file.readline().strip()
        if not line:
            break

        business_id = line.split('\t')[0]
        words = line.split('\t')[1]
        word_freq = {}
        output = business_id + '\t'

        for word in words.split(' '):
            # Skip stop words
            if word in stop_word_dic:
                continue

            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

        word_freq = sorted(word_freq.items(), key=lambda (k, v): -v)
        # print(word_freq)
        for (key, value) in word_freq:
            output += key + ':' + str(value) + '\t'

        output = output.strip() + '\n'
        output_file.write(output)



def main():
    # conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data_new")
    # group_review_text_by_business_id(conn, 'pitt_restaurants_review_text')
    get_word_count_each_item('stop_words', 'pitt_restaurants_review_text', 'pitt_restaurants_review_compressed')


if __name__ == "__main__":
    main()
