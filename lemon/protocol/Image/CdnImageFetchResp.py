# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Image

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CdnImageFetchResp(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCdnImageFetchResp(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CdnImageFetchResp()
        x.Init(buf, n + offset)
        return x

    # CdnImageFetchResp
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CdnImageFetchResp
    def Status(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # CdnImageFetchResp
    def Content(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # CdnImageFetchResp
    def ContentAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # CdnImageFetchResp
    def ContentLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CdnImageFetchResp
    def ContentIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def CdnImageFetchRespStart(builder): builder.StartObject(2)
def CdnImageFetchRespAddStatus(builder, status): builder.PrependUint8Slot(0, status, 0)
def CdnImageFetchRespAddContent(builder, content): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(content), 0)
def CdnImageFetchRespStartContentVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def CdnImageFetchRespEnd(builder): return builder.EndObject()