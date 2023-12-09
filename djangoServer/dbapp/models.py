from django.db import models
import logging
from config.config import conf
import pymongo

loggy=logging.getLogger(__name__)

# Create your models here.
class BiModel(models.Model):
    product_id=models.IntegerField(primary_key=True, unique=True)
    category=models.CharField(max_length=100)
    industry=models.CharField(max_length=100)
    business_scale=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100)
    no_of_users=models.CharField(max_length=100)
    deployment=models.CharField(max_length=100)
    os=models.CharField(max_length=100)
    mobile_apps=models.CharField(max_length=100)
    pricing=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    id=models.CharField(max_length=200)
    
    class Meta():
        db_table="bimodel"

client = pymongo.MongoClient('mongodb://'+conf.mongodb.host+":"+conf.mongodb.port+"/")
db = client[conf.mongodb.dbname]
collection = db[conf.mongodb.collection]