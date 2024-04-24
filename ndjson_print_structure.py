#!/usr/bin/python3

# https://github.com/HuskyCougar/ndjson-utilities
# https://github.com/HuskyCougar/ndjson-utilities/blob/master/ndjson_print_structure.py
# ndjson_print_structure.py

import sys
import fileinput
import json

sys.stdout.reconfigure( line_buffering = True )

########################################################################
##                         Print Nested Data                          ##
########################################################################

def print_nested_data( ref , val ) :

    '''print_nested_data - this function provides a way to explore and understand the structure and content of complex nested data in Python'''

    typ_pad = 18
    ref_pad = 95
    max_list_preview = 5

    val_t = str(type(val))
    ref_s = f'{(str(ref))}'

    if   isinstance( val , str   ) : print( f'# {val_t:<{typ_pad}} # {ref_s:<{ref_pad}} : {val}' )
    elif isinstance( val , int   ) : print( f'# {val_t:<{typ_pad}} # {ref_s:<{ref_pad}} : {val}' )
    elif isinstance( val , float ) : print( f'# {val_t:<{typ_pad}} # {ref_s:<{ref_pad}} : {val}' )
    elif             val is None   : print( f'# {val_t:<{typ_pad}} # {ref_s:<{ref_pad}} : None'  )

    elif isinstance( val , set   ) : # Python has sets. JSON does not.
        print( f'# {val_t:<{typ_pad}} # {ref_s:<{ref_pad}} # set' )
        # GitHub homies, what might make sense here?

    elif isinstance( val , list  ) :
        print( f'# {val_t:<{typ_pad}} # {ref_s:<{ref_pad}} # {val[:max_list_preview]}' )
        for i , v in enumerate(val) : print_nested_data( f'{ref_s}[ {i} ]' , v )

    elif isinstance( val , dict ) :
        for k , v in val.items() : print_nested_data( f'{ref_s}[ "{k}" ]' , val[ k ] )

    else : print( f"# TODO # Type : {(type(val)) : {val}}" )  # Fix me if this ever happens

########################################################################
##                            Read in Data                            ##
########################################################################

for rec_str in fileinput.input() :

    if not rec_str.strip() : continue

    try :
        print_nested_data( "rec" , json.loads( rec_str ) )
        print()
    except Exception as try_err :
        print( f'# Try Error : {try_err}' )
        print( f'# rec_str   : {rec_str}' )
    except : pass


########################################################################
##                               Usage                                ##
########################################################################

#   ## Add alias to ~/.bashrc
#
#   nano ~/.bashrc
#   alias ndjsonnested=/path/to/ndjson_print_structure.py
#   source ~/.bashrc
#
#   Examples assume you made an alias. If you did not, use the path to the script instead.
#
#   Examples will also assume you have a file containing data that looks like this. This is Newline-Delimited JSON (NDJSON).
#
#   {"album": {"title": "Abbey Road", "year": 1969, "genre": "Rock"}, "tracks": ["Come Together", "Something", "Here Comes the Sun" ]}
#   {"album": {"title": "Nevermind", "year": 1991, "genre": "Grunge"}, "tracks": ["Smells Like Teen Spirit", "Come As You Are", "Lithium" ]}
#   {"album": {"title": "Blue Train", "year": 1957, "genre": "Jazz"}, "tracks": ["Blue Train", "Moment's Notice", "”Cease Fire”" ]}
#   {"album": {"title": "Kind of Blue", "year": 1959, "genre": "Jazz"}, "tracks": ["So What", "Freddie Freeloader", "Blue in Green" ]}
#   {"album": {"title": "The Black Parade", "year": 2006, "genre": "Rock"}, "tracks": ["The Black Parade", "Welcome to the Black Parade", "I Don't Love You" ]}
#
#
#   ## Run on a regular file using alias
#
#   ### Syntax
#
#       ndjsonnested music_albums.ndjson
#
#   ### Output
#
#       # <class 'str'>      # rec[ "album" ][ "title" ]                 : Abbey Road
#       # <class 'int'>      # rec[ "album" ][ "year" ]                  : 1969
#       # <class 'str'>      # rec[ "album" ][ "genre" ]                 : Rock
#       # <class 'list'>     # rec[ "tracks" ]                           # ['Come Together', 'Something', 'Here Comes the Sun']
#       # <class 'str'>      # rec[ "tracks" ][ 0 ]                      : Come Together
#       # <class 'str'>      # rec[ "tracks" ][ 1 ]                      : Something
#       # <class 'str'>      # rec[ "tracks" ][ 2 ]                      : Here Comes the Sun
#
#       # <class 'str'>      # rec[ "album" ][ "title" ]                 : Nevermind
#       # <class 'int'>      # rec[ "album" ][ "year" ]                  : 1991
#       # <class 'str'>      # rec[ "album" ][ "genre" ]                 : Grunge
#       # <class 'list'>     # rec[ "tracks" ]                           # ['Smells Like Teen Spirit', 'Come As You Are', 'Lithium']
#       # <class 'str'>      # rec[ "tracks" ][ 0 ]                      : Smells Like Teen Spirit
#       # <class 'str'>      # rec[ "tracks" ][ 1 ]                      : Come As You Are
#       # <class 'str'>      # rec[ "tracks" ][ 2 ]                      : Lithium
#
#   ## Just look at shape of data
#
#   ### Syntax
#
#       head music_albums.ndjson | ndjsonnested
#
#   ### Output
#
#       # <class 'str'>      # rec[ "album" ][ "title" ]                 : Abbey Road
#       # <class 'int'>      # rec[ "album" ][ "year" ]                  : 1969
#       # <class 'str'>      # rec[ "album" ][ "genre" ]                 : Rock
#       # <class 'list'>     # rec[ "tracks" ]                           # ['Come Together', 'Something', 'Here Comes the Sun']
#       # <class 'str'>      # rec[ "tracks" ][ 0 ]                      : Come Together
#       # <class 'str'>      # rec[ "tracks" ][ 1 ]                      : Something
#       # <class 'str'>      # rec[ "tracks" ][ 2 ]                      : Here Comes the Sun
#
#       # <class 'str'>      # rec[ "album" ][ "title" ]                 : Nevermind
#       # <class 'int'>      # rec[ "album" ][ "year" ]                  : 1991
#       # <class 'str'>      # rec[ "album" ][ "genre" ]                 : Grunge
#       # <class 'list'>     # rec[ "tracks" ]                           # ['Smells Like Teen Spirit', 'Come As You Are', 'Lithium']
#       # <class 'str'>      # rec[ "tracks" ][ 0 ]                      : Smells Like Teen Spirit
#       # <class 'str'>      # rec[ "tracks" ][ 1 ]                      : Come As You Are
#       # <class 'str'>      # rec[ "tracks" ][ 2 ]                      : Lithium
#
#   ## Look at shape of compressed data
#
#   ### Syntax
#
#       gunzip -c music_albums.ndjson.gz | head | ndjsonnested
#
#   ### Output
#
#   ## find records with specific values and then show the structure of only those records
#
#   ### Syntax
#
#       grep -i Grunge music_albums.ndjson | ndjsonnested
#
#   ### Output
#
#       # <class 'str'>      # rec[ "album" ][ "title" ]                 : Nevermind
#       # <class 'int'>      # rec[ "album" ][ "year" ]                  : 1991
#       # <class 'str'>      # rec[ "album" ][ "genre" ]                 : Grunge
#       # <class 'list'>     # rec[ "tracks" ]                           # ['Smells Like Teen Spirit', 'Come As You Are', 'Lithium']
#       # <class 'str'>      # rec[ "tracks" ][ 0 ]                      : Smells Like Teen Spirit
#       # <class 'str'>      # rec[ "tracks" ][ 1 ]                      : Come As You Are
#       # <class 'str'>      # rec[ "tracks" ][ 2 ]                      : Lithium
#
#   ## select records with specific values anywhere in the record, deconstruct, and then extract the specific value you want.
#
#   ### Syntax
#
#       grep -i Jazz music_albums.ndjson | ndjsonnested | grep title
#
#   ### Output
#
#       # <class 'str'>      # rec[ "album" ][ "title" ]                 : Blue Train
#       # <class 'str'>      # rec[ "album" ][ "title" ]                 : Kind of Blue
#


