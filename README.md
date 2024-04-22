# ndjson-utilities
Tools I have written to work with ndjson files.


## print_nested_structure

This function will read multidimensional data and recursively descend into that data. This helps you identify the structure of nested dictionaries and lists, including keys at each level and the data types of the values.

With the data structure broken down, you can find the exact index needed to access the values you need from the data.

As an example, let's day you were given this long and complex bit of JSON, needed to understand how to access and extract specific values.

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

Sometimes you just want to understand the shape of the data you are working with. More often, you need take in data from multiple souces and extract just a few values to build some new record. This function will allow to quick identify the deeply chained indexes to refence when assigned values to your new variables.

```python
artist       = json[ "music" ][ "artist" ]
album_title  = json[ "music" ][ "album" ][ "title" ]
album_year   = json[ "music" ][ "album" ][ "year" ]
album_tracks = json[ "music" ][ "album" ][ "tracks" ]
```

## print_nested_structure.py

This is a script that uses the `print_nested_structure` and reads reads ndjson data from either a file or from STDIN and deconstructs the data just as it is show above.

I have an alias to this script in my bash run com file. 
 - Use `nano ~/.bashrc` to open the the rc file.
 - Somewhere, I put mine at the end, add the line `alias ndjsonstruct=/path/to/ndjson_nested_structure.py`
 - use `source ~/.bashrc` to reload your run com file and use the alias

### Usage

If you set the alias, it is as easy as:

```sh
ndjsonstruct gemini_sample_data_03.ndjson 
# or, for gzipped data
gunzip -c Kaggle_500MB_TV_Show.ndjson.gz | head | ndjsonstruct
```

If you did not set an alias, run it like this:

```sh
python3 /path/to/ndjson_nested_structure.py gemini_sample_data_03.ndjson 
# or, for gzipped data
gunzip -c Kaggle_500MB_TV_Show.ndjson.gz | head | python3 /path/to/ndjson_nested_structure.py
```




