# read files

## csv

```python
from jhonromerou.filereader.FReader import FReader

file_name = 'dir/file.csv'
start_line = 1
end_line = 100
columns = ['col1', 'col2', 'col3']
tsv_list_data = FReader.csv(file_name, columns, start_line, end_line)
```

## tsv

```python
from jhonromerou.filereader.FReader import FReader

file_name = 'dir/file.csv'
start_line = 1
end_line = 100
columns = ['col1', 'col2', 'col3']
tsv_list_data = FReader.tsv(file_name, columns, start_line, end_line)
```
 
properties

| property   | required |                                                     |
|------------|----------|-----------------------------------------------------|
| file_name  | true     | file path                                           |
| columns    | true     | array position with keys alias                      |
| start_line | false    | if is defined, then start in line. default = 0      |
| end_line   | false    | if is defined, then read to this line. default = 1M |

## yml

read yaml file and return dict with keys

```python
from jhonromerou.filereader.FReader import FReader

ENVS_DICTIONARY = {}
ymlData = FReader.yaml('file_path.yml', ENVS_DICTIONARY)

# -> {"key":{"i_key":"i_value"}...}
```
