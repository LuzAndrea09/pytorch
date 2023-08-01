# Defined in torch/csrc/onnx/init.cpp

from enum import Enum

_CAFFE2_ATEN_FALLBACK: bool
PRODUCER_VERSION: str

class TensorProtoDataType(Enum):
    UNDEFINED = ...
    FLOAT = ...
    UINT8 = ...
    INT8 = ...
    UINT16 = ...
    INT16 = ...
    INT32 = ...
    INT64 = ...
    STRING = ...
    BOOL = ...
    FLOAT16 = ...
    DOUBLE = ...
    UINT32 = ...
    UINT64 = ...
    COMPLEX64 = ...
    COMPLEX128 = ...
    BFLOAT16 = ...
    FP8E4M3 = ...
    FP8E5M2 = ...

class OperatorExportTypes(Enum):
    ONNX = ...
    ONNX_ATEN = ...
    ONNX_ATEN_FALLBACK = ...
    ONNX_FALLTHROUGH = ...

class TrainingMode(Enum):
    EVAL = ...
    PRESERVE = ...
    TRAINING = ...
