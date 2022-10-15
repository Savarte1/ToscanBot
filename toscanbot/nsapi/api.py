import aiohttp
from aiolimiter import AsyncLimiter
from . import errors
from urllib import parse

NS_DOMAIN = "www.nationstates.net"
API_URL = ("https", NS_DOMAIN, "/cgi-bin/api.cgi")
NS_URL = ("https", NS_DOMAIN)

class NSApi:
    def __init__(self, agent: str):
        self._session = aiohttp.ClientSession()
        self._limiter = AsyncLimiter(40, 30)
        self.agent = agent

    async def close(self):
        await self._session.close()

    async def nsrequest(self, uri: str, data=False):
        if not self.agent:
            raise errors.NoAgentError
        headers = {"User-Agent": f"{self.agent}"}
        compiled_uri = f"https://www.nationstates.net/{uri}"
        async with self._limiter:
            async with self._session.get(compiled_uri, headers=headers) as response:
                if response.status == 200:
                    if data:
                        return await response.read()
                    else:
                        return await response.text()

