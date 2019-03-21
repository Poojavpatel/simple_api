from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import random
from flask_responses import json_response

app=Flask(__name__)
api= Api(app)
CORS(app)

resultlist = ["Fake","Real"]

class User(Resource):
    def get(self):
        # randomly choosing real or fake and return with response status 200
        result = random.choice(resultlist)
        print(result)
        return json_response({"result":result}, status_code=200)
    
    def post(self, name):
        a = "url added to db"
        return a,200

api.add_resource(User, "/")
if __name__ == '__main__':
    app.run()