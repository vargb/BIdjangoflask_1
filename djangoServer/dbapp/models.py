from django.db import models
from djongo import models as mongoModels
# Create your models here.

class BiModelPostgres(models.Model):
    product_id=models.IntegerField(primary_key=True)
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
    id=models.CharField(max_length=1500)

class BiModelMongo(mongoModels.Model):
    product_id=models.IntegerField(primary_key=True)
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
    id=models.CharField(max_length=1500)