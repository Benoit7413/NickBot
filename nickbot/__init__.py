import os
from os import environ
import sys
from nickbot.__version__ import __version__
import asyncio
from nickbot import classes
from nickbot.classes.config import client


def main():
    try:
        os.environ["DISCORD_TOKEN"]
    except KeyError:
        print('Please set the environment variable DISCORD_TOKEN')
        sys.exit(1)

    print("Runing NickBot version : " + __version__)
    print("Considering performances, the inability to remove owner messages "
          "this bot only listen to administratives messages from "
          "#nickboc_admin")

    client.run(os.environ["DISCORD_TOKEN"])
