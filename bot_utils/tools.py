from difflib import get_close_matches 

async def closeMatches(patterns, word):
    """ 
    Function to find all close matches of  
    input string in given list of possible strings 
    """
    
async def get_human_count(guild):
    return len([x for x in guild.users.values() if not x.is_bot])
