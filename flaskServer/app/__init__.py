from flask import Flask
from .app import server
from config import config


srv = Flask(__name__)
srv.config["SQLALCHEMY_DATABASE_URI"] = config.postgresUrl
srv.config["MONGO_URI"]=config.mongoUrl
srv.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

app=server(srv)