import asyncio
import socket
from asyncio import AbstractEventLoop

async def echo(connection:socket,loop:AbstractEventLoop)->None:
    while data:=await loop.sock_recv(connection,1024):
        if data==b"boom\r\n":
            raise Exception("unexpected network error")
        print(f"received {data}")
        await loop.sock_sendall(connection,data)

async def listen_for_connection(server_socket:socket,loop:AbstractEventLoop):
    while True:
        connection,address=await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f" got a conneciton from {address}")
        task=asyncio.create_task(echo(connection,loop))
        await task

async def main():
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    server_address=("127.0.0.1",8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connection(server_socket,asyncio.get_event_loop())

asyncio.run(main())
