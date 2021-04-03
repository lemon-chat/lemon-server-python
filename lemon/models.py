from .application import mongo

class User(mongo.Document):
    userid = mongo.IntField(required=True)
    username = mongo.StringField(max_length=50)
    email = mongo.StringField(max_length=50)
    password = mongo.StringField(max_length=50)
