from flask import Flask,request
from flask_restful import Resource,Api
from pymongo import MongoClient
import logging

client = MongoClient('mongodb+srv://jeanpaulsb:1041690395@pollingapp.yvnqz8y.mongodb.net/test')

app = Flask(__name__)
api = Api(app)

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG, filename= "data.log")


class Register(Resource):
    def post(self):
        # getting our jurors db
        db = client.Users
        jurors = db.Jurors
        
        # handling data from html form
        data = request.form

        # user object
        user = {
            'email':data['email'],
            'name':data['name'],
            'upbId':data['upbId'],
            'password':data['password'],
            'participants':[]
        }

    

        jurors.insert_one(user)

        logging.debug(f"Added new Juror {user['name']}")



        return 201

api.add_resource(Register,"/api/register")

if __name__ == '__main__':
    app.run(debug=True)