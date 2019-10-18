import json
import unittest

from listservice import app
# set our application to testing mode
from listservice.listShared.routes import listShared

app.register_blueprint(listShared)

app.testing = True
app_context = app.app_context()


# app_context.push()

class TestApi(unittest.TestCase):

    # add listShared
    def test_add_listShared(self):
        data = dict(emailUser='hadhemiwesleti@gmail.com', list_id='1', permission='can view and edit', group_id='1')
        with app.app_context():
            self.listShared = app.test_client()
            response = self.listShared.post('/listShared/add', data=json.dumps(data), content_type='application/json')

    # delete listShared
    def test_delete_listShared(self):
        data = dict(list_id=1, enabled=True)
        with app.app_context():
            self.listShared = app.test_client()
            response = self.listShared.delete('/listShared/delete/<int:id>', data=json.dumps(data),
                                              content_type='application/json')

    # Test: Get all listShared

    def test_get_list_Shared(self):
        with app.app_context():
            self.listShared = app.test_client()
            resp = self.listShared.get(path='/listShared', content_type='application/json')
            self.assertEqual(resp.status_code, 200)


if __name__ == "__main__":
    unittest.main()
