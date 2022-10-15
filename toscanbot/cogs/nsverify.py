from discord.ext import commands
import discord
from .. import robot


class NSVerify(commands.Cog):
    """Verification system for NationStates"""
    def __init__(self, bot: robot.Toscan):
        self.bot = bot

    # Commands

    @commands.command()
    async def verify(self, ctx: commands.Context, *, nation: str = None):
        pass

    @commands.command()
    async def drop(self, ctx: commands.Context, *, nation: str = None):
        pass


async def setup(bot: robot.Toscan):
    await bot.add_cog(NSVerify(bot))