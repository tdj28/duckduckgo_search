import asyncio
import logging
from typing import Dict, Generator, Optional

from .duckduckgo_search_async import AsyncDDGS

logger = logging.getLogger("duckduckgo_search.DDGS")

class DDGS(AsyncDDGS):
    def __init__(self, headers=None, proxies=None, timeout=10):
        super().__init__(headers, proxies, timeout)

    async def __aenter__(self) -> "DDGS":
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._asession.close()  # Close the async session


    async def _iter_over_async(self, ait) -> AsyncGenerator:
        async for obj in ait:
            yield obj

    async def text(self, *args, **kwargs) -> AsyncGenerator[Dict[str, Optional[str]], None]:
        return await self._iter_over_async(super().text(*args, **kwargs))

    async def images(self, *args, **kwargs) -> AsyncGenerator[Dict[str, Optional[str]], None]:
        async for item in super().images(*args, **kwargs):
            yield item

    async def videos(self, *args, **kwargs) -> AsyncGenerator[Dict[str, Optional[str]], None]:
        async for item in super().videos(*args, **kwargs):
            yield item

    async def news(self, *args, **kwargs) -> AsyncGenerator[Dict[str, Optional[str]], None]:
        async for item in super().news(*args, **kwargs):
            yield item

    async def answers(self, *args, **kwargs) -> AsyncGenerator[Dict[str, Optional[str]], None]:
        async for item in super().answers(*args, **kwargs):
            yield item

    async def suggestions(self, *args, **kwargs) -> AsyncGenerator[Dict[str, Optional[str]], None]:
        async for item in super().suggestions(*args, **kwargs):
            yield item

    async def maps(self, *args, **kwargs) -> AsyncGenerator[Dict[str, Optional[str]], None]:
        async for item in super().maps(*args, **kwargs):
            yield item

    async def translate(self, *args, **kwargs) -> Optional[Dict[str, Optional[str]]]:
        return await super().translate(*args, **kwargs)
