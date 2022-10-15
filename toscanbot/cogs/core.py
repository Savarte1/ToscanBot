from discord.ext import commands
from ..robot import Toscan


class BotCore(commands.Cog):

    def __init__(self, bot: Toscan):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx: commands.Context):
        await ctx.send("Shutting down...")
        await self.bot.close()