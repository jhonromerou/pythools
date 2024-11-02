import time


class FReader:
    def __init__(self, file_path: str, columns_name: list,
                 delimiter=',', start_line=1, end_line=1000000):
        """
       :param file_path: path of file to read.
       :param columns_name: list with sorted names for columns.
       :param delimiter: use to separate in columns each line.
       :param start_line: line to start read content, from 1 to n.
       :param end_line: line to end read content. to n.
       """
        self.handle = open(file_path, "r")
        self.delimiter = delimiter
        self.columns_name = columns_name
        self.start_line = start_line
        self.end_line = end_line

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.handle.close()

    @staticmethod
    def tsv(file_path: str, columns_name: list, start_line=1, end_line=1000000):
        """
        :param file_path: path of file to read
        :param columns_name: list with sorted names for columns
        :param start_line: line to start read content, from 1 to n
        :param end_line: line to end read content. to n
        """
        return FReader(file_path, columns_name, '\t', start_line, end_line)

    @staticmethod
    def csv(file_path: str, columns_name: list, start_line=1, end_line=1000000):
        """
        :param file_path: path of file to read
        :param columns_name: list with sorted names for columns
        :param start_line: line to start read content, from 1 to n
        :param end_line: line to end read content. to n
        """
        return FReader(file_path, columns_name, ',', start_line, end_line)

    @staticmethod
    def with_delimiter(delimiter: str, file_name: str, columns_name: list, start_line=1, end_line=1000000):
        return FReader(file_name, columns_name, delimiter, start_line, end_line)

    def stream(self, callback, limit=100, sleep=0, key_type='string'):
        line_reads = 1
        start_line = self.start_line
        end_line = self.end_line
        is_key_number = key_type == 'index'
        with self.handle as file:
            data = []
            for line in file.readlines():
                if not start_line > line_reads:
                    content = line.strip().split(self.delimiter)
                    data_line = [] if is_key_number else {}
                    index = 0
                    for field in self.columns_name:
                        if is_key_number:
                            data_line.append(content[index])
                        else:
                            data_line[field] = content[index]
                        index += 1
                    data.append(data_line)
                # process lines in batch
                if line_reads % limit == 0:
                    callback(data, {'number_line': line_reads})
                    if sleep > 0:
                        print('waiting {} seg... next range: {},{}'.format(sleep, line_reads, limit))
                        time.sleep(sleep)
                    data = []
                line_reads += 1
                if line_reads > end_line:
                    break
            callback(data, {'number_line': line_reads})

    def for_line(self, callback):
        line_reads = 1
        start_line = self.start_line
        end_line = self.end_line
        with self.handle as file:
            for line in file.readlines():
                if not start_line > line_reads:
                    content = line.strip().split(self.delimiter)
                    data_line = {}
                    index = 0
                    for field in self.columns_name:
                        data_line[field] = content[index]
                        index += 1
                    callback(data_line, {'number_line': line_reads})
                line_reads += 1
                if line_reads > end_line:
                    break
