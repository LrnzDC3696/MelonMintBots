from hata import Client, Embed

from bot_utils.shared_data import FREE_ROLES, BLUE
from bot_utils.tools import colourfunc
MELON: Client

MELON.command_processer.create_category('Roles',)

@MELON.commands.from_class
class role:
    category = 'Roles'
    
    async def description(self, message):
        prefix = self.command_processer.get_prefix_for(message)
        return Embed(
            title = 'Role Command',
            color = colourfunc(self, message, message.guild),
            description = (
                'Gives or removes the given role\n'
                f'To list all role do `{prefix}role all`'
            ),
        ).add_footer(f'Usage: {prefix}role <role-name> | <all>')
    
    async def command(self, message, role_to_give):
        the_role = FREE_ROLES.get(role_to_give.upper())
        
        if not the_role or role_to_give.upper() in ('ALL','LIST'):

            to_send = (
                'Sorry I cannot find that role\n'
                f'`{sorted(list(FREE_ROLES.keys()))}` are the roles available to be chosen'
            )
            return to_send
        
        if message.author.has_role(the_role):
            await self.user_role_delete(message.author, the_role)
            result = f'The role {the_role} has been removed'
    
        else:
            await self.user_role_add(message.author, the_role)
            result = f'The role {the_role} has been given'
        
        return result
