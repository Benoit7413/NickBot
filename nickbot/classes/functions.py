import re
from .config import client


class Functions:
    async def getPrefix(content):
        content = content.strip('ﾠﾠ \t\n\r').lower()
        content_split = content.split(" ")

        return content_split[0]

    async def rmPrefix(content):
        content = content.strip('ﾠﾠ \t\n\r').lower()
        content_split = content.split(" ")

        return content.replace(content_split[0], "")

    async def nick_filter(member):
        trimed_nick = member.nick.strip('ﾠﾠ \t\n\r')
        user = await client.get_user_info(member.id)
        if trimed_nick != member.nick:
            await client.change_nickname(member, None)

    async def ownerForbiden(message):
        user = await client.get_user_info(message.author.id)
        if user == message.server.owner:
            prefix = await Functions.getPrefix(message.content)
            await client.send_message(message.channel,
                                      'ERROR : Server owner can\'t use ' +
                                      prefix)
            return True
        return False

    async def getParams(content):
        regex = r"(?<=\"|\')([A-z0-9 ]+)(?=\"|\')|([[A-z0-9]+)"
        prefix = await Functions.getPrefix(content)
        result = re.finditer(regex, await Functions.rmPrefix(content))
        params = [match.group() for matchNum, match in enumerate(result)]
        return params
