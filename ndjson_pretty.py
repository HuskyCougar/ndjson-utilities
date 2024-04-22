#!/usr/bin/python3

# https://github.com/HuskyCougar/ndjson-utilities
# https://github.com/HuskyCougar/ndjson-utilities/blob/master/ndjson_pretty.py
# ndjson_pretty.py

import sys
import fileinput
import json

sys.stdout.reconfigure( line_buffering = True )

########################################################################
##                            Read in Data                            ##
########################################################################

for rec_str in fileinput.input() :

    if not rec_str.strip() : continue

    try    : print( json.dumps( json.loads(rec_str ) , indent=4 ) )
    except Exception as try_err : print( f'# Try Error : {try_err}' )
    except : pass # Handle more errors


########################################################################
##                               Usage                                ##
########################################################################

#   ## Add alias to ~/.bashrc
#
#   nano ~/.bashrc
#   alias ndjsonstruct=/path/to/ndjson_pretty.py
#   source ~/.bashrc




