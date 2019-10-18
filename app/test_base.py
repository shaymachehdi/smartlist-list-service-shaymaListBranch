import os
import unittest
from listservice import app, db
from listservice.listShared.models import ListShared

LIST_MS_DB = 'list_ms_db'
basedir = os.path.abspath(os.path.dirname(__file__))


class BasicTests(unittest.TestCase):
    """A base test case."""

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        # ensure that db URI is set up correctly

        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@mysql/list_ms_db' + os.path.join(basedir, LIST_MS_DB)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
        self.app = app.test_list()

        # ensure that db create models

        db.create_all()
        db.session.add(ListShared("hadhemiwesleti@gmail.com", "3", "2","can view and edit"))
        db.session.commit()

    # executed after each test

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == "__main__":
    unittest.main()