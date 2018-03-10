from .config import client


class Functions:
    async def rmPrefix(content):
        content = content.strip('ﾠﾠ \t\n\r').lower()
        content_split = content.split(" ")

        return content.replace(content_split[0], "")

    async def nick_filter(member):
        trimed_nick = member.nick.strip('ﾠﾠ \t\n\r')
        user = await client.get_user_info(member.id)
        if trimed_nick != member.nick:
            await client.change_nickname(member, None)
