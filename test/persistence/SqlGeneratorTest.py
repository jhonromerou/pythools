import unittest

from jhonromerou.persistence.SqlGenerator import SqlGenerator
from test.ReadResources import ReadResources

table = 'table'
fields = [
    {'name': 'id', 'auto_increment': True},
    {'name': 'user'},
    {'name': 'actived', 'type': 'boolean', 'default': True}
]
data = [
    {'user': 'jhromero'},
    {'user': 'jdoe', 'actived': 'false'},
    {'user': 'user3'}
]


class SqlGeneratorTest(unittest.TestCase):
    def test_insert_multiple_in_one(self):
        query = SqlGenerator.insert(table, fields, data)
        expected_query = ReadResources.get_content('sql/insert_multiple_in_one.sql')
        self.assertEqual(expected_query, query)  # add assertion here

    def test_insert_multiple_divide_2(self):
        query = SqlGenerator.insert(table, fields, data, 2)
        expected_query = ReadResources.get_content('sql/insert_multiple_divide_2.sql')
        self.assertEqual(expected_query, query)  # add a

    def test_insert_1(self):
        query = SqlGenerator.insert(table, fields, [
            {'user': 'jhromero'}])
        expected_query = ReadResources.get_content('sql/insert_1_row.sql')
        self.assertEqual(expected_query, query)
