
from hata import Client, Embed, sleep
from hata.ext.commands import checks

from bot_utils.shared_data import LINKS, SERVER_RULES, BLUE, MOD_ROLE
from bot_utils.faq_data import FAQ

MINT : Client

@MINT.commands(checks = checks.has_role(MOD_ROLE))
async def welcome(client, message):
    """Sends all the information needed for beginners"""
    
    #intro 
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'This channel contains everything you need to know')
        )
    
    await sleep(3)
    
    #rules
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'RULES')
        )
        
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'Rules',
            description = '\n'.join((f'**Rule {x}**\n{y}\n' for x, y in SERVER_RULES.items())) + '\nIf anyone is bothering you or you would like to report something please send a direct to our currently active mods but if our mods are the one bothering please direct message <@683006961788387368>'
            )
        )
        
    await sleep(3)
    
    #what channels are for
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'NAVIGATION')
        )
        
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'Navigation',
            description = """
<#716722197481390130>: Category where server related information are posted.\n
<#717200392840282154>: Category where Nihongo Quest Game related information are posted.\n
<#809346661343035442>: Category where we just chill out and talk over something fun!\n
<#717211219034898463>: Category where all the fun is!\n
<#717309484795428894>: Category where we study 日本語 and posts some of our good resources to others\n
<#717668394396286998>: Place to chill out and listen to music or even talk to other members!\n
"""
            )
        )
    
    await sleep(3)
    
    #what bots are for
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'BOTS')
        )
    
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'M-Bots',
            description = """
<@811236307211649064> bot is mostly for helping people in our server giving FAQs and welcoming people.\n
<@811242799877718026> bot is for moderating the server bonking bad users and managing server.\n
<@809281851650474005> bot is <@762335112368750602>'s pet he works for him and does the testing.\n

The source code is private for some reasons but if you want to contribute please dm <@762335112368750602> !
"""
            )
        )
    
    await sleep(3)
    
    #what to do if...
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'WHAT TO DO IF ...'
            )
        )
    
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'What to do if ...',
            description= """
**If I found a bug:** You can post it at <#747323336836644865> and call out an active mod.\n
**If I have questions:** You can ask them at <#717222563259875370> and we will help if we can.\n
**If I have a suggestion:** You can post your suggestion at <#809262950971473930> and react thumbs up and down. Then you can wait for results. \n
**If someone is inappropriate:** You can report then to our active mods but please send proof
            """
            )
        )
        
    await sleep(3)
    
    #what to do next
    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'WHAT IS NEXT?'
            )
        )

    await client.message_create(message.channel,
        Embed(
            color = BLUE,
            title = 'What is next?',
            description = """
Why not introduce yourself in <#717214286988050443>!\n
Start a conversation in <#717211320881250336> or <#809349050091569152>\n
Visit <#717200392840282154> to know more about the game and how to download it!
"""
            )
        )
        
    await client.message_delete(message)
    
@MINT.commands
async def faq(client, message, key):
    """
    Gives you the faq that you have given.
    If the faq isn't in the database you willll get a list of faq available.
    """
    try:
        embed = Embed(title=key.lower(), description=FAQ[key])
    
    except KeyError:
        embed = Embed(
            title=f'FAQ `{key}` not found',
            description=f'Available FAQs `{list(FAQ.keys())}`'
            )
    
    await client.message_create(message.channel, embed)

@MINT.commands
async def link(client, message, key):
    """
    Gives you the link that you need.
    If the link is not in the database you will get all of the links.
    """
    try:
        embed = Embed(description=f'**[{key.upper()}]({LINKS[key.upper()]})**'.lower())
    except KeyError:
        
        string = '\n'.join((f'**[{x}]({y})**'.lower() for x, y in sorted(LINKS.items())))
        
        embed = Embed(title='Links', description=string)
    
    await client.message_create(message.channel, embed)
