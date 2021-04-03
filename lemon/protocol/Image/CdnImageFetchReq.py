# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Image

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CdnImageFetchReq(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCdnImageFetchReq(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CdnImageFetchReq()
        x.Init(buf, n + offset)
        return x

    # CdnImageFetchReq
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CdnImageFetchReq
    def Token(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from Lemon.Auth.AuthToken import AuthToken
            obj = AuthToken()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CdnImageFetchReq
    def Image(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from Lemon.Image.CdnImage import CdnImage
            obj = CdnImage()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def CdnImageFetchReqStart(builder): builder.StartObject(2)
def CdnImageFetchReqAddToken(builder, token): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(token), 0)
def CdnImageFetchReqAddImage(builder, image): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(image), 0)
def CdnImageFetchReqEnd(builder): return builder.EndObject()