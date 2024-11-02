# create files

generate a new file with type structure.

## [csv] comma-separate values

```python
from jhonromerou.filereader.FWrite import FWrite

FWrite.csv("dir/path.csv", [
    ['line1_value1', 'line1_value2', 'line1_value3'],
    ['line2_value2', 'line2_value2', 'line2_value3']
])

''' -> cat dir/path.csv
line1_value1,line1_value2,line1_value3
line2_value1,line2_value2,line2_value3
'''
```

## [tvs] tabulator-separate values

```python
from jhonromerou.filereader.FWrite import FWrite

FWrite.tvs("dir/path.csv", [
    ['line1_value1', 'line1_value2', 'line1_value3'],
    ['line2_value2', 'line2_value2', 'line2_value3']
])

''' -> cat dir/path.tsv
line1_value1    line1_value2    line1_value3
line2_value1    line2_value2    line2_value3
'''
```
