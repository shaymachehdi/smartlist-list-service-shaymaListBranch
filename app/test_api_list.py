import json
import unittest

from listservice import app
# set our application to testing mode
from listservice.list.routes import list

app.register_blueprint(list)

app.testing = True
app_context = app.app_context()


# app_context.push()

class TestApi(unittest.TestCase):

    # Test: Get all lists

    def test_get_all_list(self):
        with app.app_context():
            self.list = app.test_client()
            resp = self.list.get(path='/list', content_type='application/json')
            self.assertEqual(resp.status_code, 200)

    # Test: Get a single list by designatin + device_id

    def test_getting_a_single_list(self):
        data = dict(device_id=1,designation='designation', enabled=True)
        with app.app_context():
            self.list = app.test_client()
            response = self.list.get('/list/<int:id>', data=json.dumps(data), content_type='application/json')

    # Test: Add list
    def test_add_list(self):
        data = dict(designation='test', created_at='2010-04-02', recurrence='1',
                    device_id='2')
        with app.app_context():
            # resp = list.get('/list')

            self.list = app.test_client()
            response = self.list.post('/list/add', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)

    # # Test:  Delete list

    def test_delete_list(self):
        data = dict(id=1, enabled=True)
        with app.app_context():
            self.list = app.test_client()
            response = self.list.delete('/list/<int:id>', data=json.dumps(data),
                                        content_type='application/json')
            self.assertEqual(response.status_code, 200)

    # Test: Edit List

    def test_update_list(self):
        data = dict(id=1, enabled=True)
        with app.app_context():
            self.list = app.test_client()
            response = self.list.put('/list/<int:id>', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)

    # # Test: Delete listProduct

    def test_delete_listProduct(self):
        data = dict(list_id=1, product_id=2, enabled=True)
        with app.app_context():
            self.listProduct = app.test_client()
            response = self.listProduct.delete('/listProduct/<int:idProduct>/<int:idList>', data=json.dumps(data),
                                               content_type='application/json')


if __name__ == "__main__":
    unittest.main()
