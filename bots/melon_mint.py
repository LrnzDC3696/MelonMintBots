from hata import Client
from hata.ext.commands import setup_ext_commands
from hata.ext.slash import setup_ext_slash
from hata.ext.commands.helps.subterranean import SubterraneanHelpCommand

from bot_utils.shared_data import BOT_LOGS, MELON_MINT_PREFIX, RED, RAN_FROM

MELON_MINT: Client

setup_ext_slash(MELON_MINT)
setup_ext_commands(MELON_MINT, MELON_MINT_PREFIX)
MELON_MINT.commands(SubterraneanHelpCommand(color=RED), 'help')

@MELON_MINT.events
async def ready(client):
    message = f'{client:f} logged in via {RAN_FROM}'
    await client.message_create(BOT_LOGS, message)
    print(message)
