class Field:
    def __init__(self, table: str, type='string', default=None, auto_increment=False):
        self.name = table
        self.type = type
        self.default = default
        self.auto_increment = auto_increment


class SqlGenerator:
    def __init__(self, table: str, fields: list[Field]):
        self.table = table
        self.fields = fields
        self.__generated_id = 1

    def insert(self, data: list, maximum_one_insert=50):
        num_rows = len(data)
        if num_rows == 0:
            return ''

        query_base = self.__base_insert()

        full_query = query_base
        restart_base = False
        for row in data:
            if restart_base:
                full_query += query_base

            full_query += '\n    ('
            for field in self.fields:
                value = SqlGenerator.get_field_value(field, row, self.__generated_id)
                full_query += '{}, '.format(value)
            self.__generated_id += 1
            full_query = full_query[:len(full_query) - 2] + ')'

            restart_base = (self.__generated_id) % maximum_one_insert == 0
            if restart_base:
                full_query += ';\n'
            else:
                full_query += ','

        full_query = full_query[:len(full_query) - 1]
        if num_rows < maximum_one_insert:
            return full_query + ';\n'

        return full_query

    def __base_insert(self):
        query_base = 'INSERT INTO {}\n    ('.format(self.table)
        for field in self.fields:
            query_base += '{}, '.format(field.name)

        return query_base[:len(query_base) - 2] + ')\nVALUES'

    def prepare_insert(self, scape = '%s'):
        fields = ''
        for field in self.fields:
            fields += '{}, '.format(scape)

        return '{} ({})'.format(self.__base_insert(), fields[:len(fields) - 2])

    @staticmethod
    def get_field_value(field: Field, row: dict, generate_id):
        if field.auto_increment:
            value = generate_id
        elif field.name not in row:
            value = field.default
        else:
            value = row[field.name]

        if field.type == 'number':
            value = '{}'.format(value)
        elif field.type == 'boolean':
            value = '{}'.format('true' if value == True else 'false')
        else:
            value = '\'{}\''.format(value)

        return value
