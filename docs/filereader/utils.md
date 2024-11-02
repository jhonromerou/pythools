# utils

## create file in dir

create and return a file in directory, if directory not exist, then create.

```python
from jhonromerou.filereader.FReaderUtils import FReaderUtils

dir_path = 'parent_folder/folder_to_create'
file_name = 'file_path.txt'
file_handler = FReaderUtils.create_file_in_dir(dir_path, file_name)

# result-> parent_folder/folder_to_create/file_path.txt
```

#### creation with prefix number

```python
from jhonromerou.filereader.FReaderUtils import FReaderUtils

dir_path = 'parent_folder/folder_to_create'
file_name = 'file_path.txt'

file_handler_1 = FReaderUtils.create_file_in_dir(dir_path, file_name, 1)
file_handler_10 = FReaderUtils.create_file_in_dir(dir_path, file_name, 10)
file_handler_11 = FReaderUtils.create_file_in_dir(dir_path, file_name, 11)
# result -> parent_folder/folder_to_create/001_file_path.txt
# parent_folder/folder_to_create/010_file_path.txt
# parent_folder/folder_to_create/011_file_path.txt
```