from bot_utils.guild_data import FREE_ROLES, NIHONGO_QUEST

from hata import Client

MMB: Client

@MMB.commands
async def role(client, message, role_to_give):
    """Gives you your chosen role"""
     
    the_role = FREE_ROLES.get(role_to_give.upper())
    
    if not the_role:
        if role_to_give.upper() in ('ALL','LIST'):
            to_send = f'`{sorted(list(FREE_ROLES.keys()))}` are the roles available to be chosen'
            await client.message_create(message, to_send)
            return
        
        await client.message_create(message, 'Sorry I cannot find that role')
        return
    
    if message.author.has_role(the_role):
        await client.user_role_delete(message.author, the_role, None)
        result = f'The role {the_role} has been removed'

    else:
        await client.user_role_add(message.author, the_role, None)
        result = f'The role {the_role} has been given'

    await client.message_create(message, result)
    