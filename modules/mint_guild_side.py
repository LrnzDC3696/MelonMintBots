
from hata import Client, Embed, sleep, Permission
from hata.ext.commands import checks
from bot_utils.shared_data import LINKS, SERVER_RULES, BLUE, MOD_ROLE
from bot_utils.faq_data import FAQ

from bot_utils.command_handler import PERMISSION_CHECK_HANDLER
MINT : Client


def DRY(titles=None, descript=None):
    embedded = Embed(
        color = BLUE,
        title = titles,
        description = descript
    )
    return embedded

@MINT.commands(
    checks=checks.has_guild_permissions(
        Permission().update_by_keys(manage_guild = True),
        handler=PERMISSION_CHECK_HANDLER)
    )
async def welcome(client, message):
    """Sends all the information needed for beginners must have "manage guild" permission"""
    
    to_send = [
        ['This channel contains everything you need to know'], #Intro
        ['RULES'],
        ['Rules','\n'.join((f'**Rule {x}**\n{y}\n' for x, y in SERVER_RULES.items())) + '\nIf anyone is bothering you or you would like to report something please send a direct to our currently active mods but if our mods are the one bothering please direct message <@683006961788387368>'],
        ['NAVIGATION'],
        ['Navigation',"""
<#716722197481390130>: Category where server related information are posted.\n
<#717200392840282154>: Category where Nihongo Quest Game related information are posted.\n
<#809346661343035442>: Category where we just chill out and talk over something fun!\n
<#717211219034898463>: Category where all the fun is!\n
<#717309484795428894>: Category where we study 日本語 and posts some of our good resources to others\n
<#717668394396286998>: Place to chill out and listen to music or even talk to other members!\n
"""],
        ['BOTS'],
        ['M-Bots',"""
<@811236307211649064> bot is mostly for helping people in our server giving FAQs and welcoming people.\n
<@811242799877718026> bot is for moderating the server bonking bad users and managing server.\n
<@809281851650474005> bot is <@762335112368750602>'s pet he works for him and does the testing.\n

The source code is private for some reasons but if you want to contribute please dm <@762335112368750602> !
"""],
        ['WHAT TO DO IF'],
        ['What to do if...',"""
**If I found a bug:** You can post it at <#747323336836644865> and call out an active mod.\n
**If I have questions:** You can ask them at <#717222563259875370> and we will help if we can.\n
**If I have a suggestion:** You can post your suggestion at <#809262950971473930> and react thumbs up and down. Then you can wait for results. \n
**If someone is inappropriate:** You can report then to our active mods but please send proof
"""],
        ['WHAT IS NEXT'],
        ['What is next?',"""
Why not introduce yourself in <#717214286988050443>!\n
Start a conversation in <#717211320881250336> or <#809349050091569152>\n
Visit <#717200392840282154> to know more about the game and how to download it!
"""]
    ]
    
    for groups in to_send:
        await client.message_create(message.channel, DRY(*groups[:2]))
        await sleep(1)
    await client.message_delete(message)

@MINT.commands
async def link(client, message, key):
    """
    Gives you the link that you need.
    If the link is not in the database you will get all of the links.
    """
    try:
        embed = Embed(description=f'**[{key.upper()}]({LINKS[key.upper()]})**'.lower())
        await client.message_create(message.channel, embed)
    except KeyError:
        
        string = '\n'.join((f'**[{x}]({y})**'.lower() for x, y in sorted(LINKS.items())))
        
        embed = Embed(title='Nihongo Quest Links', description=string)
    
        await client.message_create(message.channel, embed)
