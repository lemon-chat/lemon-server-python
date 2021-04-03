
import asyncio
from typing import Any
from lemon.protocol.Auth import LoginReq, LoginResp
from lemon.protocol.Register import RegisterReq, RegisterResp


class Packet(object):
    packet_map = {
        0: LoginReq,
        1: LoginResp,
        2: RegisterReq,
        3: RegisterResp
    }
    def __init__(self, id: int, data: bytes):
        self.id = id
        self.data = data

    def get_bytes(self) -> bytes:
        out = bytearray()
        out += self.id.to_bytes(4, byteorder='big')
        out += len(self.data).to_bytes(4, byteorder='big')
        out += self.data
        return bytes(out)


class TypeStreamReader(object):
    def __init__(self, reader: asyncio.StreamWriter):
        self.reader = reader

    async def read_int32(self):
        out = bytearray()
        n = 4
        while n > 0:
            try:
                # self.request is the TCP socket connected to the client
                b = await self.reader.read(n)
                n -= len(b)
                out += b
            except asyncio.exceptions.IncompleteReadError:
                continue
        packid = int.from_bytes(bytes(out), byteorder='big')
        return packid

