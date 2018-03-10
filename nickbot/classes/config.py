import configparser
import discord

global client
client = discord.Client()


class Config(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
#       self.config.read('config.ini')
