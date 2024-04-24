# ndjson-utilities
Tools I have written to work with ndjson files.

## print_nested_data

This function reads multidimensional data and recursively descends into it. This helps you identify the structure of nested dictionaries and lists, including keys at each level and the data types of the values.

With the data structure broken down, you can easily find the exact index (or key) needed to access the values you need from the data.

As an example, let's say you were given this long and complex piece of JSON. You'd need to understand how to access and extract specific values.

```js
json = {"music": {"artist": "The Beatles", "album": {"title": "Abbey Road", "year": 1969, "tracks": ["Come Together", "Something", "Here Comes the Sun"]}}}
```
This function would deconstruct the nested data and display it as shown below.

```js
# <class 'str'>      # json[ "music" ][ "artist" ]                   : The Beatles
# <class 'str'>      # json[ "music" ][ "album" ][ "title" ]         : Abbey Road
# <class 'int'>      # json[ "music" ][ "album" ][ "year" ]          : 1969
# <class 'list'>     # json[ "music" ][ "album" ][ "tracks" ]        # ['Come Together', 'Something', 'Here Comes the Sun']
# <class 'str'>      # json[ "music" ][ "album" ][ "tracks" ][ 0 ]   : Come Together
# <class 'str'>      # json[ "music" ][ "album" ][ "tracks" ][ 1 ]   : Something
# <class 'str'>      # json[ "music" ][ "album" ][ "tracks" ][ 2 ]   : Here Comes the Sun
```

Sometimes you just want to understand the structure of the data you're working with. More often, you need to take in data from multiple sources and extract just a few values to build a new record. This function will allow you to quickly identify the deeply chained indexes to reference when assigning values to your new variables.

```python
artist       = json[ "music" ][ "artist" ]
album_title  = json[ "music" ][ "album" ][ "title" ]
album_year   = json[ "music" ][ "album" ][ "year" ]
album_tracks = json[ "music" ][ "album" ][ "tracks" ]
```

## ndjson_print_structure.py

This is a script that uses the `print_nested_data` function and reads NDJSON data from either a file or standard input (STDIN). It deconstructs the data structure, similar to what was shown above.

I have an alias for this script in my bash run com file (.bashrc). Here's how to set it up:

 - Open your bash configuration file using `nano ~/.bashrc`.
 - Add a line at the end similar to: `alias ndjsonnested=/path/to/ndjson_nested_structure.py` (replace `/path/to/ndjson_nested_structure.py` with the actual path to your script).
 - After saving the changes, source the bash configuration file using `source ~/.bashrc` to reload it and start using the alias `ndjsonnested`.

This is a command-line tool that uses the `print_nested_data` and reads ndjson data from either a file or from STDIN and deconstructs the data just as it is shown above. 

To use this function to analyze your Python data copy the `print_nested_data` function into your script and use the function like `print_nested_data( "string_to_prepend" , var_name )`

### Usage

If you set the alias, it is as easy as:

```sh
ndjsonnested gemini_sample_data_03.ndjson 
# or, for gzipped data
gunzip -c Kaggle_500MB_TV_Show.ndjson.gz | head | ndjsonnested
```

If you did not set an alias, run it like this:

```sh
python3 /path/to/ndjson_nested_structure.py gemini_sample_data_03.ndjson 
# or, for gzipped data
gunzip -c Kaggle_500MB_TV_Show.ndjson.gz | head | python3 /path/to/ndjson_nested_structure.py
```

## ndjson_pretty.py

This is a simple command line tool that reads JSON or NDJSON data from a file or from STDIN and pretty prints the data to STDOUT. 

I have this set as an aliased command in my ~/.bashrc file.

## read_ndjson_and_yield_dict.py

This script does nothing. I assume that you will import or copy this function into your script.

The function in this script `read_ndjson_and_yield_dict` opens NDJSON files and returns a dictionary for each record. It also opens JSON files. If the JSON is an Array of Objects, the function will iterate over the list and yield dictionaries (or return dictionaries one by one).






