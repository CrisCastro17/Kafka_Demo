from kafka import KafkaConsumer
#import pandas as pd
import json
from pymongo import MongoClient
try:
   # connect = MongoClient('mongodb://root:root@localhost:27017')
    connect = MongoClient('mongodb://localhost:27017')
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

def main():
                     
    consumer = KafkaConsumer('twitter')
    db = connect.twitter
    collection = db.data
    #dbcur = initialize(db_name = "tweetdata")
    for msg in consumer:
        output = []
        output.append(json.loads(msg.value))
        collection.insert_one(json.loads(msg.value))
        print (json.loads(msg.value))
        print ('\n')


if __name__ == "__main__":
    main()
