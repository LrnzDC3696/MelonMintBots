from hata import Client, Embed
from hata.ext.commands import setup_ext_commands
from hata.ext.slash import setup_ext_slash
from hata.ext.commands.helps.subterranean import SubterraneanHelpCommand

from bot_utils.shared_data import SEND_LOG, BOT_LOGS, MELON_PREFIX, RED, RAN_FROM, BLUE, SERVER_RULES

MELON: Client

setup_ext_slash(MELON)
setup_ext_commands(MELON, MELON_PREFIX)
MELON.commands(SubterraneanHelpCommand(color=RED), 'help')

@MELON.events
async def ready(client):
    message = f'{client:f} logged in via {RAN_FROM[0]}'
    print(message)
    
    if not SEND_LOG and not RAN_FROM[1]:
        return
    await client.message_create(BOT_LOGS, message)
    

# Rules
@MELON.commands
async def rule(client, message, rule_number):
    the_rule = SERVER_RULES.get(rule_number)
    embed = Embed(color=BLUE)
    embed.add_field(f'RULE {rule_number}', the_rule if the_rule else "Does not Exist")
    await client.message_create(message.channel, embed)
    await client.message_delete(message)
    