import asyncio
import socket
from asyncio import AbstractEventLoop

import aiohttp

list_of_connection = []

users_data = {}


class Client:

    def __init__(self, connection):
        self.connection = connection
        self.user_name: str = ''
        self.password: str = ''


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(connection, 1024):
        # await loop.sock_sendall(connection, data)
        await send_message(data.decode())


async def listen_for_connection(server_socket: socket,
                                loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        client = Client(connection)
        list_of_connection.append(client)
        print(f"Got a connection from {address}")
        await authorization(client)
        asyncio.create_task(echo(connection, loop))


# async def send_message_to_everyone(message):
#     loop = asyncio.get_event_loop()
#     global list_of_connection
#     copy_list_of_connection = list_of_connection[:]
#     for client in list_of_connection:
#         try:
#             await loop.sock_sendall(client.connection, message.encode())
#         except Exception as e:
#             print(e)
#             copy_list_of_connection.remove(client)
#     list_of_connection = copy_list_of_connection[:]


async def send_message(message, client: Client = None):
    loop = asyncio.get_event_loop()
    global list_of_connection
    copy_list_of_connection = list_of_connection[:]
    if client is None:
        for client in list_of_connection:
            try:
                await loop.sock_sendall(client.connection, message.encode())
            except Exception as e:
                print(e)
                copy_list_of_connection.remove(client)
    else:
        try:
            await loop.sock_sendall(client.connection, message.encode())
        except Exception as e:
            print(e)
            copy_list_of_connection.remove(client)
    list_of_connection = copy_list_of_connection[:]


async def authorization(client: Client):
    await send_message('test', client)


async def joke_by_chuck():
    url = "https://api.chucknorris.io/jokes/random"
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(url) as resp:
                raw = await resp.json()
                joke_value = raw['value']
                await send_message(joke_value)
                await asyncio.sleep(60)
                # print(resp.status)
                # print(await resp.text())


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8888)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    asyncio.create_task(joke_by_chuck())
    await listen_for_connection(server_socket, asyncio.get_event_loop())


asyncio.run(main())
