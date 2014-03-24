from ichnaea.tests.base import DBTestCase


class TestDatabase(DBTestCase):

    def test_constructors(self):
        self.assertEqual(self.archival_db.engine.name, 'mysql')
        self.assertEqual(self.volatile_db.engine.name, 'mysql')

    def test_sessions(self):
        self.assertTrue(
            self.archival_db_session.bind.engine is self.archival_db.engine)
        self.assertTrue(
            self.volatile_db_session.bind.engine is self.volatile_db.engine)

    def test_table_creation(self):
        session = self.archival_db_session
        result = session.execute('select * from cell;')
        self.assertTrue(result.first() is None)
        result = session.execute('select * from measure;')
        self.assertTrue(result.first() is None)
