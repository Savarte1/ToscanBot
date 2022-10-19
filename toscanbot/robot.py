import discord
from discord.ext import commands
from .nsapi import NSApi
from . import version
from tortoise import Tortoise
from typing import Optional
from .dbsetup import geturl


class Toscan(commands.Bot):
    def __init__(self, settings: dict, *args, **kwargs):
        intents = discord.Intents.all()
        self.nsapi: Optional[NSApi] = None
        self.settings = settings
        self.agent: Optional[str] = None
        agent = settings["nationstates"]["agent"]
        if agent:
            self.agent = f"{agent} ToscanBot/{version}"
        super().__init__(intents=intents, command_prefix=settings["bot"]["prefix"], *args, **kwargs)

    async def setup_hook(self):
        self.nsapi = NSApi(self.agent)
        uri = geturl(self.settings["postgres"])
        await Tortoise.init(
            db_url=uri,
            modules={'models': ['models']}
        )
        await self.add_cog(BotCore(self))

    async def close(self):
        await self.nsapi.close()
        await Tortoise.close_connections()
        await super().close()


class BotCore(commands.Cog):

    def __init__(self, bot: Toscan):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx: commands.Context):
        await ctx.send("Shutting down...")
        await self.bot.close()

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, cog: str):
        try:
            await self.bot.reload_extension(cog)
        except commands.ExtensionNotLoaded:
            await ctx.send(f"Failed to reload cog: {cog}")
        else:
            await ctx.send(f"Reloaded {cog}")
