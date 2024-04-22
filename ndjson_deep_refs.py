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

    typ_pad = 18
    ref_pad = 95

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
        print( f'# {val_t:<{typ_pad}} # {ref_s:<{ref_pad}} # {val[:5]}' )
        for i , v in enumerate(val) : print_deep_refs( f'{ref_s}[ {i} ]' , v )

    elif isinstance( val , dict ) :
        for k , v in val.items() : print_deep_refs( f'{ref_s}[ "{k}" ]' , val[ k ] )

    else : print( f"# TODO # Type : {(type(val)) : {val}}" )  # Fix me if this ever happens


########################################################################
##                            Read in Data                            ##
########################################################################

for rec_str in fileinput.input() :

    if not rec_str.strip() : continue

    try : 
        print_deep_refs( "rec" , json.loads( rec_str ) )
        print()
    except Exception as try_err : 
        print( f'# Try Error : {try_err}' )
        print( f'# rec_str   : {rec_str}' )
    except : pass




