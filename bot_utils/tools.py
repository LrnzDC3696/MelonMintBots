
def colourfunc(_client, message, _name):
    return message.author.color_at(message.guild)
    
async def GET_PREFIX(client, DATABASE, guild):
    prefix = await client.loop.run_in_executor(DATABASE.child(guild.id).child('bot settings').child('prefix'))
    return prefix

async def GET_HUMAN_COUNT(guild):
    return len([x for x in guild.users.values() if not x.is_bot])

async def EXECUTOR(client, function):
    return await client.loop.run_in_executor(function)
