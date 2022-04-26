import asyncio
import socket
from asyncio import AbstractEventLoop

import aiohttp

list_of_auth_users = []

users_data = {}


class Client:

    def __init__(self, connection):
        self.connection = connection
        self.user_name: str = ''
        self.password: str = ''
        self.authorized: bool = False


async def recive_data(client, loop):
    while data := await loop.sock_recv(client.connection, 1024):
        return data.decode()


async def chat(client, loop):
    while data := await recive_data(client, loop):
        await send_message(data)


async def echo(client: Client, loop: AbstractEventLoop) -> None:
    while data := await loop.sock_recv(client.connection, 1024):
        # await loop.sock_sendall(connection, data)
        await send_message(data.decode())


async def listen_for_connection(server_socket: socket,
                                loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        client = Client(connection)
        # list_of_auth_users.append(client)
        print(f"Got a connection from {address}")
        asyncio.create_task(authorization(client))
        # await authorization(client)

        # asyncio.create_task(echo(client, loop))
        # asyncio.create_task(chat(client, loop))


# async def send_message_to_everyone(message):
#     loop = asyncio.get_event_loop()
#     global list_of_auth_users
#     copy_list_of_connection = list_of_auth_users[:]
#     for client in list_of_auth_users:
#         try:
#             await loop.sock_sendall(client.connection, message.encode())
#         except Exception as e:
#             print(e)
#             copy_list_of_connection.remove(client)
#     list_of_auth_users = copy_list_of_connection[:]


async def send_message(message, client: Client = None):
    loop = asyncio.get_event_loop()
    global list_of_auth_users
    copy_list_of_connection = list_of_auth_users[:]
    if client is None:
        for user_name, client in users_data.items():
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
    # list_of_auth_users = copy_list_of_connection[:]


# async def authorization_first_variant(client: Client):
#     loop = asyncio.get_event_loop()
#     await send_message('Please enter your user name: ', client)
#     # while data := await loop.sock_recv(client.connection, 1024):
#     if client.user_name == '':
#         client.user_name = await recive_data(client, loop)
#         if client.user_name in users_data.keys():
#             await send_message('User name is already exists ', client)
#             client.user_name = ''
#             client.password = ''
#             await authorization(client)
#         await send_message('Please enter your password: ', client)
#     if client.password == '' and client.user_name != '':
#         client.password = await recive_data(client, loop)
#     if client.user_name in users_data.keys():
#         if client.password == users_data[client.user_name].password:
#             await send_message(f'Welcome {client.user_name}!', client)
#             client.authorized = True
#         else:
#             await send_message('Password is incorrect\n', client)
#             client.user_name = ''
#             client.password = ''
#             await authorization(client)
#     else:
#         await send_message(f'Welcome {client.user_name}!', client)
#         users_data[client.user_name] = client
#         print(f'{client.user_name} - {client.password}')
#         chat_task = asyncio.create_task(chat(client, asyncio.get_event_loop()))
#         # await chat_task
#         # list_of_auth_users.append(client)


async def authorization(client: Client):
    loop = asyncio.get_event_loop()
    n = 3
    while n > 0:
        await send_message('Please enter your user name: ', client)
        client.user_name = await recive_data(client, loop)
        await send_message('Please enter your password: ', client)
        client.password = await recive_data(client, loop)
        if client.user_name in users_data.keys() and client.password == users_data[client.user_name].password:
            await send_message(f'Welcome {client.user_name}', client)
            break
        elif client.user_name in users_data.keys() and client.password != users_data[client.user_name].password:
            n -= 1
            if n == 0:
                await send_message('Incorrect password. Try another time!', client)
            else:
                await send_message(f'Incorrect password. {n} tries left!', client)
        else:
            await send_message(f'Welcome {client.user_name}!', client)
            users_data[client.user_name] = client
            print(f'User name: {client.user_name}. Password: {client.password}')
            chat_task = asyncio.create_task(chat(client, asyncio.get_event_loop()))
            break


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
