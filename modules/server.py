from bot_utils.guild_data import SERVER_RULES, WELCOME_CHANNEL
from hata import Client

MMS: Client

@MMB.commands
async def rule(client, message, rule_number):
    the_rule = SERVER_RULES.get(rule_number)
    await client.message_create(message, the_rule if the_rule else 'Rule Not Found')
    
@MMB.events
async def guild_user_add(client, _ , user):
    if user.is_bot:
        return
    
    message = f'Welcome {user:m} please check <#717221907480576000> and <#717220941519781900> for more info on our current situation'
    await client.message_create(WELCOME_CHANNEL, message)
