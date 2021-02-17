from hata import Client
from hata.ext.commands import setup_ext_commands
from hata.ext.slash import setup_ext_slash
from hata.ext.commands.helps.subterranean import SubterraneanHelpCommand

from bot_utils.shared_data import SEND_LOG, BOT_LOGS, MELON_MINT_PREFIX, RED, RAN_FROM

MELON_MINT: Client

setup_ext_slash(MELON_MINT)
setup_ext_commands(MELON_MINT, MELON_MINT_PREFIX)
MELON_MINT.commands(SubterraneanHelpCommand(color=RED), 'help')

@MELON_MINT.events
async def ready(client):
    message = f'{client:f} logged in via {RAN_FROM[0]}'
    print(message)
    
    if not SEND_LOG and not RAN_FROM[1]:
        return
    await client.message_create(BOT_LOGS, message)


Todo = {
    'bot':[
        'add category in commands',
        'add change member count event',
        'add dm help command',
        'add reaction role',
        'add user info command',
        'add suggestion command',
        'add error event',
        'links commands'
        ],
    'bots':[
        'add auto mod event'
        'add filter words event',
        'add leveling',
        'add slash commands',
        'add moderation command',
        'add evalute command',
        'add snekbox command',
        'add image processing'
        ],
    'other':[
        'translation command',
        'global chat',
        'games',
        'gifs event',
        'music',
        'anime search',
        'reddit search',
        'google search',
        'leveling'
        ],
    'server':[
        'add welcome channel (information about the server)',
        'remove dm sent by the bot'
        ]
    }
    
@MELON_MINT.commands
async def todo(client, message, key):
    result = Todo.get(key) if Todo.get(key) else list(Todo.keys())
    await client.message_create(message, f'`{result}`')
    