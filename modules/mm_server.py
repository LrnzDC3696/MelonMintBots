from hata import Client, sleep

from bot_utils.tools import get_human_count
from bot_utils.guild_data import NIHONGO_QUEST, MEMBER_COUNT

MELON_MINT: Client
    
async def update_user_count(something):
    print(something , '\nNOOOOO\n')
    member = await get_human_count(NIHONGO_QUEST)
    print(member , '\nNOOOOO\n')
    await MELON_MINT.channel_edit(MEMBER_COUNT, name=f"member count {member}")
    await sleep(10)

#MELON.loop.cycle(float(10), update_user_count)

# every 1 hour Send message to start convo event
