import unittest
import tempfile


from main import create_app
from api.utils.database import db
from api.config.config import TestingConfig


class BaseTestCase(unittest.TestCase):
    """A base test case"""

    def setUp(self):

        self.test_db_file = tempfile.mkstemp()[1]
        database_uri = 'sqlite:///' + self.test_db_file
        TestingConfig.SQLALCHEMY_DATABASE_URI = database_uri

        app = create_app(TestingConfig)
        with app.app_context():
            db.create_all()
        app.app_context().push()

        self.app = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
