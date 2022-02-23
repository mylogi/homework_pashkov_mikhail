import asyncio

import aiohttp


async def main():
    url = 'https://example.com/1'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            # print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print(html)


if __name__ == '__main__':
    asyncio.run(main())
