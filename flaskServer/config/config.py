from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Mongodb:
    host: str
    port: str
    collection: str

    @staticmethod
    def from_dict(obj: Any) -> 'Mongodb':
        _host = str(obj.get("host"))
        _port = str(obj.get("port"))
        _collection = str(obj.get("collection"))
        return Mongodb(_host, _port, _collection)

@dataclass
class Postgres:
    host: str
    sqlport: str
    user: str
    password: str
    dbname: str

    @staticmethod
    def from_dict(obj: Any) -> 'Postgres':
        _host = str(obj.get("host"))
        _sqlport = str(obj.get("sqlport"))
        _user = str(obj.get("user"))
        _password = str(obj.get("pass"))
        _dbname = str(obj.get("dbname"))
        return Postgres(_host, _sqlport, _user, _password, _dbname)


@dataclass
class Server:
    host: str
    port: str
    webhook:str

    @staticmethod
    def from_dict(obj: Any) -> 'Server':
        _host = str(obj.get("host"))
        _port = str(obj.get("port"))
        _webhook=str(obj.get("webhookUrl"))
        return Server(_host, _port,_webhook)
    
@dataclass
class Root:
    server: Server
    postgres: Postgres
    mongodb: Mongodb

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _server = Server.from_dict(obj.get("server"))
        _postgres = Postgres.from_dict(obj.get("postgres"))
        _mongodb = Mongodb.from_dict(obj.get("mongodb"))
        return Root(_server, _postgres, _mongodb)

with open("C:\VGBPython\graphql-flask\\flask2\\flaskServer2\\flaskServer\config.json") as config_file:
    parsed_json=json.load(config_file)
conf=Root.from_dict(parsed_json)

postgresUrl = (
    "postgresql://"
    + conf.postgres.user
    + ":"
    + conf.postgres.password
    + "@"
    + conf.postgres.host
    + ":"
    + conf.postgres.sqlport
    + "/"
    + conf.postgres.dbname
)

mongoUrl = (
    "mongodb://"
    + conf.mongodb.host
    +":"
    + conf.mongodb.port
    + "/" 
    + conf.mongodb.collection)