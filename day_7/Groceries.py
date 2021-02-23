from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

vegetables = [
    {
        'name': 'Onion',
                'quantity': 15
    }, {
        'name': 'potato',
                'quantity': 13
    }
]


class vegetable(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('quantity',
                        type=float,
                        required=True,
                        help="quantity cannot be left blank!"
                        )

    def get(self, name):
        veg = {'vegetable': next(
            filter(lambda x: x['name'] == name, vegetables), None)}
        if veg['vegetable'] is None:
            return {"message": "vegetable not found"}, 404
        else:
            return veg, 200

    def delete(self, name):
        global vegetables
        vegbef = len(vegetables)
        vegetables = list(filter(lambda x: x['name'] != name, vegetables))
        vegaft = len(vegetables)
        if vegbef > vegaft:
            return {'message': 'vegetable deleted'}, 200
        else:
            return {"message": "vegetable not found"}, 404

    def put(self, name):
        data = vegetable.parser.parse_args()
        veg = next(filter(lambda x: x['name'] == name, vegetables), None)
        if veg is None:
            veg = {'name': name, 'quantity': data['quantity']}
            vegetables.append(veg)
        else:
            veg.update(data)
        return veg, 201


class vegetableList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="name cannot be left blank!"
                        )
    parser.add_argument('quantity',
                        type=float,
                        required=True,
                        help="quantity field cannot be left blank!"
                        )

    def get(self):
        return {'vegetables': vegetables}, 200

    def post(self):
        data = vegetableList.parser.parse_args()
        if next(filter(lambda x: x['name'] == data['name'], vegetables), None) is not None:
            return {'message': "vegetable with name '{}' already exists.".format(data['name'])}, 400
        vegetable = {'name': data['name'], 'quantity': data['quantity']}
        vegetables.append(vegetable)
        return vegetable, 201


api.add_resource(vegetable, '/vegetable/<string:name>')
api.add_resource(vegetableList, '/vegetables')

if __name__ == '__main__':
    app.run(debug=True)
