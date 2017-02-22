import json
import mysql.connector



def connect_to_mysql(url, port, username, password, database):
    # Create DB connection
    conn = mysql.connector.connect(host=url, port=port, user=username, passwd=password, db=database)

    # Prepare a cursor
    cursor = conn.cursor()

    return conn



def init():
    dic = {}
    dic['Ambience'] = 1
    dic['BusinessParking'] = 1
    dic['GoodForMeal'] = 1
    dic['Music'] = 1
    dic['DietaryRestrictions'] = 1
    dic['BestNights'] = 1
    dic['HairSpecializesIn'] = 1
    return dic



def read_file_businesses(dic, input_file, output_file):
    f = open(input_file, 'r')
    file = open(output_file, 'w')

    # Traverse the file
    while True:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        data = json.loads(line)

        categories = data['categories']
        business_id = data['business_id']

        if categories:
            for category in categories:
                if category == 'Restaurants':
                    attributes = data['attributes']
                    if attributes:
                        for attribute in attributes:

                            # Find if the attribute has inner attributes
                            flag = False
                            father_attr_name = ''
                            for key in dic:
                                if str(attribute).startswith(key):
                                    father_attr_name = key
                                    flag = True
                                    break
                            if flag == False:
                                key = attribute.split(': ')[0]
                                value = attribute.split(': ')[1]
                                file.write(business_id + '\t' + key + '\t' + value + '\n')
                            else:
                                attribute = attribute.replace("'", '"').replace(': ', ':"').replace(', ', '",').replace('}', '"}')
                                attribute = attribute[attribute.find('{'):]
                                sub_data = json.loads(attribute)

                                for key, value in sub_data.iteritems():
                                    key = father_attr_name + '_' + key
                                    file.write(business_id + '\t' + key + '\t' + value + '\n')
    f.close()
    file.close()


def write_to_MySQL(conn, filename):
    f = open(filename, 'r')

    # Traverse the file
    while True:
        line = str(f.readline())
        # If line is null
        if not line:
            break

        business_id = line.split('\t')[0]
        attribute = line.split('\t')[1]
        value = line.split('\t')[2]

        # Insert into businesses
        try:
            cur = conn.cursor()
            cur.execute("""
                        INSERT INTO attributes
                        (business_id, attribute, value) VALUES (%s, %s, %s);
                        """, (business_id, attribute, value))
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
    conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data_new")
    dic = init()
    # read_file_businesses(dic, 'yelp-data-new/business.json', 'test3')
    write_to_MySQL(conn, 'test3')

if __name__ == "__main__":
    main()
