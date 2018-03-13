import configparser
import discord
from .db import DbHandler

global Config, client


class ConfigHandler(object):

    admin_chan = str("nickbot_admin")

    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read('/etc/nickbot')
        self.db_msg = DbHandler.human_readable_return
        self.__db = DbHandler(self.__config['REDIS'])

    async def set(self, server, param, value):
        return await self.__db.set(server.id, param, value)

    async def get(self, server, param):
        return await self.__db.get(server.id, param)

    async def connected(self):
        return await self.__db.is_connected()


Config = ConfigHandler()
client = discord.Client()
