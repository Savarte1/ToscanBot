import discord
from discord.ext import commands
from .nsapi import NSApi
from . import version
from typing import Optional
from .cogs.core import BotCore


class Toscan(commands.Bot):
    def __init__(self, settings: dict, *args, **kwargs):
        intents = discord.Intents.all()
        self.nsapi: Optional[NSApi] = None
        self.settings = settings
        self.agent: Optional[str] = None
        if settings["nationstates"]["agent"]:
            self.agent = f"{settings['UserAgent']} ToscanBot/{version}"
        super().__init__(intents=intents, command_prefix=settings["Prefix"], *args, **kwargs)

    async def setup_hook(self):
        self.nsapi = NSApi(self.agent)
        await self.add_cog(BotCore(self))

    async def close(self):
        await self.nsapi.close()
        await super().close()
