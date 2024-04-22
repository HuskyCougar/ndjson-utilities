#!/usr/bin/python3

# https://github.com/HuskyCougar/ndjson-utilities
# https://github.com/HuskyCougar/ndjson-utilities/blob/master/read_ndjson_and_yield_dict.py
# read_ndjson_and_yield_dict.py

import os
import sys
import gzip
import json

########################################################################
##               Read NDJSON File and Yield Dictionary                ##
########################################################################

#region    ## Read NDJSON File and Yield Dictionary ####################

def read_ndjson_and_yield_dict( path_str: str) -> dict:

    """
    Reads an NDJSON or JSON file and yields individual dictionaries from each record.

    Args:
        path_str: String representing the file to be read.

    Yields:
        Dictionaries parsed from each record in the file.
    """

    if not ( os.path.isfile( path_str ) ) :
        print( f'# ERROR # File not found: {path_str}' , file=sys.stderr)
        return

    ####################################################################
    ##                           Open File                            ##
    ####################################################################

    try:
        
        if   path_str.endswith( ( '.ndjson.gz', '.json.gz' ) ) : fh = gzip.open( path_str , mode='rt' , encoding="utf-8" )
        elif path_str.endswith( ( '.ndjson'   , '.json'    ) ) : fh =      open( path_str , mode='r'  , encoding="utf-8" )
        else:
            print( f'Could not guess how to open this file: {path_str}' , file=sys.stderr )
            return
    
    except FileNotFoundError:
        print( f'File not found: {path_str}' , file=sys.stderr )

    if not fh : 
        print( f'No file handle opened: {path_str}' , file=sys.stderr )
        return

    ####################################################################
    ##                          Read NDJSON                           ##
    ####################################################################

    if path_str.endswith( ( '.ndjson.gz', '.ndjson' ) ) : 

        try :

            #print( f'path_str : {path_str}')

            for rec_str in fh :
            
                if rec_str.startswith( '#' ) : continue
            
                try :
                    rec = json.loads( rec_str )

                    if   isinstance( rec , dict ) : yield rec

                    elif isinstance( rec , list ) :

                        for rec2 in rec :
                            if   isinstance( rec2 , dict ) : yield rec2

                except json.JSONDecodeError as try_err :
                    print( f'Error decoding JSON data: {try_err}' , file=sys.stderr )

                except Exception as try_err :
                    print( f'# ERROR  # Could not load NDJSON record : {try_err}' , file=sys.stderr )

        except EOFError as try_err :

            print( f'# ERROR  # Problem reading this file : {path_str}' , file=sys.stderr )
            print( f'# ERROR  # Python says this is the problem : {try_err}' , file=sys.stderr )
        
        except Exception as try_err :
            
            print( f'# ERROR  # Problem reading this file : {path_str}' , file=sys.stderr )
            print( f'# ERROR  # Python says this is the problem : {try_err}' , file=sys.stderr )
            return

        finally : fh.close()

    ####################################################################
    ##                   Read JSON Array of Objects                   ##
    ####################################################################

    elif path_str.endswith( ( '.json.gz' , '.json' ) ) :

        try :

            #print( f'path_str : {path_str}')

            json_rec = json.load( fh )

            if isinstance( json_rec , list ) :

                for rec in json_rec :

                    if isinstance( rec , dict ) : yield rec

        except json.JSONDecodeError as try_err :
            print( f'Error decoding JSON data: {try_err}' , file=sys.stderr )

        except EOFError as try_err :

            print( f'# ERROR  # Problem reading this file : {path_str}' , file=sys.stderr )
            print( f'# ERROR  # Python says this is the problem : {try_err}' , file=sys.stderr )
        
        except Exception as try_err :
            
            print( f'# ERROR  # Problem reading this file : {path_str}' , file=sys.stderr )
            print( f'# ERROR  # Python says this is the problem : {try_err}' , file=sys.stderr )
            return

        finally : fh.close()

#endregion ## Read NDJSON File and Yield Dictionary ####################


########################################################################
##                               Usage                                ##
########################################################################

# Use the above function to read in NDJSON files and return a Python 
# dictionary. This will also read a list of JSON file and if it is an 
# Array of Objects (List of Dictionaries) the function will return each 
# of those objects one at a time so you can use the data as though it 
# was an NDJSON file.

#   read_this_file = r'/CODE/SampleData/reddit_2017_conspiracy_modlogs_full.ndjson.gz'
#   
#   print( f'read_this_file : {read_this_file}')
#   
#   for rec in read_ndjson_and_yield_dict( read_this_file ) :
#   
#       # Do something with the record returned
