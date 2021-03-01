from hata import Embed, Permission, sleep
from hata.ext.commands import checks

from .shared_data import RED

from datetime import datetime

SECOND_DELAY = 10

def embed_template(user, titles=None, descript=None):
    """
    Template for error embeds
    """
    embeded = Embed(
        color = RED,
        title = titles,
        description = descript,
        timestamp   = datetime.utcnow()
    )
    embeded.add_footer(user.id)
    embeded.add_author(user.avatar_url, user.full_name)
    
    return embeded

async def send_wait_delete(client, message, text, delay = SECOND_DELAY):
    """
    Sends the given data and deletes it after the seconds given defaults to 10
    """
    msg = await client.message_create(message, text)
    await sleep(delay)
    await client.message_delete(message, msg)
    
#HANDLER

async def NO_PERMISSION_HANDLER(client, message, command, check):
    to_send = embed_template(
        user     = message.author,
        titles   = 'Permission Denied',
        descript = f"You must have the `"
            f"{' '.join(permission_name.replace('_',' ') for permission_name in check.permissions)}"
            f"` permission to use `{command}` command"
    )
    send_wait_delete(client, message, to_send)

#CHECKS

CHECK_MANAGE_GUILD = checks.has_guild_permissions(
    Permission().update_by_keys(manage_guild = True),
    handler=NO_PERMISSION_HANDLER,
)
