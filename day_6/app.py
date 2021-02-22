'''
Implement a small Flask App for Groceries API
Create a new project
Create and activate venv
Install Flask
Develop below endpoints:
/groceries - display all the veggies
/groceries/carrot - display the name of hte veggie and the current qty
Implement POST and DELETE as well for the Groceries API to add/delete veggies
'''
from flask import Flask, jsonify, request
app = Flask(__name__)

grocery_stores = [
    {
        'name': 'bigbasket',
        'groceries': [
            {
                'name': 'Onion',
                'price': 49.50,
                'qty': 15
            }, {
                'name': 'potato',
                'price': 22.77,
                'qty': 13
            }
        ]
    },
    {
        'name': 'grofers',
        'groceries': [
            {
                'name': 'Capsicum-Green',
                'price': 41.40,
                'qty': 12
            },
            {
                'name': 'Tomato-Hybrid',
                'price': 18.81,
                'qty': 32
            }
        ]
    }
]
# POST /store {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'groceries': []
    }
    grocery_stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in grocery_stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': grocery_stores})

# POST /store/<string:name>/groceries {name:, price:, qty:}
@app.route('/store/<string:name>/groceries', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in grocery_stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
                'qty': request_data['qty']
            }
            store['groceries'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/groceries/<string:iname>
@app.route('/store/<string:name>/groceries/<string:iname>')
def get_item_in_store(name, iname):
    for store in grocery_stores:
        if store['name'] == name:
            for item in store['groceries']:
                if item['name'] == iname:
                    return jsonify(item)
            return jsonify({'message': 'item not found'})
    return jsonify({'message': 'store not found'})

# DELETE /store/<string:name>/groceries/<string:iname>
@app.route('/store/<string:name>/groceries/<string:iname>', methods=['DELETE'])
def del_item_in_store(name, iname):
    cnt = -1
    for store in grocery_stores:
        cnt+=1
        if store['name'] == name:
            for item in store["groceries"]:
                if item['name'] == iname:
                    grocery_stores[cnt]["groceries"].remove(item)
                    return jsonify({'message': 'item deleted successfully'})
            return jsonify({'message': 'item not found'})
    return jsonify({'message': 'store not found'})


app.run(port=5000)
