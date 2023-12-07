from flask_sqlalchemy import SQLAlchemy
from flask import current_app,request
import requests
from config.config import conf
from sqlalchemy import event
import hashlib

postgredb = SQLAlchemy()


class Models(postgredb.Model):
    __abstract__ = True
    id = postgredb.Column(postgredb.String())
    
class BiModel(Models):
    __tablename__="bimodel"
    
    product_id=postgredb.Column(postgredb.Integer, primary_key=True, unique=True)
    category=postgredb.Column(postgredb.String())
    industry=postgredb.Column(postgredb.String())
    business_scale=postgredb.Column(postgredb.String())
    user_type=postgredb.Column(postgredb.String())
    no_of_users=postgredb.Column(postgredb.String())
    deployment=postgredb.Column(postgredb.String())
    os=postgredb.Column(postgredb.String())
    mobile_apps=postgredb.Column(postgredb.String())
    pricing=postgredb.Column(postgredb.String())
    rating=postgredb.Column(postgredb.String())
    
    def __init__(self, product_id:int,industry:str,category:str,business_scale:str,user_type:str
                 ,no_of_users:str,deployment:str,os:str,mobile_apps:str,pricing:str
                 ,rating:str,id:str) -> None:
        self.product_id=product_id
        self.industry=industry
        self.category=category
        self.business_scale=business_scale
        self.user_type=user_type
        self.no_of_users=no_of_users
        self.deployment=deployment
        self.os=os
        self.mobile_apps=mobile_apps
        self.pricing=pricing
        self.rating=rating
        self.id=id
        
    def __repr__(self):
        return f"<BI {self.product_id}>"

@event.listens_for(BiModel,"after_insert")
def insert_change(mapper,connection,target):
    current_app.logger.info("insert changes detected")
    requestWebhook("insert_changes")
    
@event.listens_for(BiModel,"after_update")
def update_change(mapper,connection,target):
    current_app.logger.info("update changes detected")
    requestWebhook("update_changes")
    
@event.listens_for(BiModel,"after_delete")
def delete_change(mapper,connection,target):
    current_app.logger.info("delete changes detected")
    requestWebhook("delete_changes")
 
def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def requestWebhook(changeType:str):
    webhookUrl=request.json.get("webhook-url") if request.json else conf.server.webhook
    payload={
        changeType:BiModel.__name__
    }
    try:
        res=requests.post(webhookUrl,json=payload)
        
        if res.status_code==200:
            current_app.logger.info("Webhook triggered successfully")
            return
        else:
            current_app.logger.info("hook aint in web ",res.status_code)
    except Exception as e:
        current_app.logger.error("yo somethin wrong fam ",e)
        return 