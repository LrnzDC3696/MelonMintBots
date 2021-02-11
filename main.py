from hata import *
from hata.ext.commands import setup_ext_commands

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

MMB = Client(os.environ.get('TOKEN'))
setup_ext_commands(MMB,'m!')

@MMB.events
async def ready(client):
    print(f'{client:f} logged in.')

@MMB.commands
async def ping(client, message):
    await client.message_create(message, 'pong')

if __name__ == '__main__':
    MMB.start()
