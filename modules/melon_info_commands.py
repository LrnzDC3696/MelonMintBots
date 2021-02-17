from hata import Client

MELON: Client

def get_user_info(message, user):
    the_user = user
    if not the_user:
        the_user = message.author
        
    return f'user {the_user}'

def get_role_info(message, role):
    if not role:
        return tell_usage
        
    return f'role {role}'

def get_server_info(message, server):
    the_server = server
    if not the_server:
        return tell_usage
        
    return f'server {server}'

def tell_usage(_):
    return 'does not exist this is how u use it blah blah blah'

REDIRECT = {
    'user':get_user_info,
    'role':get_role_info,
    'server':get_server_info
    }
    
@MELON.commands
async def info(client, message, first, second):
    bonk = await REDIRECT.get(first.lower(),tell_usage)(message, second)
    await client.message_create(message, bonk)
