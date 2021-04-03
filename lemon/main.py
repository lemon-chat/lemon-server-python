import socketserver
import flatbuffers
import asyncio

from lemon.protocol.Auth.HeartBeatReq import HeartBeatReq
from lemon.protocol.Auth.HeartBeatResp import HeartBeatResp
from lemon.protocol.Auth.LoginReq import LoginReq
from lemon.protocol.Auth.LoginResp import LoginResp

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Received message from {addr!r}")

    #print(f"Send: {message!r}")
    #writer.write(data)
    #await writer.drain()

    while True:
        try:
            # self.request is the TCP socket connected to the client
            packid_bytes = await reader.readexactly(4)
            packid = int.from_bytes(packid_bytes, byteorder='big')
            length_bytes = await reader.readexactly(4)
            length = int.from_bytes(length_bytes, byteorder='big')
            data = await reader.readexactly(length)
        except asyncio.exceptions.IncompleteReadError:
            continue

        # print(data)
        if packid == 0:
            pack = HeartBeatReq.GetRootAsHeartBeatReq(data, 0)
            print("收到心跳包")
        elif packid == 2:
            pack = LoginReq.GetRootAsLoginReq(data, 0)
            print(f'用户{pack.Username()}登入')
            print("收到登录包")
        else:
            raise Exception("未知包类型")

        # just send back the same data, but upper-cased
        # self.request.sendall(data.upper())
    print("Close the connection")
    writer.close()

async def start_server():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 3839)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

def main():
    asyncio.run(start_server())

