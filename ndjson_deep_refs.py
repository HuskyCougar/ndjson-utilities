#!/usr/bin/python3

# nano ~/.bashrc
# alias ndjsondeeprefs=/data/CODE/ndjson_deep_refs.py

import sys
import fileinput
import json

sys.stdout.reconfigure( line_buffering = True )

########################################################################
##                       Print Deep References                        ##
########################################################################

def print_deep_refs( ref , val ) :

    '''print_deep_refs - Print deep references to multidimensional python datastructures'''

    val_typ = str(type(val))
    ref_str = f'{(str(ref))}'

    if   isinstance( val , str   ) : print( f'# {val_typ:<18} # {ref_str:<65} : {val}' )
    elif isinstance( val , int   ) : print( f'# {val_typ:<18} # {ref_str:<65} : {val}' )
    elif isinstance( val , float ) : print( f'# {val_typ:<18} # {ref_str:<65} : {val}' )
    elif             val is None   : print( f'# {val_typ:<18} # {ref_str:<65} : None'  )

    elif isinstance( val , set   ) :
        print( f'# {val_typ:<18} # {ref_str:<65} # set' )
        # todo: figure out something useful. No sets in JSON.

    elif isinstance( val , list  ) :
        #print( f'# {val_typ:<18} # {ref_str:<65} # {val}' )
        for i in range(len(val)) : print_deep_refs( f'{ref_str}[ {i} ]' , val[ i ] )

    elif isinstance( val , dict ) :
        #print( f'# {val_typ:<18} # {ref_str:<65} # {val}' )
        for k,v in val.items() : print_deep_refs( f'{ref_str}[ {k} ]' , v )

    else : print( f"# TODO # Type : {(type(val)) : {val}}" )  # Fix me if this ever happens


########################################################################
##                            Read in Data                            ##
########################################################################

for rec_str in fileinput.input() :

    if not rec_str.strip() : continue

    try : 
        print_deep_refs( "rec" , json.loads(rec_str) )
        print()
    except Exception as try_err : 
        print( f'# Try Error : {try_err}' )
        print( f'# rec_str   : {rec_str}' )
    except : pass




