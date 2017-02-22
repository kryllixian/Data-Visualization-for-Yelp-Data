import json
import pymongo
from pymongo import MongoClient
import bson

ids = {}


def connect_to_mongodb(url, port, database):
    print('Try to connect to database!')
    new_url = url + ':' + str(port)
    try:
        client = MongoClient(new_url)
        db = client[database]
        print('Connected to MongoDB!')
    except e:
        print('Unable to connect to MongoDB!')
    return db


def filter_business_pittsburgh(db, collection_name, new_collection_name):
    print('Filtering business in pittsburgh')
    db[new_collection_name].insert(db[collection_name].find({
            '$and': 
                [
                    {
                        'latitude': 
                            {
                                '$lte': 41, 
                                '$gte': 40
                            }
                    }, 
                    {
                        'longitude': 
                            {   '$lte': -79, 
                                '$gte': -81
                            }
                    }
                ]
            }
        ))


def filter_tip_pittsburgh(db):
    print('Left outer join tip to business in pittsburgh')
    db['pittsburgh_business'].aggregate(
        [
            {
                '$lookup': 
                {
                    'from': 'tip',
                    'localField': 'business_id',
                    'foreignField': 'business_id',
                    'as': 'tips'
                }
            },
            {
                '$out': "pittsburgh_business_tip"
            }
        ])


def filter_checkin_pittsburgh(db):
    print('Left outer join checkin to business in pittsburgh')
    db['pittsburgh_business_tip'].aggregate(
        [
            {
                '$lookup': 
                {
                    'from': 'checkin',
                    'localField': 'business_id',
                    'foreignField': 'business_id',
                    'as': 'checkins'
                }
            },
            {
                '$out': "pittsburgh_business_tip_checkin"
            }
        ])


def filter_review_pittsburgh(db):
    print('Left outer join review to business in pittsburgh')
    db['pittsburgh_business_tip_checkin'].aggregate(
        [
            {
                '$lookup': 
                {
                    'from': 'review',
                    'localField': 'business_id',
                    'foreignField': 'business_id',
                    'as': 'reviews'
                }
            },
            {
                '$out': "pittsburgh_business_tip_checkin_review"
            }
        ])


def filter_user_pittsburgh(db):
    print('Left outer join user to business in pittsburgh')
    db['pittsburgh_business_tip_checkin_review'].aggregate(
        [
            {
                '$lookup': 
                {
                    'from': 'user',
                    'localField': 'business_id',
                    'foreignField': 'business_id',
                    'as': 'users'
                }
            },
            {
                '$out': "pittsburgh_business_tip_checkin_review_user"
            }
        ])


def test(db):
    for item in db['pittsburgh_business'].find():
        business_id = str(item['business_id'])
        ids[business_id] = 1

    # print(ids)

    for item in db['checkin'].find():
        # print(item['business_id'])
        if ids.has_key(item['business_id']):
            if ids[item['business_id']] == 2:
                print('Find one!!!!!!!')
                break
            ids[item['business_id']] = 2


def main():
    db = connect_to_mongodb("mongodb://localhost", 27017, 'YelpData')
    # test(db)
    # filter_business_pittsburgh(db, 'business', 'pittsburgh_business')
    # filter_tip_pittsburgh(db)
    # filter_checkin_pittsburgh(db)
    # filter_review_pittsburgh(db)
    # filter_user_pittsburgh(db)


if __name__ == "__main__":
    main()
