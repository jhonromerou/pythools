
class FWrite:
    @staticmethod
    def csv(file_name: str, data: list):
        FWrite.with_delimiter(',', file_name, data)

    @staticmethod
    def tvs(file_name: str, data: list):
        FWrite.with_delimiter('\t', file_name, data)

    @staticmethod
    def with_delimiter(delimiter: str, file_name: str, data: list):
        f = open(file_name, "w")
        for line_data in data:
            line = ''
            for field in line_data:
                line += '{}{}'.format(field, delimiter)
            f.write('{}\n'.format(line[:len(line) - 1]))
        f.close()
