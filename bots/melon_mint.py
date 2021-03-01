from hata import Client
from hata.ext.commands import setup_ext_commands
from hata.ext.commands.helps.subterranean import SubterraneanHelpCommand

from bot_utils.shared_data import SEND_LOG, BOT_LOGS, MELON_MINT_PREFIX, RAN_FROM
from bot_utils.tools import colourfunc

MELON_MINT: Client

setup_ext_commands(MELON_MINT, MELON_MINT_PREFIX, default_category_name="Uncategorized",)
MELON_MINT.commands(SubterraneanHelpCommand(colourfunc), 'help',)

@MELON_MINT.events
async def ready(client):
    """
    Same for all clients
    
    Sends a message to log channel if the bot is ran from the hosting
    If it is ran from the local you can change it to send or not send in RAN_FROM variable
    """
    message = f'{client:f} logged in via {RAN_FROM[0]}'
    print(message)
    
    if SEND_LOG and RAN_FROM[1]:
        await client.message_create(BOT_LOGS, message)
