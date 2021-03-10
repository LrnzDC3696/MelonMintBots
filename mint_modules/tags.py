from hata import Client, now_as_id, Embed, sleep, User, id_to_time, chunkify
from hata.ext.commands import Pagination

from bot_utils.database import My_Database
from bot_utils.tools import executor , colourfunc


MINT : Client
MINT.command_processer.create_category('Tags',)

DB = My_Database.DATABASE

@MINT.commands.from_class
class tag:
    category = 'Tags'
    
    async def description(self, message):
        return Embed(
            title = 'tag',
            color = colourfunc(message = message),
            description = "Do `m!tag <name>` to find the given tag",
        )
        
    async def command(self, message, name):
        if not name:
            return 'Give me the name you baka!!!'
        tag_val = await executor(self, DB.child('Tags').child(name.lower()).get().val)
        
        if tag_val is None:
            msg = await self.message_create(message.channel, 'Tag not found')
            await sleep(69)
            await self.message_delete(msg)
            return

        if tag_val['embed']:
            await self.message_create(message.channel,
                Embed(
                    name.lower(),
                    tag_val['content'],
                    color = colourfunc(message),
                )
            )
        else:
            await self.message_create(message.channel, tag_val['content'], allowed_mentions=None)
        
        tag_val['uses'] += 1
        await executor(self, DB.child('Tags').child(name.lower()).set(tag_val).update)
    

@MINT.commands.from_class
class tag_create:
    separator = ('|')
    category = 'Tags'

    async def description(self, message):
        return Embed(
            title = 'tag-create',
            color = colourfunc(message = message),
            description = \
                'Creates a new tag for you'
                '\nDo `m!tag-create <name> | <value> | [anything if you dont want to embed]`',
        )
    
    async def command(self, message, name = None, content = None, emb = None):
        if not name or not content:
            return 'please fill the missing parameter'
        
        existing_tags = await executor(self, DB.child('Tags').shallow().get().val)
        
        if name.lower() in (existing_tags or []):
            return f"tag {name} already exist"
        del existing_tags
            
        data = {
            'content' : content,
            'owner'   : message.author.id,
            'id'      : now_as_id(),
            'uses'    : 0,
            'embed'   : True if emb is None else False,
        }
        
        await executor(self, DB.child('Tags').child(name.lower()).set(data).update)
        return 'Tag has been created'


@MINT.commands.from_class
class tag_info:
    category = 'Tags'
    
    async def description(self, message):
        return Embed(
            title = 'tag-info',
            color = colourfunc(message = message),
            description = "Do `m!tag-info <name>`",
        )
        
    async def command(self, message, name):
        if not name:
            return 'Give me the name you baka!!!'
        
        tag_data = await executor(self, DB.child('Tags').child(name.lower()).get().val)
        
        if tag_data is None:
            return "tag not found"
        
        owner = User.precreate(tag_data["owner"])
        return Embed(
            f"**Tag: {name}**",
            
            f"**Use Count** : {tag_data['uses']}"\
            f"\n**Created At**: {id_to_time(tag_data['id'])}"\
            f"\n**Created By**: <@!{owner.id}>",
            
            color = colourfunc(message),
        ).add_author(owner.avatar_url, owner.name)

@MINT.commands.from_class
class tag_all:
    category = 'Tags'
        
    async def description(self, message):
        return Embed(
            title = 'tag-all',
            color = colourfunc(message = message),
            description = "Do `m!tag <name>` to list all tag",
        )
    
    async def command(self, message):
        bonk = sorted(list((await executor(self, DB.child('Tags').shallow().get().val))\
            or ['We dont have tags for now']))
        
        color = colourfunc(message)
        pages = [Embed('Tags', tag_name, color=color) for tag_name in chunkify(bonk)]
        
        limit = len(pages)
        index = 0
        
        while index < limit:
            embed = pages[index]
            index += 1
            embed.add_footer(f'page {index}/{limit}')
        
        await Pagination(self, message.channel, pages)

@MINT.commands.from_class
class tag_del:
    category = 'Tags'
    
    async def description(self, message):
        return Embed(
            title = 'tag-del',
            color = colourfunc(message = message),
            description = "Do `m!tag-del <name>` to remove the given tag",
        )
    async def command(self, message, name):
        if not name:
            return 'Give me the name you baka!!!'
                   
        the_tag = await executor(self, DB.child('Tags').child(name.lower()).get().val)
        
        if the_tag is None:
            return 'Tag not found'
        
        if message.author.id in (self.owner.id, the_tag['owner']):
            await executor(self, DB.child('Tags').child(name.lower()).remove)
            return 'Tag has been deleted'
        
        return 'You can only remove your own tag unless you are my owner'
