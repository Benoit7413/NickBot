from .config import client
from .config import Config
from .emojiflag import EmojiFlag
from .functions import Functions
# Commands defined functions should only have message arguments


class Commands:

    async def flag(message):
        if await Functions.ownerForbiden(message):
            return False
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

    async def admin(message):
        params = await Functions.getParams(message.content)
        if message.content.startswith('.get'):
            try:
                key = params[0]
            except Exception:
                await client.send_message(message.channel,
                                          'Usage .get key')
                return False

            tmp = await client.send_message(message.channel,
                                            'Getting ' + key.upper() +
                                            ' ...')
            await Commands.msg_db_status(tmp)
            result = await Config.get(message.server, key)
            if result in Config.db_msg:
                bot_message = Config.db_msg[result].format(key=key.upper())
            else:
                bot_message = params[0].upper() + ' : ' + str(result)
            await client.edit_message(tmp,
                                      bot_message)
        if message.content.startswith('.set'):
            try:
                key = params[0]
                value = params[1]
            except Exception:
                await client.send_message(message.channel,
                                          'Usage .set key value')
                return False

            tmp = await client.send_message(message.channel,
                                            'Setting ' + key.upper() +
                                            ' to ' + value + ' ...')
            await Commands.msg_db_status(tmp)
            result = await Config.set(message.server, key, params[1])
            if result in Config.db_msg:
                bot_message = Config.db_msg[result].format(key=key.upper(),
                                                           value=value)
            else:
                bot_message = "Unknown return : " + result
            await client.edit_message(tmp,
                                      bot_message)

    async def msg_db_status(tmp_message):
        if not await Config.connected():
            await client.edit_message(tmp_message,
                                      tmp_message.content +
                                      "\r\n[Not connected to DB, "
                                      "message may be lost]")
