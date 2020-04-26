from flask import Flask, request, json,jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token)

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': '<---YOUR_DB_NAME--->',
    'host': 'mongodb://<---YOUR_DB_FULL URI--->'
}

db = MongoEngine(app)
app.config['SECRET_KEY'] = '<---YOUR_SECRET_FORM_KEY--->'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

mongo= PyMongo(app)
bcrypt= Bcrypt(app)
jwt= JWTManager(app)

CORS(app)

@app.route('/users/register',methods=['POST'])
def register():
    users= mongo.db.users
    Name= request.get_json()['Name']
    Email=request.get_json()['Email']
    Password=bcrypt.generate_password_hash(request.get_json()['Password']).decode('utf-8'))
    created=datatime.utcnow()

    user_id= users.insert{
        
    }
    