import os
from datetime import datetime


class FWrite:
    def __init__(self, file_path: str, delimiter=None):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.__protected_previous()
        self.handle = open(file_path, "w")
        self.delimiter = delimiter
        self.len_delimiter = 0 if delimiter is None else len(delimiter)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.handle.close()

    def __protected_previous(self):
        if os.path.isfile(self.file_path):
            date = datetime.now().strftime("%Y%m%d%H%M%S")
            new_file_path = self.file_path.replace(self.file_name, '{}_bk_{}'.format(self.file_name, date))
            os.renames(self.file_path, new_file_path)
            print('=> already file exists: {}\n\tgenerate backup: {}'.format(self.file_path, new_file_path))

    @staticmethod
    def csv(file_path: str):
        return FWrite(file_path, ',')

    @staticmethod
    def tsv(file_path: str):
        return FWrite(file_path, '\t')

    def add(self, line_data: list | dict | str):
        if type(line_data) == str:
            self.__add_line(line_data)
            return

        line = ''
        if type(line_data) == list:
            for value in line_data:
                line += '{}{}'.format(value, self.delimiter)
            self.__add_line(line)
            return

        for key in line_data:
            line += '{}{}'.format(line_data[key], self.delimiter)
        self.__add_line(line)

    def __add_line(self, line: str):
        self.handle.write('{}\n'.format(line[:len(line) - self.len_delimiter]))

    @staticmethod
    def with_delimiter(delimiter: str, file_name: str):
        return FWrite(file_name, delimiter)
