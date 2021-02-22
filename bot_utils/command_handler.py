from hata import Embed

from .shared_data import RED

from datetime import datetime

def EMBED_TEMPLATE(user, titles=None, descript=None):
    embeded = Embed(
        color = RED,
        title = titles,
        description = descript,
        timestamp = datetime.utcnow()
    )
    embeded.add_footer(user.id)
    embeded.add_author(user.avatar_url, user.full_name)
    
    return embeded

#Checks
async def PERMISSION_CHECK_HANDLER(client, message, command, check):
    to_send = EMBED_TEMPLATE(
        user = message.author,
        titles = 'Permission Denied',
        descript = f"You must have the `{' '.join(permission_name.replace('_', ' ') for permission_name in check.permissions)}` permission to use `{command}` command"
    )
    msg = await client.message_create(message, to_send)
    await client.message_delete(message, msg)
    