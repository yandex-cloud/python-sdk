"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class OptimizerAdamw(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BETA1_FIELD_NUMBER: builtins.int
    BETA2_FIELD_NUMBER: builtins.int
    EPS_FIELD_NUMBER: builtins.int
    WEIGHT_DECAY_FIELD_NUMBER: builtins.int
    beta1: builtins.float
    beta2: builtins.float
    eps: builtins.float
    weight_decay: builtins.float
    def __init__(
        self,
        *,
        beta1: builtins.float = ...,
        beta2: builtins.float = ...,
        eps: builtins.float = ...,
        weight_decay: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["beta1", b"beta1", "beta2", b"beta2", "eps", b"eps", "weight_decay", b"weight_decay"]) -> None: ...

global___OptimizerAdamw = OptimizerAdamw
