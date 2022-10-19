from discord.ext import commands


def guildowner():
    async def predicate(ctx: commands.Context):
        return ctx.author.id == ctx.guild.owner.id

    return commands.check(predicate)

def admin():
    async def predicate(ctx: commands.Context):
        pass