#!/usr/bin/python3

# nano ~/.bashrc
# alias ndjsondeeprefs=/data/CODE/ndjson_pretty.py

import sys
import fileinput
import json

sys.stdout.reconfigure( line_buffering = True )

for rec_str in fileinput.input() :

    try    : print( json.dumps( json.loads(rec_str ) , indent=4 ) )
    except Exception as try_err : print( f'# Try Error : {try_err}' )
    except : pass # Handle more errors
