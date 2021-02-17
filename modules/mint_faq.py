
from hata import Client, Embed

from bot_utils.shared_data import LINKS
from bot_utils.faq_data import FAQ

MINT : Client

@MINT.commands
async def faq(client, message, key):
    
    try:
        embed = Embed(title=key.lower(), description=FAQ[key])
    except KeyError:
        embed = Embed(title=f'FAQ `{key}` not found', description=f'Available FAQs `{list(FAQ.keys())}`')
    
    await client.message_create(message.channel, embed)

@MINT.commands
async def link(client, message, key):
    try:
        embed = Embed(description=f'**[{key.upper()}]({LINKS[key.upper()]})**')
    except KeyError:
        
        generate = (f'**[{x}]({y})**' for x, y in sorted(LINKS.items()))
        string = '\n'.join('' + generates for generates in generate)
        
        embed = Embed(title='Links', description=string)
    
    await client.message_create(message.channel, embed)
