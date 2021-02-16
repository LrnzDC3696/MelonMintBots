from bot_utils.guild_data import SERVER_RULES, WELCOME_CHANNEL

from hata import Client, sleep, Embed

MMB: Client

# Update server status event

# every 1 hour Send message to start convo event

# Rules
# Embedify this;
@MMB.commands
async def rule(client, message, rule_number):
    the_rule = SERVER_RULES.get(rule_number)
    embed = Embed(color=0x1489B0)
    embed.add_field(f'RULE {rule_number}', the_rule)
    await client.message_create(message.channel, embed)

# Welcomes new users
# Direct Message this
@MMB.events
async def guild_user_add(client, _ , user):
    if user.is_bot:
        return
    
    #In DM
    
    
    #In Channel
    message = f'Welcome {user:m} please check <#717221907480576000> and <#717220941519781900> for more info on our current situation'
    to_send = await client.message_create(WELCOME_CHANNEL, message)
    await sleep(60*3)
    await client.message_delete(to_send)