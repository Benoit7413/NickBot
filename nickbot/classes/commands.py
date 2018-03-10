from .config import client
from .emojiflag import EmojiFlag
from .functions import Functions
# Commands defined functions should only have message arguments


class Commands:

    async def flag(message):
        code = await Functions.rmPrefix(message.content)
        user = await client.get_user_info(message.author.id)
        if code is "" and message.author.nick is not None:
            await client.change_nickname(message.author,
                                         EmojiFlag.remove(message.author.nick))
        elif message.author.nick is None:
            await client.change_nickname(message.author,
                                         EmojiFlag.add(user.name, code))
        else:
            await client.change_nickname(message.author,
                                         EmojiFlag.change(
                                             message.author.nick, code))
        await client.delete_message(message)
