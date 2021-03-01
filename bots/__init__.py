import os

from hata import Client, start_clients, ActivityRich, ActivityTypes, Status
from hata.ext.extension_loader import EXTENSION_LOADER

from bot_utils.database import My_Database

import config

MINT = Client(
    token     = config.MINT_TOKEN,
    client_id = config.MINT_ID,
    status    = None,
    activity  = ActivityRich("Nihongo Quest",type_=ActivityTypes.watching)
)

MELON = Client(
    token     = config.MELON_TOKEN,
    client_id = config.MELON_ID,
    status    = "dnd",
    activity  = ActivityRich("The Server",type_=ActivityTypes.watching)
)

MELON_MINT = Client(
    token     = config.MELON_MINT_TOKEN,
    client_id = config.MELON_MINT_ID,
    status    = 'idle',
    activity  = ActivityRich("My Creator",type_=ActivityTypes.watching)
)

#Connecting to database
MELON_MINT.loop.run(My_Database.setup_firebase(config.FIREBASE_CONFIG))

EXTENSION_LOADER.add_default_variables(
    MINT  = MINT,
    MELON = MELON,
    MELON_MINT = MELON_MINT,
)

EXTENSION_LOADER.load_extension('bots.mint',       locked=True)
EXTENSION_LOADER.load_extension('bots.melon',      locked=True)
EXTENSION_LOADER.load_extension('bots.melon_mint', locked=True)

path = os.path.abspath('.')
for folder_name in os.listdir(path):
    
    if not folder_name.endswith('_modules'):
        continue
    
    folder_path = os.path.join(path, folder_name)
    for file_name in os.listdir(folder_path):
        if not file_name.endswith('.py'):
            continue
        
        file_name = file_name[:-3]
        EXTENSION_LOADER.add(f'{folder_name}.{file_name}')

EXTENSION_LOADER.load_all()
