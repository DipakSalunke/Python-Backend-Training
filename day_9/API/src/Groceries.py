#imports
from flask import Flask,request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#app config
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

#model
class Vegetables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    quantity = db.Column(db.Float(2))

#schema
class VegetablesSchema(ma.SQLAlchemyAutoSchema):
    name = ma.Str(required=True)
    quantity = ma.Float(required=True) 
    class Meta:
        model = Vegetables

#creates tables
db.create_all()


vegetablesSchema = VegetablesSchema()
all_vegetablesSchema = VegetablesSchema(many=True)

#Resource_1
class vegetable(Resource):
    def get(self, name):
        veg = Vegetables.query.filter_by(name=name).first()
        if veg is None:
            return {"message": "vegetable not found"}, 404
        else:
            return vegetablesSchema.dump(veg), 200

    def delete(self, name):
        result = Vegetables.query.filter_by(name=name).delete()
        db.session.commit()
        if result:
            return {'message': 'vegetable deleted'}, 200
        else:
            return {"message": "vegetable not found"}, 404

    def put(self, name):
        data =request.get_json()
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

#Resource_2
class vegetableList(Resource):
    def get(self):
        return all_vegetablesSchema.dump(Vegetables.query.all()), 200

    def post(self):
        data =request.get_json()
        errors = vegetablesSchema.validate(data)
        print(errors)
        if errors:
            return {"message":errors},400
        if Vegetables.query.filter_by(name=data['name']).first() is not None:
            return {'message': "vegetable with name '{}' already exists.".format(data['name'])}, 400
        veg = Vegetables(name=data["name"], quantity=data['quantity'])
        db.session.add(veg)
        db.session.commit()
        print(type(veg))
        return vegetablesSchema.dump(veg), 201

#endpoints
api.add_resource(vegetable, '/vegetable/<string:name>')
api.add_resource(vegetableList, '/vegetables')

#checkrun
if __name__ == '__main__':
    app.run(debug=True)
