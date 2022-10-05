import aiohttp
from aiolimiter import AsyncLimiter


class NSApi:
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.limiter = AsyncLimiter(40, 30)

    async def close(self):
        await self.session.close()
