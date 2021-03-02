
from hata import Client, Embed, sleep, DiscordException, ERROR_CODES

from bot_utils.shared_data import (LINKS, SERVER_RULES, BLUE, MEMBER_COUNT, NIHONGO_QUEST, WELCOME_N_RULES_CHANNEL,
    NAVIGATION_CHANNEL, GENERAL_CHANNEL)
from bot_utils.permission_handler import CHECK_MANAGE_GUILD
from bot_utils.tools import GET_HUMAN_COUNT


MINT : Client

async def update_user_count(_smth):
    """
    Updates the server count vc
    """
    member = await GET_HUMAN_COUNT(NIHONGO_QUEST)
    await MINT.channel_edit(MEMBER_COUNT, name = f"member count {member}")

MINT.loop.cycle(float(5*60), update_user_count)


MINT.command_processer.create_category('Server',)

@MINT.events
async def guild_user_add(client, guild , user):
    if user.is_bot:
        return
    
    private_channel = await client.channel_private_create(user)

    member = await GET_HUMAN_COUNT(guild)
    server_message = f'Welcome {user:m} you are the {member}th member!!!'
    welcome_message = (
        'Hello there!!!\n'
        f'Please read and follow the {WELCOME_N_RULES_CHANNEL:m} in our server.\n'
        f'Also check out {NAVIGATION_CHANNEL:m} to see what the channels are for.\n'
        'Have a fun stay at our server and good luck on learning Japanese!'
    )

    try:
        await client.message_create(private_channel, welcome_message)
    except DiscordException as brr:
        if brr.code == ERROR_CODES.cannot_message_user:
            server_message += f"\nSince I can't DM you I'll send the message here\n\n{welcome_message}"
    
    to_send = await client.message_create(GENERAL_CHANNEL, server_message)
    await sleep(60*5)
    await client.message_delete(to_send)

@MINT.commands(category = 'Server')
async def rule(client, message, rule_number):
    """
    Gives you the rule that you want
    """
    the_rule = SERVER_RULES.get(rule_number)
    embed = Embed(color = BLUE)
    embed.add_field(f'RULE {rule_number}', the_rule or "Does not Exist")
    return embed

@MINT.commands(category = 'Server')
async def link(client, message, key):
    """
    Gives you the link that you need.
    If the link is not in the database you will get all of the links.
    """
    try:
        return Embed(description = f'**[{key.upper()}]({LINKS[key.upper()]})**'.lower())
    except KeyError:
        string = '\n'.join((f'**[{x}]({y})**'.lower() for x, y in sorted(LINKS.items())))
        return Embed(title = 'Nihongo Quest Links', description = string)

@MINT.commands.from_class
class welcome:
    category = 'Server'
    checks = CHECK_MANAGE_GUILD
    
    async def description(self, message):
        prefix = self.command_processer.get_prefix_for(message)
        return Embed(
            title = 'Role Command',
            color = BLUE,
            description = (
                'Sends all the information needed for beginners\n'
                'Must have `manage guild` permission'
            ),
        ).add_footer(f'Usage: {prefix}welcome')

    async def command(self, message):
        await self.message_create(message.channel,
            Embed(title = 'This channel contains everything you need to know'))
        
        await self.message_create(message.channel, Embed(title = 'RULES'))
        await self.message_create(message.channel,
            Embed(
                title = 'Rules',
                color = BLUE,
                description = (
                    '\n'.join((f'**Rule {x}**\n{y}\n' for x, y in SERVER_RULES.items())) +
                    '\nIf anyone is bothering you or you would like to report something please send a direct to our mods'
                    '\nIf our mods are the one bothering please direct message <@683006961788387368>'
                )
            )
        )
        
        await sleep(1.69)
        
        await self.message_create(message.channel, Embed(title = 'NAVIGATION'))
        await self.message_create(message.channel, 
            Embed(
                title = 'Navigation',
                color = BLUE,
                description = (
                    '<#716722197481390130>: Category where server related information are posted.\n'
                    '<#717200392840282154>: Category where Nihongo Quest Game related information are posted.\n'
                    '<#809346661343035442>: Category where we just chill out and talk over something fun!\n'
                    '<#717211219034898463>: Category where all the fun is!\n'
                    '<#717309484795428894>: Category where we study 日本語 and posts some of our good resources to others\n'
                    '<#717668394396286998>: Place to chill out and listen to music or even talk to other members!\n'
                )
            )
        )
        
        await sleep(1.69)
        
        await self.message_create(message.channel, Embed(title = 'BOTS'))
        await self.message_create(message.channel, 
            Embed(
                title = 'Bots',
                color = BLUE,
                description = (
                    '<@811236307211649064> bot is mostly for helping people in our server giving FAQs and welcoming people.\n'
                    '<@811242799877718026> bot is for moderating the server bonking bad users and managing server.\n'
                    '<@809281851650474005> bot is <@762335112368750602>\'s pet he works for him and does the testing.\n'
                    'The source code is private for some reasons but if you want to contribute please dm <@762335112368750602> !'
                )
            )
        )
        
        await sleep(1.69)
        
        await self.message_create(message.channel, Embed(title = 'WHAT TO DO IF'))
        await self.message_create(message.channel, 
            Embed(
                title = 'What to do if...',
                color = BLUE,
                description = (
                    '**If I found a bug:** You can post it at <#747323336836644865> and call out an active mod.\n'
                    '**If I have questions:** You can ask them at <#717222563259875370> and we will help if we can.\n'
                    '**If I have a suggestion:** You can post your suggestion at <#809262950971473930> and react'
                        'thumbs up and down.Then you can wait for results. \n'
                    '**If someone is inappropriate:** You can report then to our active mods but please send proof'
                )
            )
        )
        
        await sleep(1.69)
        
        await self.message_create(message.channel, Embed(title = 'WHAT IS NEXT OWO'))
        await self.message_create(message.channel, 
            Embed(
                title = 'What\'s Next',
                color = BLUE,
                description = (
                    'Why not introduce yourself in <#717214286988050443>!\n'
                    'Start a conversation in <#717211320881250336> or <#809349050091569152>\n'
                    'Visit <#717200392840282154> to know more about the game and how to download it!'
                )
            )
        )
        await self.message_delete(message)
