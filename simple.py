from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app=Flask(__name__)
api= Api(app)

resultlist = ["Fake","Real"]

class User(Resource):
    def get(self):
        # randomly choosing real or fake and return with response status 200
        result = random.choice(resultlist)
        print(result)
        return result, 200
    
    def post(self, name):
        a = "url added to db"
        return a,200

api.add_resource(User, "/")
