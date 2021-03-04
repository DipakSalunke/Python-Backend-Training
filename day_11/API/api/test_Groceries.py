from Groceries import app
import pytest
tester = app.test_client()
headers = ''
class TestSecurity:
    
    def test_reg_success(self):
        response = tester.post(
            '/register', json={"username": "dipak", "password": "supersecret"})
        status = response.status_code
        assert status == 201

        
    def test_reg_duplicate(self):
        response = tester.post(
            '/register', json={"username": "dipak", "password": "supersecret"})
        status = response.status_code
        assert status == 400

    def test_reg_bad_input(self):
        response = tester.post(
            '/register', json={"username": "dipak"})
        status = response.status_code
        assert status == 400
    
    def test_auth_success(self):
        response = tester.post(
            '/auth', json={"username": "dipak", "password": "supersecret"})
        status = response.status_code
        assert status == 200
        global headers
        headers = {'Authorization':'JWT {}'.format(response.json["access_token"])}

class TestVegetableList:
    def test_post_success(self):
        response = tester.post(
            '/vegetables', json={"name": "chilli", "quantity": 5.5},headers=headers)
        status = response.status_code
        assert status == 201

    def test_post_duplicate(self):
        response = tester.post(
            '/vegetables', json={"name": "chilli", "quantity": 5.5},headers=headers)
        status = response.status_code
        assert status == 400

    def test_post_bad_input(self):
        response = tester.post('/vegetables', json={"quantity": 5.5},headers=headers)
        status = response.status_code
        assert status == 400

    def test_get_vegetables(self):
        response = tester.get('/vegetables',headers=headers)
        status = response.status_code
        assert status == 200


class TestVegetable:
    def test_get_success(self):
        response = tester.get('/vegetable/{}'.format("chilli"),headers=headers)
        status = response.status_code
        assert status == 200

    def test_get_not_found(self):
        response = tester.get('/vegetable/{}'.format("potato"),headers=headers)
        status = response.status_code
        assert status == 404

    def test_put_update(self):
        response = tester.put(
            '/vegetable/{}'.format("chilli"), json={"quantity": 15.6},headers=headers)
        status = response.status_code
        assert status == 201

    def test_put_insert(self):
        response = tester.put(
            '/vegetable/{}'.format("potato"), json={"quantity": 10},headers=headers)
        status = response.status_code
        assert status == 201

    def test_delete_success(self):
        response = tester.delete('/vegetable/{}'.format("chilli"),headers=headers)
        status = response.status_code
        assert status == 200

    def test_delete_not_found(self):
        response = tester.delete('/vegetable/{}'.format("tomato"),headers=headers)
        status = response.status_code
        assert status == 404
