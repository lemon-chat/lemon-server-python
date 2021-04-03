# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Image

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CdnImageUploadCheckResp(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCdnImageUploadCheckResp(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CdnImageUploadCheckResp()
        x.Init(buf, n + offset)
        return x

    # CdnImageUploadCheckResp
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CdnImageUploadCheckResp
    def Status(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # CdnImageUploadCheckResp
    def Image(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from Lemon.Image.CdnImage import CdnImage
            obj = CdnImage()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def CdnImageUploadCheckRespStart(builder): builder.StartObject(2)
def CdnImageUploadCheckRespAddStatus(builder, status): builder.PrependUint8Slot(0, status, 0)
def CdnImageUploadCheckRespAddImage(builder, image): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(image), 0)
def CdnImageUploadCheckRespEnd(builder): return builder.EndObject()