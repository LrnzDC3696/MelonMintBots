from hata import Client
from hata.discord.channel import ChannelPrivate

MELON_MINT : Client

def take_suggestion():
    pass

def connect_to_mods():
    pass

@MELON_MINT.events
async def message_create(client, message):
    if message.author.is_bot:
        return
    
    if not isinstance(message.channel, ChannelPrivate):
        return
        
    await client.message_create(message, message.content)
