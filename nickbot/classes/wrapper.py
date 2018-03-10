from .config import client
from ..nickbot import NickBot


@client.event
async def on_ready():
    await NickBot.ready()


@client.event
async def on_message(message):
    await NickBot.message(message)


@client.event
async def on_member_update(before, after):
    await NickBot.member_update(before, after)


@client.event
async def on_member_join(member):
    await NickBot.member_join(member)
