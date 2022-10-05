import discord
from discord.ext import commands
import aiohttp


class ToscanBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.all()
        super().__init__(intents=intents,*args, **kwargs)
        self.ns_session = aiohttp.ClientSession()