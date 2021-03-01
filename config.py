import os
import ast

try:
    from dotenv import load_dotenv
    load_dotenv()
    RAN_FROM = ['Local Device', False]
except ModuleNotFoundError:
    RAN_FROM = ['Hosting', True]

# BOTS
MELON_TOKEN  = os.environ.get('TOKEN_MELON')
MELON_ID     = 811242799877718026
MELON_PREFIX = 'm.'

MINT_TOKEN   = os.environ.get('TOKEN_MINT')
MINT_ID      = 811236307211649064
MINT_PREFIX  = 'm!'

MELON_MINT_TOKEN  = os.environ.get('TOKEN_MELON_MINT')
MELON_MINT_ID     = 809281851650474005
MELON_MINT_PREFIX = 'mm?'

# FIREBASE (Database)
FIREBASE_CONFIG = ast.literal_eval(os.environ.get('FB_CONFIG'))
