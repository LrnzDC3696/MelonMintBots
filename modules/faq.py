from bot_utils.guild_data import LINKS

from hata import Client

MMB: Client

@MMB.commands
async def link(client, message, link_to_give):
    """Gives you your chosen link do `m!link` to list all links"""
    
    result = LINKS.get(link_to_give.upper())
    if not result:
        if link_to_give.upper() in ('ALL','LIST'):
            result = f'`{sorted(list(LINKS.keys()))}` are the links available to be chosen'
        
        if not result:
            await client.message_create(message, 'Link not found')
            
    await client.message_create(message, result)
    