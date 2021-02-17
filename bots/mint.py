from hata import Client, sleep, DiscordException, ERROR_CODES
from hata.ext.commands import setup_ext_commands
from hata.ext.slash import setup_ext_slash
from hata.ext.commands.helps.subterranean import SubterraneanHelpCommand

from bot_utils.shared_data import BOT_LOGS, MINT_PREFIX, RAN_FROM, RED, RULES_CHANNEL, NAVIGATION_CHANNEL, WELCOME_CHANNEL
from bot_utils.tools import get_human_count
MINT: Client

setup_ext_slash(MINT)
setup_ext_commands(MINT, MINT_PREFIX)
MINT.commands(SubterraneanHelpCommand(color=RED), 'help')

@MINT.events
async def ready(client):
    message = f'{client:f} logged in via {RAN_FROM}'
    await client.message_create(BOT_LOGS, message)
    print(message)

# Welcomer
@MINT.events
async def guild_user_add(client, guild , user):
    if user.is_bot:
        return
    
    private_channel = await client.channel_private_create(user)

    member = await get_human_count(guild)
    server_message = f'Welcome {user:m} you are the {member}th member!!!'
    welcome_message = f"""
Hello there!!!
Please follow the {RULES_CHANNEL:m} in our server.
Also check out {NAVIGATION_CHANNEL:m} to see what the channels are for.
"""

    try:
        await client.message_create(private_channel, welcome_message)
    except DiscordException as brr:
        if brr.code == ERROR_CODES.cannot_message_user:
            server_message += f'\nSince I can\'t DM you I\'ll send the message here \n\n{welcome_message}'
    
    to_send = await client.message_create(WELCOME_CHANNEL, server_message)
    await sleep(60*3)
    await client.message_delete(to_send)
