from nickbot import classes
from nickbot.classes.config import client
from nickbot.classes.config import Config
from nickbot.classes.commands import Commands
from nickbot.classes.functions import Functions


class NickBot:

    async def ready():
        print("Logged in as " + client.user.name + " (ID: " + client.user.id +
              ") \r\nConnected to " + str(len(client.servers)) + " servers " +
              "| Connected to " + str(len(set(client.get_all_members()))) +
              " users")
        print('Use this link to invite {}:'.format(client.user.name))
        print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&'
              'permissions=8'.format(client.user.id))

    async def message(message):
        if message.channel.name == Config.admin_chan:
            await Commands.admin(message)
        prefix = await Config.get(message.server, 'prefix')
        if type(prefix) is str:
            if message.content.startswith(prefix + 'flag'):
                await Commands.flag(message)
            if message.content.startswith(prefix + 'penguin'):
                await Commands.penguin(message)
            if message.content.startswith(prefix + 'curly'):
                await Commands.curly(message)

    async def member_update(before, after):
        if after.nick is not None:
            await Functions.nick_filter(after)

    async def member_join(member):
        await Functions.nick_filter(member)
