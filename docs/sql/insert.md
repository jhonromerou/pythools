from dataclasses import Field

# sql-generator

generate a sql script

## insert statement

### Field definition

| property       | required | type    | description                                          |
|----------------|----------|---------|------------------------------------------------------|
| name           | true     | string  | name of sql field                                    |
| type           | false    | string  | value type [number, boolean, string], default string |
| auto_increment | false    | boolean | generate automatic value to field 1-n                |
| default        | false    | string  | default value to field                               |

### Script

```python
from jhonromerou.persistence.SqlGenerator import SqlGenerator, Field

table_name = 'table_name'
fields = [
    Field('id', auto_increment=True),
    Field('user'),
    Field('year', type='number', default=2024),
    Field('actived', type='boolean')]

data = [
    {'user': 'jhromero', 'year': 1992},
    {'user': 'jdoe', 'actived': True},
    {'user': 'wick'}
]

result_query = SqlGenerator.insert(table_name, fields, data, maximum_one_insert=2)
```

### Result

```sql
INSERT INTO table_name
    (id, user, year, actived)
VALUES (1, 'jhromero', 1992, false),
       (2, 'jdoe', 2024, true);
INSERT INTO table_name
    (id, year, actived, user)
VALUES (3, 'wick', 2024, false);
```