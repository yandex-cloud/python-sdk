"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _SubjectType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SubjectTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SubjectType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SUBJECT_TYPE_UNSPECIFIED: _SubjectType.ValueType  # 0
    USER_ACCOUNT: _SubjectType.ValueType  # 1
    SERVICE_ACCOUNT: _SubjectType.ValueType  # 2
    GROUP: _SubjectType.ValueType  # 3
    INVITEE: _SubjectType.ValueType  # 4

class SubjectType(_SubjectType, metaclass=_SubjectTypeEnumTypeWrapper): ...

SUBJECT_TYPE_UNSPECIFIED: SubjectType.ValueType  # 0
USER_ACCOUNT: SubjectType.ValueType  # 1
SERVICE_ACCOUNT: SubjectType.ValueType  # 2
GROUP: SubjectType.ValueType  # 3
INVITEE: SubjectType.ValueType  # 4
global___SubjectType = SubjectType

@typing.final
class SubjectClaims(google.protobuf.message.Message):
    """Claims representation, see https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims for details."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUB_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    GIVEN_NAME_FIELD_NUMBER: builtins.int
    FAMILY_NAME_FIELD_NUMBER: builtins.int
    PREFERRED_USERNAME_FIELD_NUMBER: builtins.int
    PICTURE_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    ZONEINFO_FIELD_NUMBER: builtins.int
    LOCALE_FIELD_NUMBER: builtins.int
    PHONE_NUMBER_FIELD_NUMBER: builtins.int
    SUB_TYPE_FIELD_NUMBER: builtins.int
    FEDERATION_FIELD_NUMBER: builtins.int
    LAST_AUTHENTICATED_AT_FIELD_NUMBER: builtins.int
    sub: builtins.str
    """Subject - Identifier for the End-User at the Issuer."""
    name: builtins.str
    """End-User's full name in displayable form including all name parts, possibly including titles and suffixes, ordered according to the End-User's locale and preferences."""
    given_name: builtins.str
    """Given name(s) or first name(s) of the End-User. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters."""
    family_name: builtins.str
    """Surname(s) or last name(s) of the End-User. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters."""
    preferred_username: builtins.str
    """Shorthand name by which the End-User wishes to be referred to at the RP, such as janedoe or j.doe.
    This value MAY be any valid JSON string including special characters such as @, /, or whitespace. The RP MUST NOT rely upon this value being unique, as discussed in Section 5.7.
    """
    picture: builtins.str
    """URL of the End-User's profile picture. This URL MUST refer to an image file (for example, a PNG, JPEG, or GIF image file),
    rather than to a Web page containing an image. Note that this URL SHOULD specifically reference a profile photo of the End-User suitable for displaying when describing the End-User, rather than an arbitrary photo taken by the End-User.
    """
    email: builtins.str
    """End-User's preferred e-mail address. Its value MUST conform to the RFC 5322 [RFC5322] addr-spec syntax.
    The RP MUST NOT rely upon this value being unique, as discussed in Section 5.7.
    """
    zoneinfo: builtins.str
    """String from zoneinfo [zoneinfo] time zone database representing the End-User's time zone. For example, Europe/Paris or America/Los_Angeles."""
    locale: builtins.str
    """End-User's locale, represented as a BCP47 [RFC5646] language tag. This is typically an ISO 639-1 Alpha-2 [ISO639-1] language code in lowercase and an ISO 3166-1 Alpha-2 [ISO3166-1] country code in uppercase, separated by a dash.
    For example, en-US or fr-CA. As a compatibility note, some implementations have used an underscore as the separator rather than a dash, for example, en_US; Relying Parties MAY choose to accept this locale syntax as well.
    """
    phone_number: builtins.str
    """End-User's preferred telephone number. E.164 [E.164] is RECOMMENDED as the format of this Claim, for example, +1 (425) 555-1212 or +56 (2) 687 2400.
    If the phone number contains an extension, it is RECOMMENDED that the extension be represented using the RFC 3966 [RFC3966] extension syntax, for example, +1 (604) 555-1234;ext=5678.
    """
    sub_type: global___SubjectType.ValueType
    """Subject type."""
    @property
    def federation(self) -> global___Federation:
        """User federation, non-empty only for federated users."""

    @property
    def last_authenticated_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Last time the access token was created. Filled only for federated users (not for global users)."""

    def __init__(
        self,
        *,
        sub: builtins.str = ...,
        name: builtins.str = ...,
        given_name: builtins.str = ...,
        family_name: builtins.str = ...,
        preferred_username: builtins.str = ...,
        picture: builtins.str = ...,
        email: builtins.str = ...,
        zoneinfo: builtins.str = ...,
        locale: builtins.str = ...,
        phone_number: builtins.str = ...,
        sub_type: global___SubjectType.ValueType = ...,
        federation: global___Federation | None = ...,
        last_authenticated_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["federation", b"federation", "last_authenticated_at", b"last_authenticated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["email", b"email", "family_name", b"family_name", "federation", b"federation", "given_name", b"given_name", "last_authenticated_at", b"last_authenticated_at", "locale", b"locale", "name", b"name", "phone_number", b"phone_number", "picture", b"picture", "preferred_username", b"preferred_username", "sub", b"sub", "sub_type", b"sub_type", "zoneinfo", b"zoneinfo"]) -> None: ...

global___SubjectClaims = SubjectClaims

@typing.final
class Federation(google.protobuf.message.Message):
    """Minimalistic analog of yandex.cloud.organizationmanager.v1.saml.Federation"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    id: builtins.str
    """ID of the federation."""
    name: builtins.str
    """Name of the federation. The name is unique within the cloud or organization"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "name", b"name"]) -> None: ...

global___Federation = Federation
