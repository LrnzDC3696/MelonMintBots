import os

from hata import Client, start_clients, ActivityRich, ActivityTypes, Status
from hata.ext.extension_loader import EXTENSION_LOADER

import config

MINT = Client(
    token= config.MINT_TOKEN,
    client_id= config.MINT_ID,
    status= None,
    activity = ActivityRich("Nihongo Quest",type_=ActivityTypes.watching)
    )

EXTENSION_LOADER.add_default_variables(MINT=MINT)


MELON = Client(
    token= config.MELON_TOKEN,
    client_id= config.MELON_ID,
    status= "dnd",
    activity = ActivityRich("The Server",type_=ActivityTypes.watching)
    )

EXTENSION_LOADER.add_default_variables(MELON=MELON)


MELON_MINT = Client(
    token= config.MELON_MINT_TOKEN,
    client_id= config.MELON_MINT_ID,
    status = 'idle',
    activity = ActivityRich("My Creator",type_=ActivityTypes.watching)
    )
    
EXTENSION_LOADER.add_default_variables(MELON_MINT=MELON_MINT)

EXTENSION_LOADER.load_extension('bots.mint', locked=True)
EXTENSION_LOADER.load_extension('bots.melon', locked=True)
EXTENSION_LOADER.load_extension('bots.melon_mint', locked=True)

try:
    for name in os.listdir('modules'):
        if name.endswith(".py"):
            EXTENSION_LOADER.add(f"modules.{name[:-3]}")
except FileNotFoundError:
    print('No Such Files')

EXTENSION_LOADER.load_all()
