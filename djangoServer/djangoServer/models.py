import pymongo
from djangoServer2.config.config import conf

client = pymongo.MongoClient("mongodb://"+conf.mongodb.host+":"+conf.mongodb.port)
dbname=client.get_database(conf.mongodb.dbname)
collection=dbname.get_collection(conf.mongodb.collection)
