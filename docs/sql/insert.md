# sql-generator

generate a sql script

## insert statement

### field definition allow properties

| property       | required | type    | description                                  |
|----------------|----------|---------|----------------------------------------------|
| name           | true     | string  | name of sql field                            |
| type           | false    | string  | value type [number, boolean], default string |
| auto_increment | false    | boolean | generate automatic value to field 1-n        |
| default        | false    | string  | default value to field                       |

### script

```python
from src.persistence.SqlGenerator import SqlGenerator

table_name = 'table_name'
field_definition = [
    {'name': 'id', 'auto_increment': True},
    {'name': 'year', 'type': 'number', 'default': 2024},
    {'name': 'actived', 'type': 'boolean'},
    {'name': 'user'},
]

data = [
    {'user': 'jhromero', 'year': 1992},
    {'user': 'jdoe', 'actived': True}
]

result_query = SqlGenerator.insert(table_name, field_definition, data)
```

### result

```sql
INSERT INTO table_name
    (id, year, actived, user)
VALUES
    (1, 1992, false, 'jhromero'),
    (2, 2024, true, 'jdoe');
```