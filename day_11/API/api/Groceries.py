# imports
from flask import Flask, request
from flask_restful import Resource, Api
from datetime import timedelta
from flask_jwt import JWT, jwt_required
from security import authenticate, identity,UserRegister
from db import db
from ma import ma
# app config
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecret'
app.config["JWT_EXPIRATION_DELTA"] = timedelta(hours=1)
db.init_app(app)
ma.init_app(app)
jwt = JWT(app, authenticate, identity)

# model


class Vegetables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=True,nullable=False)
    quantity = db.Column(db.Float(2),nullable=False)

# schema


class VegetablesSchema(ma.SQLAlchemyAutoSchema):
    name = ma.Str(required=True)
    quantity = ma.Float(required=True)

    class Meta:
        model = Vegetables


@app.before_first_request
def create_tables():
    db.create_all()

vegetablesSchema = VegetablesSchema()
all_vegetablesSchema = VegetablesSchema(many=True)

# Resource_1


class vegetable(Resource):
    @jwt_required()
    def get(self, name: str):
        veg = Vegetables.query.filter_by(name=name).first()
        if veg is None:
            return {"message": "vegetable not found"}, 404
        else:
            return vegetablesSchema.dump(veg), 200

    @jwt_required()
    def delete(self, name: str):
        result = Vegetables.query.filter_by(name=name).delete()
        db.session.commit()
        if result:
            return {'message': 'vegetable deleted'}, 200
        else:
            return {"message": "vegetable not found"}, 404
        
    @jwt_required()
    def put(self, name: str):
        data = request.get_json()
        veg = Vegetables.query.filter_by(name=name).first()
        if veg is None:
            veg = Vegetables(name=name, quantity=data['quantity'])
            db.session.add(veg)
            db.session.commit()
        else:
            Vegetables.query.filter_by(name=name).update(
                {"quantity": data['quantity']})
            db.session.commit()
        return vegetablesSchema.dump(veg), 201

# Resource_2


class vegetableList(Resource):
    @jwt_required()
    def get(self):
        return all_vegetablesSchema.dump(Vegetables.query.all()), 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        errors = vegetablesSchema.validate(data)
        print(errors)
        if errors:
            return {"message": errors}, 400
        if Vegetables.query.filter_by(name=data['name']).first() is not None:
            return {'message': "vegetable with name '{}' already exists.".format(data['name'])}, 400
        veg = Vegetables(name=data["name"], quantity=data['quantity'])
        db.session.add(veg)
        db.session.commit()
        return vegetablesSchema.dump(veg), 201


# endpoints
api.add_resource(vegetable, '/vegetable/<string:name>')
api.add_resource(vegetableList, '/vegetables')
api.add_resource(UserRegister, '/register')

# checkrun

if __name__ == '__main__':
    app.run(debug=True)
