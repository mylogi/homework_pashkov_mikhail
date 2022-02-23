import asyncio
import random
from asyncio import sleep
from typing import TypeAlias

import aiohttp

from config.init_logging import init_logging
from config.loggers import get_inner_logger

T_URL: TypeAlias = str
T_REQUEST_RESULT: TypeAlias = int


# class A:
#     def __enter__(self):
#         ...
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         ...
#
#     async def __aenter__(self):
#         ...
#
#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         ...


async def make_request(url: T_URL, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore) -> T_REQUEST_RESULT:
    logger = get_inner_logger()
    logger.info(f'start: {url}')

    async with semaphore:
        logger.info(f'before maked: {url}')
        async with session.get(url) as response:
            logger.info(f'request maked: {url}')
            result = response.status
            await sleep(random.randint(0, 10) / 10)

    logger.info(f'end: {url}')
    return result


async def main():
    urls: list[T_URL] = [f'https://example.com/{x}' for x in range(10)]

    semaphore = asyncio.BoundedSemaphore(3)

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[make_request(url=url, session=session, semaphore=semaphore) for url in urls]
        )

    print(results)


if __name__ == '__main__':
    init_logging()

    asyncio.run(main())
