from hata import Client, Embed
from hata.ext.commands import setup_ext_commands
from hata.ext.slash import setup_ext_slash
from hata.ext.commands.helps.subterranean import SubterraneanHelpCommand

from bot_utils.shared_data import SEND_LOG, BOT_LOGS, MINT_PREFIX, RAN_FROM, NIHONGO_QUEST

MINT: Client

setup_ext_commands(MINT, MINT_PREFIX, default_category_name="Uncategorized",)
setup_ext_slash(MINT)

MINT.commands(SubterraneanHelpCommand(
        lambda _client, msg, _name: msg.author.color_at(msg.guild)
    ),'help',
)

@MINT.events
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

@MINT.interactions(guild = NIHONGO_QUEST)
async def perms(client, event):
    """Shows your permissions."""
    user_permissions = event.user_permissions
    if user_permissions:
        description = '\n'.join(permission_name.replace('_', '-') for permission_name in user_permissions)
    else:
        description = '*none*'
    
    user = event.user
    return Embed('Permissions', description).add_author(user.avatar_url, user.full_name)
