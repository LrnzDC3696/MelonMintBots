from hata import Client

from bot_utils.shared_data import BOT_LOGS, NIHONGO_QUEST
from bot_utils.tools import get_human_count

MELON_MINT: Client

@MELON_MINT.commands
async def test(client, message):
    bonk = await get_human_count(message.guild)
    await client.message_create(message, bonk)
#async def vote(owo):
#    message = f"{VOTERS_ROLE.mention} time to vote or else I will vote you out and make you suffer in space\nTo remove the voter role check out {ROLES_CHANNEL.mention}"
#    await Nekowo.message_create(VOTE_CHANNEL, message)

#async def bump(owo):
#    message = f"{BUMPERS_ROLE.mention} time to bump or I will bump you\nTo remove the bumper role check out {ROLES_CHANNEL.mention}"
#    await Nekowo.message_create(BUMP_CHANNEL, message)

#Nekowo.loop.cycle(timedelta(hours=12).total_seconds(), vote)
#Nekowo.loop.cycle(timedelta(hours=2).total_seconds(), bump)
#Nekowo.loop.cycle(5*60, update_channel)

@MELON_MINT.interactions(guild=NIHONGO_QUEST)
async def ping(client, event):
    """ping-pong"""
    return 'pong'
