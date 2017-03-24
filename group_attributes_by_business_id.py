#!/usr/bin/python
import json
import mysql.connector


def connect_to_mysql(url, port, username, password, database):
    # Create DB connection
    conn = mysql.connector.connect(host=url, port=port, user=username, passwd=password, db=database)

    # Prepare a cursor
    cursor = conn.cursor()

    return conn



def group_attributes_by_id(conn, output_file):
    print(0)
    file = open(output_file, 'w')
    try:
        cur = conn.cursor()
        print(1)
        cur.execute("""SELECT business_id, attribute, value FROM attributes;""")
        print(2)
        rows = cur.fetchall()
        print(3)
        for row in rows:
            file.write(row[0] + '\t' + row[1] + '\t' + row[2])

    except mysql.connector.Error as e:
        print "Error code:", e.errno  # error number
        print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
        print "Error message:", e.msg  # error message
        print "Error:", e  # errno, sqlstate, msg values
        s = str(e)
        print "Error:", s  # errno, sqlstate, msg values

    file.close()


def create_all_attributes_for_each_business(pitt_restaurants, input_file, output_file):
    input = open(input_file, 'r')
    output = open(output_file, 'w')

    dic = {}
    ambience_list = ['Ambience_casual', 'Ambience_classy', 'Ambience_divey', 'Ambience_hipster', 'Ambience_intimate',
                     'Ambience_romantic', 'Ambience_touristy', 'Ambience_trendy', 'Ambience_upscale']
    dietary_list = ['DietaryRestrictions_dairy-free', 'DietaryRestrictions_gluten-free', 'DietaryRestrictions_halal',
                    'DietaryRestrictions_kosher', 'DietaryRestrictions_soy-free', 'DietaryRestrictions_vegan',
                    'DietaryRestrictions_vegetarian']
    parking_list = ['BikeParking', 'BusinessParking_garage', 'BusinessParking_lot', 'BusinessParking_street',
                    'BusinessParking_valet', 'BusinessParking_validated']
    music_list = ['Music_background_music', 'Music_dj', 'Music_jukebox', 'Music_karaoke', 'Music_live', 'Music_no_music',
                  'Music_video', 'GoodForDancing']
    good_for_meal_list = ['GoodForMeal_breakfast', 'GoodForMeal_brunch', 'GoodForMeal_lunch', 'GoodForMeal_dessert',
                          'GoodForMeal_dinner', 'GoodForMeal_latenight']
    best_night_list = ['BestNights_monday', 'BestNights_tuesday', 'BestNights_wednesday', 'BestNights_thursday',
                       'BestNights_friday', 'BestNights_saturday', 'BestNights_sunday']
    others_list = ['GoodForKids', 'OutdoorSeating', 'Open24Hours', 'DriveThru', 'ByAppointmentOnly', 'RestaurantsDelivery',
                   'RestaurantsGoodForGroups', 'RestaurantsReservations']

    # Read the whole input into memory
    while True:
        line = str(input.readline()).strip()
        # If line is null
        if not line:
            break

        items = line.split('\t')
        business_id = items[0]
        attribute = items[1]
        value = items[2]

        if not pitt_restaurants.has_key(business_id):
            continue

        if not dic.has_key(items[0]):
            dic[business_id] = {}

        dic[business_id][attribute] = value

    # Traverse the dictionary and normalize the data
    for business_id in dic:
        temp_dic = dic[business_id]
        new_dic = {}

        # Alcohol
        if temp_dic.has_key('Alcohol'):
            new_dic['Alcohol'] = temp_dic['Alcohol']
        else:
            new_dic['Alcohol'] = 'N/A'

        # Ambience
        ambience_value = ''
        for word in ambience_list:
            if temp_dic.has_key(word) and temp_dic[word] == 'True':
                ambience_value += word + ' '

        ambience_value = ambience_value.strip()
        if len(ambience_value) == 0:
            ambience_value = 'N/A'
        new_dic['Ambience'] = ambience_value

        # Dietary restrictions
        dietary_value = ''
        for word in dietary_list:
            if temp_dic.has_key(word) and temp_dic[word] == 'True':
                dietary_value += word + ' '

        dietary_value = dietary_value.strip()
        if len(dietary_value) == 0:
            dietary_value = 'N/A'
        new_dic['Dietary'] = dietary_value

        # Parking
        parking_value = ''
        for word in parking_list:
             if temp_dic.has_key(word) and temp_dic[word] == 'True':
                 parking_value += word + ' '

        parking_value = parking_value.strip()
        if len(parking_value) == 0:
            parking_value = 'N/A'
        new_dic['Parking'] = parking_value

        # Music
        music_value = ''
        for word in music_list:
            if temp_dic.has_key(word) and temp_dic[word] == 'True':
                music_value += word + ' '

        music_value = music_value.strip()
        if len(music_value) == 0:
            music_value = 'N/A'
        new_dic['Music'] = music_value

        # Noise Level
        if temp_dic.has_key('NoiseLevel'):
            new_dic['NoiseLevel'] = temp_dic['NoiseLevel']
        else:
            new_dic['NoiseLevel'] = 'N/A'

        # Price range
        if temp_dic.has_key('RestaurantsPriceRange2'):
            new_dic['PriceRange'] = temp_dic['RestaurantsPriceRange2']
        else:
            new_dic['PriceRange'] = 'N/A'

        # Attire
        if temp_dic.has_key('RestaurantsAttire'):
            new_dic['Attire'] = temp_dic['RestaurantsAttire']
        else:
            new_dic['Attire'] = 'N/A'

        # Good for meal
        good_for_meal_value = ''
        for word in good_for_meal_list:
            if temp_dic.has_key(word) and temp_dic[word] == 'True':
                good_for_meal_value += word + ' '

        good_for_meal_value = good_for_meal_value.strip()
        if len(good_for_meal_value) == 0:
            good_for_meal_value = 'N/A'
        new_dic['GoodForMeal'] = good_for_meal_value

        # Best nights
        best_night_value = ''
        for word in best_night_list:
            if temp_dic.has_key(word) and temp_dic[word] == 'True':
                best_night_value += word + ' '

        best_night_value = best_night_value.strip()
        if len(best_night_value) == 0:
            best_night_value = 'N/A'
        new_dic['BestNight'] = best_night_value

        # Other attributes
        others_value = ''
        for word in others_list:
            if temp_dic.has_key(word) and temp_dic[word] == 'True':
                others_value += word + ' '

        others_value = others_value.strip()
        if len(others_value) == 0:
            others_value = 'N/A'
        new_dic['Others'] =others_value

        # Write to file
        output.write(business_id + '\t' + new_dic['Alcohol'] + '\t' + new_dic['Ambience'] + '\t' + new_dic['Dietary'] + '\t' +
                     new_dic['Parking'] + '\t' + new_dic['Music'] + '\t' + new_dic['NoiseLevel'] + '\t' + new_dic['PriceRange'] + '\t' +
                     new_dic['Attire'] + '\t' + new_dic['GoodForMeal'] + '\t' + new_dic['BestNight'] + '\t' + new_dic['Others'] + '\n')


def get_restaurants_in_pitt(conn, output_file):
    file = open(output_file, 'w')
    dic = {}
    try:
        cur = conn.cursor()
        cur.execute("""SELECT b.business_id FROM businesses b, categories c
                        WHERE b.latitude >= 40 AND b.latitude <= 41 AND
                        b.longitude >= -81 AND b.longitude <= -79 AND
                        b.business_id = c.business_id AND c.name = 'Restaurants';""")
        rows = cur.fetchall()
        for row in rows:
            dic[row[0]] = 1
            file.write(row[0] + '\n')

    except mysql.connector.Error as e:
        print "Error code:", e.errno  # error number
        print "SQLSTATE value:", e.sqlstate  # SQLSTATE value
        print "Error message:", e.msg  # error message
        print "Error:", e  # errno, sqlstate, msg values
        s = str(e)
        print "Error:", s  # errno, sqlstate, msg values

    file.close()
    return dic




def main():
    # print('00')
    conn = connect_to_mysql("localhost", 3306, "", "", "yelp_data_new")
    # print('11')
    # group_attributes_by_id(conn, 'all_attributes')
    # print('22')

    dic = get_restaurants_in_pitt(conn, 'restaurants_pittsburgh')

    conn.close()

    create_all_attributes_for_each_business(dic, 'all_attributes_sorted', 'attributes_pitt_restaurants')


if __name__ == "__main__":
    main()
