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
class GenerateSshCertificateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLOUD_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    SUBJECT_ID_FIELD_NUMBER: builtins.int
    OS_LOGIN_FIELD_NUMBER: builtins.int
    PUBLIC_KEY_FIELD_NUMBER: builtins.int
    cloud_id: builtins.str
    """the cloud must be attached to an organization"""
    organization_id: builtins.str
    subject_id: builtins.str
    """specify subject to generate certificate for default login"""
    os_login: builtins.str
    """specify os_login for a specific login"""
    public_key: builtins.str
    def __init__(
        self,
        *,
        cloud_id: builtins.str = ...,
        organization_id: builtins.str = ...,
        subject_id: builtins.str = ...,
        os_login: builtins.str = ...,
        public_key: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cloud_id", b"cloud_id", "organization_id", b"organization_id", "os_login", b"os_login", "scope", b"scope", "subject", b"subject", "subject_id", b"subject_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cloud_id", b"cloud_id", "organization_id", b"organization_id", "os_login", b"os_login", "public_key", b"public_key", "scope", b"scope", "subject", b"subject", "subject_id", b"subject_id"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["scope", b"scope"]) -> typing.Literal["cloud_id", "organization_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["subject", b"subject"]) -> typing.Literal["subject_id", "os_login"] | None: ...

global___GenerateSshCertificateRequest = GenerateSshCertificateRequest

@typing.final
class GenerateSshCertificateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SIGNED_CERTIFICATE_FIELD_NUMBER: builtins.int
    signed_certificate: builtins.str
    """as per specification https://cvsweb.openbsd.org/src/usr.bin/ssh/PROTOCOL.certkeys?annotate=HEAD"""
    def __init__(
        self,
        *,
        signed_certificate: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["signed_certificate", b"signed_certificate"]) -> None: ...

global___GenerateSshCertificateResponse = GenerateSshCertificateResponse
