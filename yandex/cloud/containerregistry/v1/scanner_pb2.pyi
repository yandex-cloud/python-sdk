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

@typing.final
class ScanResult(google.protobuf.message.Message):
    """A ScanResult resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Status:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ScanResult._Status.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STATUS_UNSPECIFIED: ScanResult._Status.ValueType  # 0
        RUNNING: ScanResult._Status.ValueType  # 1
        """Image scan is in progress."""
        READY: ScanResult._Status.ValueType  # 2
        """Image has been scanned and result is ready."""
        ERROR: ScanResult._Status.ValueType  # 3
        """Image scan is failed."""

    class Status(_Status, metaclass=_StatusEnumTypeWrapper): ...
    STATUS_UNSPECIFIED: ScanResult.Status.ValueType  # 0
    RUNNING: ScanResult.Status.ValueType  # 1
    """Image scan is in progress."""
    READY: ScanResult.Status.ValueType  # 2
    """Image has been scanned and result is ready."""
    ERROR: ScanResult.Status.ValueType  # 3
    """Image scan is failed."""

    ID_FIELD_NUMBER: builtins.int
    IMAGE_ID_FIELD_NUMBER: builtins.int
    SCANNED_AT_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    VULNERABILITIES_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Output only. ID of the ScanResult."""
    image_id: builtins.str
    """Output only. ID of the Image that the ScanResult belongs to."""
    status: global___ScanResult.Status.ValueType
    """Output only. The status of the ScanResult."""
    @property
    def scanned_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Output only. The timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format when the scan been finished."""

    @property
    def vulnerabilities(self) -> global___VulnerabilityStats:
        """Output only. Summary information about vulnerabilities found."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        image_id: builtins.str = ...,
        scanned_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        status: global___ScanResult.Status.ValueType = ...,
        vulnerabilities: global___VulnerabilityStats | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["scanned_at", b"scanned_at", "vulnerabilities", b"vulnerabilities"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "image_id", b"image_id", "scanned_at", b"scanned_at", "status", b"status", "vulnerabilities", b"vulnerabilities"]) -> None: ...

global___ScanResult = ScanResult

@typing.final
class VulnerabilityStats(google.protobuf.message.Message):
    """A VulnerabilityStats resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CRITICAL_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    MEDIUM_FIELD_NUMBER: builtins.int
    LOW_FIELD_NUMBER: builtins.int
    NEGLIGIBLE_FIELD_NUMBER: builtins.int
    UNDEFINED_FIELD_NUMBER: builtins.int
    critical: builtins.int
    """Count of CRITICAL vulnerabilities."""
    high: builtins.int
    """Count of HIGH vulnerabilities."""
    medium: builtins.int
    """Count of MEDIUM vulnerabilities."""
    low: builtins.int
    """Count of LOW vulnerabilities."""
    negligible: builtins.int
    """Count of NEGLIGIBLE vulnerabilities."""
    undefined: builtins.int
    """Count of other vulnerabilities."""
    def __init__(
        self,
        *,
        critical: builtins.int = ...,
        high: builtins.int = ...,
        medium: builtins.int = ...,
        low: builtins.int = ...,
        negligible: builtins.int = ...,
        undefined: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["critical", b"critical", "high", b"high", "low", b"low", "medium", b"medium", "negligible", b"negligible", "undefined", b"undefined"]) -> None: ...

global___VulnerabilityStats = VulnerabilityStats

@typing.final
class Vulnerability(google.protobuf.message.Message):
    """A Vulnerability resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Severity:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SeverityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Vulnerability._Severity.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SEVERITY_UNSPECIFIED: Vulnerability._Severity.ValueType  # 0
        CRITICAL: Vulnerability._Severity.ValueType  # 1
        """Critical severity is a world-burning problem, exploitable for nearly all users.
        Includes remote root privilege escalations, or massive data loss.
        """
        HIGH: Vulnerability._Severity.ValueType  # 2
        """High severity is a real problem, exploitable for many users in a default installation.
        Includes serious remote denial of services, local root privilege escalations, or data loss.
        """
        MEDIUM: Vulnerability._Severity.ValueType  # 3
        """Medium severity is a real security problem, and is exploitable for many users.
        Includes network daemon denial of service attacks, cross-site scripting, and gaining user privileges.
        Updates should be made soon for this priority of issue.
        """
        LOW: Vulnerability._Severity.ValueType  # 4
        """Low severity is a security problem, but is hard to exploit due to environment, requires a user-assisted attack,
        a small install base, or does very little damage. These tend to be included in security updates only when
        higher priority issues require an update, or if many low priority issues have built up.
        """
        NEGLIGIBLE: Vulnerability._Severity.ValueType  # 5
        """Negligible severity is technically a security problem, but is only theoretical in nature, requires a very special situation,
        has almost no install base, or does no real damage. These tend not to get backport from upstream,
        and will likely not be included in security updates unless there is an easy fix and some other issue causes an update.
        """
        UNDEFINED: Vulnerability._Severity.ValueType  # 6
        """Unknown severity is either a security problem that has not been assigned to a priority yet or
        a priority that our system did not recognize.
        """

    class Severity(_Severity, metaclass=_SeverityEnumTypeWrapper): ...
    SEVERITY_UNSPECIFIED: Vulnerability.Severity.ValueType  # 0
    CRITICAL: Vulnerability.Severity.ValueType  # 1
    """Critical severity is a world-burning problem, exploitable for nearly all users.
    Includes remote root privilege escalations, or massive data loss.
    """
    HIGH: Vulnerability.Severity.ValueType  # 2
    """High severity is a real problem, exploitable for many users in a default installation.
    Includes serious remote denial of services, local root privilege escalations, or data loss.
    """
    MEDIUM: Vulnerability.Severity.ValueType  # 3
    """Medium severity is a real security problem, and is exploitable for many users.
    Includes network daemon denial of service attacks, cross-site scripting, and gaining user privileges.
    Updates should be made soon for this priority of issue.
    """
    LOW: Vulnerability.Severity.ValueType  # 4
    """Low severity is a security problem, but is hard to exploit due to environment, requires a user-assisted attack,
    a small install base, or does very little damage. These tend to be included in security updates only when
    higher priority issues require an update, or if many low priority issues have built up.
    """
    NEGLIGIBLE: Vulnerability.Severity.ValueType  # 5
    """Negligible severity is technically a security problem, but is only theoretical in nature, requires a very special situation,
    has almost no install base, or does no real damage. These tend not to get backport from upstream,
    and will likely not be included in security updates unless there is an easy fix and some other issue causes an update.
    """
    UNDEFINED: Vulnerability.Severity.ValueType  # 6
    """Unknown severity is either a security problem that has not been assigned to a priority yet or
    a priority that our system did not recognize.
    """

    SEVERITY_FIELD_NUMBER: builtins.int
    PACKAGE_FIELD_NUMBER: builtins.int
    severity: global___Vulnerability.Severity.ValueType
    """Output only. Severity of the Vulnerability."""
    @property
    def package(self) -> global___PackageVulnerability: ...
    def __init__(
        self,
        *,
        severity: global___Vulnerability.Severity.ValueType = ...,
        package: global___PackageVulnerability | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["package", b"package", "vulnerability", b"vulnerability"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["package", b"package", "severity", b"severity", "vulnerability", b"vulnerability"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["vulnerability", b"vulnerability"]) -> typing.Literal["package"] | None: ...

global___Vulnerability = Vulnerability

@typing.final
class PackageVulnerability(google.protobuf.message.Message):
    """A PackageVulnerability resource."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    LINK_FIELD_NUMBER: builtins.int
    PACKAGE_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    FIXED_BY_FIELD_NUMBER: builtins.int
    ORIGIN_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of vulnerability in CVE database."""
    link: builtins.str
    """URL to the page with description of vulnerability."""
    package: builtins.str
    """The package name where vulnerability has been found."""
    source: builtins.str
    """The package manager name. Ex.: yum, rpm, dpkg."""
    version: builtins.str
    """The version of the package where vulnerability has been found."""
    fixed_by: builtins.str
    """The version of the package where vulnerability has been fixed."""
    origin: builtins.str
    """The place where vulnerability is originated (OS, lang package, etc.)"""
    type: builtins.str
    """The type of vulnerability origin - name of OS if origin="os" or package type (jar, gobinary, etc.) if origin="lang" """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        link: builtins.str = ...,
        package: builtins.str = ...,
        source: builtins.str = ...,
        version: builtins.str = ...,
        fixed_by: builtins.str = ...,
        origin: builtins.str = ...,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["fixed_by", b"fixed_by", "link", b"link", "name", b"name", "origin", b"origin", "package", b"package", "source", b"source", "type", b"type", "version", b"version"]) -> None: ...

global___PackageVulnerability = PackageVulnerability
