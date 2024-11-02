import unittest

from jhonromerou.filereader.FReader import FReader
from test.ReadResources import ReadResources


class FReaderTest(unittest.TestCase):
    # should return just first line
    def test_csv_first_line(self):
        data = FReader.csv(ReadResources.get_path('filereader/file.csv'),
                           ['id', 'user', 'name'],
                           1, 1)
        self.assertEqual([
            {'id': 'id', 'user': 'user', 'name': 'name'}
        ], data)  # add assertion here

    # should return from 2 line
    def test_csv_start_line(self):
        data = FReader.csv(ReadResources.get_path('filereader/file.csv'),
                           ['id', 'user', 'name'],
                           2)
        self.assertEqual([
            {'id': '1', 'user': 'jhromero', 'name': 'Jhon Romero'},
            {'id': '21', 'user': 'jdoe', 'name': 'Joe Doe'}
        ], data)  # add assertion here

    def test_tsv(self):
        data = FReader.tsv(ReadResources.get_path('filereader/file.tsv'),
                           ['id', 'user', 'name'],
                           2)
        self.assertEqual([
            {'id': '1', 'user': 'jhromero', 'name': 'Jhon Romero'},
            {'id': '21', 'user': 'jdoe', 'name': 'Joe Doe'}
        ], data)

    def test_with_delimiter(self):
        data = FReader.with_delimiter(';',
                                      ReadResources.get_path('filereader/file_v2.csv'),
                                      ['id', 'user', 'name'],
                                      2)
        self.assertEqual([
            {'id': '1', 'user': 'jhromero', 'name': 'Jhon Romero'},
            {'id': '21', 'user': 'jdoe', 'name': 'Joe Doe'}
        ], data)
