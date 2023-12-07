from app import app
from flaskServer2.config.config import conf

if __name__=="__main__":
    app.run(conf.server.host,conf.server.port)