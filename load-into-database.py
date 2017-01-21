import json
import pymongo
from pymongo import MongoClient


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


def json_to_mongodb(db, filepath, collection_name):
    with open(filepath) as data_file:
        for line in data_file:
            data = json.loads(line)
            db[collection_name].insert_one(data)


def main():
    db = connect_to_mongodb("mongodb://localhost", 27017, 'YelpData')
    json_to_mongodb(db, 'yelp-data/business.json', 'business')
    json_to_mongodb(db, 'yelp-data/checkin.json', 'checkin')
    json_to_mongodb(db, 'yelp-data/review.json', 'review')
    json_to_mongodb(db, 'yelp-data/tip.json', 'tip')
    json_to_mongodb(db, 'yelp-data/user.json', 'user')


if __name__ == "__main__":
    main()
