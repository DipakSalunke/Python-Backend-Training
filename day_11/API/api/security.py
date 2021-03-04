from werkzeug.security import safe_str_cmp
from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from ma import ma
# jwt security required functions


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and check_password_hash(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

# user model for storing user data


class UserModel(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod    
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    
# user schema

class UserModelSchema(ma.SQLAlchemyAutoSchema):
    username = ma.Str(required=True)
    password = ma.Str(required=True)

    class Meta:
        model = UserModel


userModelSchema = UserModelSchema()

# user resource for registration


class UserRegister(Resource):

    def post(self):
        
        data = request.get_json()
        errors = userModelSchema.validate(data)
        print(errors)
        if errors:
            return {"message": errors}, 400
        
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400
        user = UserModel(data["username"], generate_password_hash(data['password'], method='sha256'))
        user.save_to_db()
        return {"message": "User created successfully"}, 201
