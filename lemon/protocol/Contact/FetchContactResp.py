# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Contact

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class FetchContactResp(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFetchContactResp(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FetchContactResp()
        x.Init(buf, n + offset)
        return x

    # FetchContactResp
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FetchContactResp
    def Status(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # FetchContactResp
    def UserContacts(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Lemon.Contact.UserContact import UserContact
            obj = UserContact()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FetchContactResp
    def UserContactsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FetchContactResp
    def UserContactsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # FetchContactResp
    def GroupContacts(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Lemon.Contact.GroupContact import GroupContact
            obj = GroupContact()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FetchContactResp
    def GroupContactsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FetchContactResp
    def GroupContactsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def FetchContactRespStart(builder): builder.StartObject(3)
def FetchContactRespAddStatus(builder, status): builder.PrependUint8Slot(0, status, 0)
def FetchContactRespAddUserContacts(builder, userContacts): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(userContacts), 0)
def FetchContactRespStartUserContactsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FetchContactRespAddGroupContacts(builder, groupContacts): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(groupContacts), 0)
def FetchContactRespStartGroupContactsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FetchContactRespEnd(builder): return builder.EndObject()