from hata import Client, sleep

from bot_utils.tools import get_human_count
from bot_utils.shared_data import NIHONGO_QUEST, MEMBER_COUNT

MELON_MINT: Client
    
async def update_user_count():
    member = await get_human_count(NIHONGO_QUEST)
    await MELON_MINT.channel_edit(MEMBER_COUNT, name=f"member count {member}")

MELON_MINT.loop.cycle(float(3*60), update_user_count)
