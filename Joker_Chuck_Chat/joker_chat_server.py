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


async def echo(client: Client, loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(client.connection, 1024):
        # await loop.sock_sendall(connection, data)
        if client.user_name == '':
            await authorization(client, data)
        await send_message(data.decode())


async def listen_for_connection(server_socket: socket,
                                loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        client = Client(connection)
        list_of_connection.append(client)
        print(f"Got a connection from {address}")
        asyncio.create_task(authorization(client))
        asyncio.create_task(echo(client, loop))


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


async def authorization(client: Client, data=None):
    if data is None:
        await send_message('Please enter your user name: ', client)
    if client.user_name == '':
        client.user_name = data.decode()
        await send_message('Please enter your password: ', client)
    if client.password == '':
        client.password = data.decode()
    if client.user_name in users_data.keys():
        if client.password == users_data[client.user_name]:
            await send_message(f'Welcome {client.user_name}!', client)
        else:
            await send_message('Password is incorrect', client)
            await authorization(client)
    else:
        users_data[client.user_name] = client.password


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
