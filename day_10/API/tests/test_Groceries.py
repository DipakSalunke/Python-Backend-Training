from src.Groceries import app
tester = app.test_client()


class TestVegetableList:
    def test_post_success(self):
        response = tester.post(
            '/vegetables', json={"name": "chilli", "quantity": 5.5})
        status = response.status_code
        assert status == 201

    def test_post_duplicate(self):
        response = tester.post(
            '/vegetables', json={"name": "chilli", "quantity": 5.5})
        status = response.status_code
        assert status == 400

    def test_post_bad_input(self):
        response = tester.post('/vegetables', json={"quantity": 5.5})
        status = response.status_code
        assert status == 400

    def test_get_vegetables(self):
        response = tester.get('/vegetables')
        status = response.status_code
        assert status == 200


class TestVegetable:
    def test_get_success(self):
        response = tester.get('/vegetable/{}'.format("chilli"))
        status = response.status_code
        assert status == 200

    def test_get_not_found(self):
        response = tester.get('/vegetable/{}'.format("potato"))
        status = response.status_code
        assert status == 404

    def test_put_update(self):
        response = tester.put(
            '/vegetable/{}'.format("chilli"), json={"quantity": 15.6})
        status = response.status_code
        assert status == 201

    def test_put_insert(self):
        response = tester.put(
            '/vegetable/{}'.format("potato"), json={"quantity": 10})
        status = response.status_code
        assert status == 201

    def test_delete_success(self):
        response = tester.delete('/vegetable/{}'.format("chilli"))
        status = response.status_code
        assert status == 200

    def test_delete_not_found(self):
        response = tester.delete('/vegetable/{}'.format("tomato"))
        status = response.status_code
        assert status == 404
