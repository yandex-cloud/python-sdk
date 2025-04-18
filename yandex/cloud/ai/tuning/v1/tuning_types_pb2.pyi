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
class TuningTypeLora(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RANK_FIELD_NUMBER: builtins.int
    ALPHA_FIELD_NUMBER: builtins.int
    INITIALIZATION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    rank: builtins.int
    alpha: builtins.float
    """Integer value"""
    initialization: builtins.str
    type: builtins.str
    def __init__(
        self,
        *,
        rank: builtins.int = ...,
        alpha: builtins.float = ...,
        initialization: builtins.str = ...,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["alpha", b"alpha", "initialization", b"initialization", "rank", b"rank", "type", b"type"]) -> None: ...

global___TuningTypeLora = TuningTypeLora

@typing.final
class TuningTypePromptTune(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VIRTUAL_TOKENS_FIELD_NUMBER: builtins.int
    virtual_tokens: builtins.int
    def __init__(
        self,
        *,
        virtual_tokens: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["virtual_tokens", b"virtual_tokens"]) -> None: ...

global___TuningTypePromptTune = TuningTypePromptTune
