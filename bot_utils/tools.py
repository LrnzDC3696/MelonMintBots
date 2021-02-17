
async def get_human_count(guild):
    return len([x for x in guild.users.values() if not x.is_bot])
