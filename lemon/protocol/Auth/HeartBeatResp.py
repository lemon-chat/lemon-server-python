# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Auth

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class HeartBeatResp(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsHeartBeatResp(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = HeartBeatResp()
        x.Init(buf, n + offset)
        return x

    # HeartBeatResp
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def HeartBeatRespStart(builder): builder.StartObject(0)
def HeartBeatRespEnd(builder): return builder.EndObject()
