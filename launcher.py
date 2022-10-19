#!/usr/bin/env python

from toscanbot import Toscan
import tomli
import asyncio
import discord
import logging

with open('config.toml', 'rb') as stream:
    BotSettings = tomli.load(stream)


async def main():
    discord.utils.setup_logging()
    bot = Toscan(BotSettings)
    async with bot:
        await bot.start(token=BotSettings["bot"]["token"])


try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass