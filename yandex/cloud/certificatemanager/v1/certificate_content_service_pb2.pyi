"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PrivateKeyFormat:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PrivateKeyFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PrivateKeyFormat.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PRIVATE_KEY_FORMAT_UNSPECIFIED: _PrivateKeyFormat.ValueType  # 0
    PKCS1: _PrivateKeyFormat.ValueType  # 1
    PKCS8: _PrivateKeyFormat.ValueType  # 2

class PrivateKeyFormat(_PrivateKeyFormat, metaclass=_PrivateKeyFormatEnumTypeWrapper): ...

PRIVATE_KEY_FORMAT_UNSPECIFIED: PrivateKeyFormat.ValueType  # 0
PKCS1: PrivateKeyFormat.ValueType  # 1
PKCS8: PrivateKeyFormat.ValueType  # 2
global___PrivateKeyFormat = PrivateKeyFormat

@typing.final
class GetCertificateContentResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    CERTIFICATE_CHAIN_FIELD_NUMBER: builtins.int
    PRIVATE_KEY_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate."""
    private_key: builtins.str
    """PEM-encoded private key content of the certificate."""
    @property
    def certificate_chain(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """PEM-encoded certificate chain content of the certificate."""

    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
        certificate_chain: collections.abc.Iterable[builtins.str] | None = ...,
        private_key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificate_chain", b"certificate_chain", "certificate_id", b"certificate_id", "private_key", b"private_key"]) -> None: ...

global___GetCertificateContentResponse = GetCertificateContentResponse

@typing.final
class GetCertificateContentRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CERTIFICATE_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    PRIVATE_KEY_FORMAT_FIELD_NUMBER: builtins.int
    certificate_id: builtins.str
    """ID of the certificate to download content."""
    version_id: builtins.str
    """Optional ID of the version."""
    private_key_format: global___PrivateKeyFormat.ValueType
    """Desired format of private key"""
    def __init__(
        self,
        *,
        certificate_id: builtins.str = ...,
        version_id: builtins.str = ...,
        private_key_format: global___PrivateKeyFormat.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["certificate_id", b"certificate_id", "private_key_format", b"private_key_format", "version_id", b"version_id"]) -> None: ...

global___GetCertificateContentRequest = GetCertificateContentRequest
