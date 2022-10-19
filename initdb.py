from tortoise import Tortoise, run_async
import tomli
from toscanbot.dbsetup import geturl

with open('config.toml', 'rb') as stream:
    BotSettings = tomli.load(stream)


async def init():

    uri = geturl(BotSettings["postgres"])

    await Tortoise.init(
        db_url=uri,
        modules={'models': ['toscanbot.models']}
    )
    await Tortoise.generate_schemas()


run_async(init())