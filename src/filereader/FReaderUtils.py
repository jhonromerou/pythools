import os


class FReaderUtils:
    @staticmethod
    def create_dir(dir_path: str):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    @staticmethod
    def create_file_in_dir(dir_path: str, file_name: str, index=0):
        FReaderUtils.create_dir(dir_path)

        if index > 0:
            index_string = '00{}'.format(index)
            index_string = index_string[len(index_string) - 3: len(index_string)]
            return open('{}/{}_{}'.format(dir_path, index_string, file_name), 'w')
        else:
            return open('{}/{}'.format(dir_path, file_name), 'w')
