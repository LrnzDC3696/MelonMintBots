def colourfunc(message):
    return message.author.color_at(message.guild)
    
async def get_prefix(client, DATABASE, guild):
    prefix = await client.loop.run_in_executor(DATABASE.child(guild.id).child('bot settings').child('prefix'))
    return prefix

async def get_human_count(guild):
    return len([x for x in guild.users.values() if not x.is_bot])

async def executor(client, function):
    return await client.loop.run_in_executor(function)
