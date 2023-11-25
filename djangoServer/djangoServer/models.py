import pymongo
from djangoServer2.config.config import conf


schema={
    "$jsonSchema":{
        "bsonType":"object",
        "required":["product_Id"],
        "properties":{
            "product_Id":{
                "bsonType":"int"
            },
            "category":{
                "bsonType":"string"
            },
            "industry":{
                "bsonType":"string"
            },
            "business_scale":{
                "bsonType":"string"
            },
            "user_type":{
                "bsonType":"string"
            },
            "no_of_users":{
                "bsonType":"string"
            },
            "deployment":{
                "bsonType":"string"
            },
            "os":{
                "bsonType":"string"
            },
            "mobile_apps":{
                "bsonType":"string"
            },
            "pricing":{
                "bsonType":"string"
            },
            "rating":{
                "bsonType":"string"
            },
            "id":{
                "bsonType":"string"
            }
        }
    }
}


def InitMongoDB():
    client = pymongo.MongoClient("mongodb://"+conf.mongodb.host+":"+conf.mongodb.port)
    dbname=client.get_database(conf.mongodb.dbname)
    if conf.mongodb.collection in dbname.list_collection_names():
        collection=dbname.get_collection(conf.mongodb.collection)
    else:
        collection=dbname.create_collection(conf.mongodb.collection,validator=schema)
    return collection
    
