class SqlGenerator:
    @staticmethod
    def insert(table_name: str, fields: list, data: list, maximum_one_insert=50):
        query_base = 'INSERT INTO {}\n    ('.format(table_name)
        for field in fields:
            fieldName = field['name']
            query_base += '{}, '.format(fieldName)

        query_base = query_base[:len(query_base) - 2] + ')\nVALUES'

        full_query = query_base
        generate_id = 1
        restart_base = False
        for row in data:
            if restart_base:
                full_query += query_base

            full_query += '\n    ('
            for field in fields:
                value = SqlGenerator.get_field_value(field, row, generate_id)
                full_query += '{}, '.format(value)
            generate_id += 1
            full_query = full_query[:len(full_query) - 2] + ')'

            restart_base = (generate_id - 1) % maximum_one_insert == 0
            if restart_base:
                full_query += ';\n'
            else:
                full_query += ','

        full_query = full_query[:len(full_query) - 1]
        if not restart_base:
            full_query += ';'

        return full_query

    @staticmethod
    def get_field_value(field: dict, row: dict, generate_id):
        default_value = None
        fieldName = field['name']
        typeField = 'string' if 'type' not in field else field['type']

        if 'default' in field:
            default_value = field['default']

        if 'auto_increment' in field:
            value = generate_id
            typeField = 'number'
        else:
            value = default_value if fieldName not in row else row[fieldName]

        if typeField == 'number':
            value = '{}'.format(value)
        elif typeField == 'boolean':
            value = '{}'.format('true' if value == True else 'false')
        else:
            value = '\'{}\''.format(value)

        return value
