from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask("lemon")
app.config['MONGODB_SETTINGS'] = {
    'db': 'lemon',
    'host': 'localhost',
    'port': 27017
}
mongo = MongoEngine(app) # 开启数据库实例