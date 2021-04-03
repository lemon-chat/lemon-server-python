# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Auth

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LoginResp(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLoginResp(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LoginResp()
        x.Init(buf, n + offset)
        return x

    # LoginResp
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LoginResp
    def Status(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # LoginResp
    def Token(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from Lemon.Auth.AuthToken import AuthToken
            obj = AuthToken()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def LoginRespStart(builder): builder.StartObject(2)
def LoginRespAddStatus(builder, status): builder.PrependUint16Slot(0, status, 0)
def LoginRespAddToken(builder, token): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(token), 0)
def LoginRespEnd(builder): return builder.EndObject()
