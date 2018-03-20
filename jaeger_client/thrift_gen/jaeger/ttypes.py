#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,tornado
#
from six.moves import xrange

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TagType(object):
  STRING = 0
  DOUBLE = 1
  BOOL = 2
  LONG = 3
  BINARY = 4

  _VALUES_TO_NAMES = {
    0: "STRING",
    1: "DOUBLE",
    2: "BOOL",
    3: "LONG",
    4: "BINARY",
  }

  _NAMES_TO_VALUES = {
    "STRING": 0,
    "DOUBLE": 1,
    "BOOL": 2,
    "LONG": 3,
    "BINARY": 4,
  }

class SpanRefType(object):
  CHILD_OF = 0
  FOLLOWS_FROM = 1

  _VALUES_TO_NAMES = {
    0: "CHILD_OF",
    1: "FOLLOWS_FROM",
  }

  _NAMES_TO_VALUES = {
    "CHILD_OF": 0,
    "FOLLOWS_FROM": 1,
  }


class Tag(object):
  """
  Attributes:
   - key
   - vType
   - vStr
   - vDouble
   - vBool
   - vLong
   - vBinary
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'key', None, None, ), # 1
    (2, TType.I32, 'vType', None, None, ), # 2
    (3, TType.STRING, 'vStr', None, None, ), # 3
    (4, TType.DOUBLE, 'vDouble', None, None, ), # 4
    (5, TType.BOOL, 'vBool', None, None, ), # 5
    (6, TType.I64, 'vLong', None, None, ), # 6
    (7, TType.STRING, 'vBinary', None, None, ), # 7
  )

  def __init__(self, key=None, vType=None, vStr=None, vDouble=None, vBool=None, vLong=None, vBinary=None,):
    self.key = key
    self.vType = vType
    self.vStr = vStr
    self.vDouble = vDouble
    self.vBool = vBool
    self.vLong = vLong
    self.vBinary = vBinary

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.key = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.vType = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.vStr = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.vDouble = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.vBool = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.vLong = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.vBinary = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Tag')
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.STRING, 1)
      oprot.writeString(self.key)
      oprot.writeFieldEnd()
    if self.vType is not None:
      oprot.writeFieldBegin('vType', TType.I32, 2)
      oprot.writeI32(self.vType)
      oprot.writeFieldEnd()
    if self.vStr is not None:
      oprot.writeFieldBegin('vStr', TType.STRING, 3)
      oprot.writeString(self.vStr)
      oprot.writeFieldEnd()
    if self.vDouble is not None:
      oprot.writeFieldBegin('vDouble', TType.DOUBLE, 4)
      oprot.writeDouble(self.vDouble)
      oprot.writeFieldEnd()
    if self.vBool is not None:
      oprot.writeFieldBegin('vBool', TType.BOOL, 5)
      oprot.writeBool(self.vBool)
      oprot.writeFieldEnd()
    if self.vLong is not None:
      oprot.writeFieldBegin('vLong', TType.I64, 6)
      oprot.writeI64(self.vLong)
      oprot.writeFieldEnd()
    if self.vBinary is not None:
      oprot.writeFieldBegin('vBinary', TType.STRING, 7)
      oprot.writeString(self.vBinary)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.key is None:
      raise TProtocol.TProtocolException(message='Required field key is unset!')
    if self.vType is None:
      raise TProtocol.TProtocolException(message='Required field vType is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.key)
    value = (value * 31) ^ hash(self.vType)
    value = (value * 31) ^ hash(self.vStr)
    value = (value * 31) ^ hash(self.vDouble)
    value = (value * 31) ^ hash(self.vBool)
    value = (value * 31) ^ hash(self.vLong)
    value = (value * 31) ^ hash(self.vBinary)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Log(object):
  """
  Attributes:
   - timestamp
   - fields
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'timestamp', None, None, ), # 1
    (2, TType.LIST, 'fields', (TType.STRUCT,(Tag, Tag.thrift_spec)), None, ), # 2
  )

  def __init__(self, timestamp=None, fields=None,):
    self.timestamp = timestamp
    self.fields = fields

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.timestamp = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.fields = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = Tag()
            _elem5.read(iprot)
            self.fields.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Log')
    if self.timestamp is not None:
      oprot.writeFieldBegin('timestamp', TType.I64, 1)
      oprot.writeI64(self.timestamp)
      oprot.writeFieldEnd()
    if self.fields is not None:
      oprot.writeFieldBegin('fields', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.fields))
      for iter6 in self.fields:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.timestamp is None:
      raise TProtocol.TProtocolException(message='Required field timestamp is unset!')
    if self.fields is None:
      raise TProtocol.TProtocolException(message='Required field fields is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.timestamp)
    value = (value * 31) ^ hash(self.fields)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class SpanRef(object):
  """
  Attributes:
   - refType
   - traceIdLow
   - traceIdHigh
   - spanId
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'refType', None, None, ), # 1
    (2, TType.I64, 'traceIdLow', None, None, ), # 2
    (3, TType.I64, 'traceIdHigh', None, None, ), # 3
    (4, TType.I64, 'spanId', None, None, ), # 4
  )

  def __init__(self, refType=None, traceIdLow=None, traceIdHigh=None, spanId=None,):
    self.refType = refType
    self.traceIdLow = traceIdLow
    self.traceIdHigh = traceIdHigh
    self.spanId = spanId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.refType = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.traceIdLow = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.traceIdHigh = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.spanId = iprot.readI64()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SpanRef')
    if self.refType is not None:
      oprot.writeFieldBegin('refType', TType.I32, 1)
      oprot.writeI32(self.refType)
      oprot.writeFieldEnd()
    if self.traceIdLow is not None:
      oprot.writeFieldBegin('traceIdLow', TType.I64, 2)
      oprot.writeI64(self.traceIdLow)
      oprot.writeFieldEnd()
    if self.traceIdHigh is not None:
      oprot.writeFieldBegin('traceIdHigh', TType.I64, 3)
      oprot.writeI64(self.traceIdHigh)
      oprot.writeFieldEnd()
    if self.spanId is not None:
      oprot.writeFieldBegin('spanId', TType.I64, 4)
      oprot.writeI64(self.spanId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.refType is None:
      raise TProtocol.TProtocolException(message='Required field refType is unset!')
    if self.traceIdLow is None:
      raise TProtocol.TProtocolException(message='Required field traceIdLow is unset!')
    if self.traceIdHigh is None:
      raise TProtocol.TProtocolException(message='Required field traceIdHigh is unset!')
    if self.spanId is None:
      raise TProtocol.TProtocolException(message='Required field spanId is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.refType)
    value = (value * 31) ^ hash(self.traceIdLow)
    value = (value * 31) ^ hash(self.traceIdHigh)
    value = (value * 31) ^ hash(self.spanId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Span(object):
  """
  Attributes:
   - traceIdLow
   - traceIdHigh
   - spanId
   - parentSpanId
   - operationName
   - references
   - flags
   - startTime
   - duration
   - tags
   - logs
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'traceIdLow', None, None, ), # 1
    (2, TType.I64, 'traceIdHigh', None, None, ), # 2
    (3, TType.I64, 'spanId', None, None, ), # 3
    (4, TType.I64, 'parentSpanId', None, None, ), # 4
    (5, TType.STRING, 'operationName', None, None, ), # 5
    (6, TType.LIST, 'references', (TType.STRUCT,(SpanRef, SpanRef.thrift_spec)), None, ), # 6
    (7, TType.I32, 'flags', None, None, ), # 7
    (8, TType.I64, 'startTime', None, None, ), # 8
    (9, TType.I64, 'duration', None, None, ), # 9
    (10, TType.LIST, 'tags', (TType.STRUCT,(Tag, Tag.thrift_spec)), None, ), # 10
    (11, TType.LIST, 'logs', (TType.STRUCT,(Log, Log.thrift_spec)), None, ), # 11
  )

  def __init__(self, traceIdLow=None, traceIdHigh=None, spanId=None, parentSpanId=None, operationName=None, references=None, flags=None, startTime=None, duration=None, tags=None, logs=None,):
    self.traceIdLow = traceIdLow
    self.traceIdHigh = traceIdHigh
    self.spanId = spanId
    self.parentSpanId = parentSpanId
    self.operationName = operationName
    self.references = references
    self.flags = flags
    self.startTime = startTime
    self.duration = duration
    self.tags = tags
    self.logs = logs

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.traceIdLow = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.traceIdHigh = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.spanId = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.parentSpanId = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.operationName = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.references = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = SpanRef()
            _elem12.read(iprot)
            self.references.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.flags = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.startTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.duration = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.LIST:
          self.tags = []
          (_etype16, _size13) = iprot.readListBegin()
          for _i17 in xrange(_size13):
            _elem18 = Tag()
            _elem18.read(iprot)
            self.tags.append(_elem18)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.LIST:
          self.logs = []
          (_etype22, _size19) = iprot.readListBegin()
          for _i23 in xrange(_size19):
            _elem24 = Log()
            _elem24.read(iprot)
            self.logs.append(_elem24)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Span')
    if self.traceIdLow is not None:
      oprot.writeFieldBegin('traceIdLow', TType.I64, 1)
      oprot.writeI64(self.traceIdLow)
      oprot.writeFieldEnd()
    if self.traceIdHigh is not None:
      oprot.writeFieldBegin('traceIdHigh', TType.I64, 2)
      oprot.writeI64(self.traceIdHigh)
      oprot.writeFieldEnd()
    if self.spanId is not None:
      oprot.writeFieldBegin('spanId', TType.I64, 3)
      oprot.writeI64(self.spanId)
      oprot.writeFieldEnd()
    if self.parentSpanId is not None:
      oprot.writeFieldBegin('parentSpanId', TType.I64, 4)
      oprot.writeI64(self.parentSpanId)
      oprot.writeFieldEnd()
    if self.operationName is not None:
      oprot.writeFieldBegin('operationName', TType.STRING, 5)
      oprot.writeString(self.operationName)
      oprot.writeFieldEnd()
    if self.references is not None:
      oprot.writeFieldBegin('references', TType.LIST, 6)
      oprot.writeListBegin(TType.STRUCT, len(self.references))
      for iter25 in self.references:
        iter25.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.flags is not None:
      oprot.writeFieldBegin('flags', TType.I32, 7)
      oprot.writeI32(self.flags)
      oprot.writeFieldEnd()
    if self.startTime is not None:
      oprot.writeFieldBegin('startTime', TType.I64, 8)
      oprot.writeI64(self.startTime)
      oprot.writeFieldEnd()
    if self.duration is not None:
      oprot.writeFieldBegin('duration', TType.I64, 9)
      oprot.writeI64(self.duration)
      oprot.writeFieldEnd()
    if self.tags is not None:
      oprot.writeFieldBegin('tags', TType.LIST, 10)
      oprot.writeListBegin(TType.STRUCT, len(self.tags))
      for iter26 in self.tags:
        iter26.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.logs is not None:
      oprot.writeFieldBegin('logs', TType.LIST, 11)
      oprot.writeListBegin(TType.STRUCT, len(self.logs))
      for iter27 in self.logs:
        iter27.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.traceIdLow is None:
      raise TProtocol.TProtocolException(message='Required field traceIdLow is unset!')
    if self.traceIdHigh is None:
      raise TProtocol.TProtocolException(message='Required field traceIdHigh is unset!')
    if self.spanId is None:
      raise TProtocol.TProtocolException(message='Required field spanId is unset!')
    if self.parentSpanId is None:
      raise TProtocol.TProtocolException(message='Required field parentSpanId is unset!')
    if self.operationName is None:
      raise TProtocol.TProtocolException(message='Required field operationName is unset!')
    if self.flags is None:
      raise TProtocol.TProtocolException(message='Required field flags is unset!')
    if self.startTime is None:
      raise TProtocol.TProtocolException(message='Required field startTime is unset!')
    if self.duration is None:
      raise TProtocol.TProtocolException(message='Required field duration is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.traceIdLow)
    value = (value * 31) ^ hash(self.traceIdHigh)
    value = (value * 31) ^ hash(self.spanId)
    value = (value * 31) ^ hash(self.parentSpanId)
    value = (value * 31) ^ hash(self.operationName)
    value = (value * 31) ^ hash(self.references)
    value = (value * 31) ^ hash(self.flags)
    value = (value * 31) ^ hash(self.startTime)
    value = (value * 31) ^ hash(self.duration)
    value = (value * 31) ^ hash(self.tags)
    value = (value * 31) ^ hash(self.logs)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Process(object):
  """
  Attributes:
   - serviceName
   - tags
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'serviceName', None, None, ), # 1
    (2, TType.LIST, 'tags', (TType.STRUCT,(Tag, Tag.thrift_spec)), None, ), # 2
  )

  def __init__(self, serviceName=None, tags=None,):
    self.serviceName = serviceName
    self.tags = tags

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.serviceName = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.tags = []
          (_etype31, _size28) = iprot.readListBegin()
          for _i32 in xrange(_size28):
            _elem33 = Tag()
            _elem33.read(iprot)
            self.tags.append(_elem33)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Process')
    if self.serviceName is not None:
      oprot.writeFieldBegin('serviceName', TType.STRING, 1)
      oprot.writeString(self.serviceName)
      oprot.writeFieldEnd()
    if self.tags is not None:
      oprot.writeFieldBegin('tags', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.tags))
      for iter34 in self.tags:
        iter34.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.serviceName is None:
      raise TProtocol.TProtocolException(message='Required field serviceName is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.serviceName)
    value = (value * 31) ^ hash(self.tags)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Batch(object):
  """
  Attributes:
   - process
   - spans
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'process', (Process, Process.thrift_spec), None, ), # 1
    (2, TType.LIST, 'spans', (TType.STRUCT,(Span, Span.thrift_spec)), None, ), # 2
  )

  def __init__(self, process=None, spans=None,):
    self.process = process
    self.spans = spans

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.process = Process()
          self.process.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.spans = []
          (_etype38, _size35) = iprot.readListBegin()
          for _i39 in xrange(_size35):
            _elem40 = Span()
            _elem40.read(iprot)
            self.spans.append(_elem40)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Batch')
    if self.process is not None:
      oprot.writeFieldBegin('process', TType.STRUCT, 1)
      self.process.write(oprot)
      oprot.writeFieldEnd()
    if self.spans is not None:
      oprot.writeFieldBegin('spans', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.spans))
      for iter41 in self.spans:
        iter41.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.process is None:
      raise TProtocol.TProtocolException(message='Required field process is unset!')
    if self.spans is None:
      raise TProtocol.TProtocolException(message='Required field spans is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.process)
    value = (value * 31) ^ hash(self.spans)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BatchSubmitResponse(object):
  """
  Attributes:
   - ok
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'ok', None, None, ), # 1
  )

  def __init__(self, ok=None,):
    self.ok = ok

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.ok = iprot.readBool()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('BatchSubmitResponse')
    if self.ok is not None:
      oprot.writeFieldBegin('ok', TType.BOOL, 1)
      oprot.writeBool(self.ok)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.ok is None:
      raise TProtocol.TProtocolException(message='Required field ok is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.ok)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
