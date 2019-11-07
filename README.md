# JSON-Merge
JSON-Merge is a utility for merging json files in the specified folder.

## INSTALLATION
It requires a basic installation of Python3.X which can be downloaded from:
[Python Software Foundation](https://www.python.org/downloads/)

## USAGE
When importing as a module:
```
    jsonmerger = JsonMerger();
    jsonmerger.merge(folder_path, input_file_base_name, output_file_base_name, max_file_size);
```

When using from command line:
```
    python3 jsonmerge.py folder_path input_file_base_name output_file_base_name max_file_size
```

## Time Complexity Analysis
JSON-Merger on a very basic level:
+ Iterates through all the files in the folder [O(n)], where n is number of files.
+ Sorts the files in increasing order of counter value [O(nlog(n)], where n is number of files.
+ Iterates through all the keys of all the files [O(number_of_files * number_of_keys)].

In worst case the time complexity will be O(n x k), where n is number of files and k is maximum number of keys in any file. 
