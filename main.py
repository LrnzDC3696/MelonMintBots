import os

from hata import Client, start_clients
from hata.ext.commands import setup_ext_commands
from hata.ext.extension_loader import EXTENSION_LOADER
from hata.ext.commands.helps.subterranean import SubterraneanHelpCommand

try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError:
    pass

MMB = Client(os.environ.get('TOKEN'))

setup_ext_commands(MMB,'m!')
MMB.commands(SubterraneanHelpCommand(color=0xBC2E25), 'help')

@MMB.events
async def ready(client):
    print(f'{client:f} logged in.')

def load_modules(directory):
    try:
        for name in os.listdir(directory):
            if name.endswith(".py"):
                EXTENSION_LOADER.add(f"modules.{name[:-3]}")
    except FileNotFoundError:
        print('No Such Files')
        
if __name__ == '__main__':
    
    EXTENSION_LOADER.add_default_variables(MMB=MMB)
    load_modules('modules')
    EXTENSION_LOADER.load_all()
    start_clients()
