import asyncio
from concurrent.futures import ThreadPoolExecutor


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    await asyncio.gather(reader_task(reader), writer_task(writer))
    print('Close the connection')
    writer.close()


async def reader_task(reader):
    while True:
        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')


async def writer_task(writer):
    while True:
        message = await ainput('->')
        writer.write(message.encode())
        # await asyncio.sleep(5)


async def ainput(prompt: str = "") -> str:
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, input, prompt)


asyncio.run(tcp_echo_client('Hello World!'))
