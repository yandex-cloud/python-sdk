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
class VersionInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURRENT_VERSION_FIELD_NUMBER: builtins.int
    NEW_REVISION_AVAILABLE_FIELD_NUMBER: builtins.int
    NEW_REVISION_SUMMARY_FIELD_NUMBER: builtins.int
    VERSION_DEPRECATED_FIELD_NUMBER: builtins.int
    current_version: builtins.str
    """Current Kubernetes version, format: major.minor (e.g. 1.15)."""
    new_revision_available: builtins.bool
    """Newer revisions may include Kubernetes patches (e.g 1.15.1 -> 1.15.2) as well
    as some internal component updates - new features or bug fixes in platform specific
    components either on the master or nodes.
    """
    new_revision_summary: builtins.str
    """Description of the changes to be applied when updating to the latest
    revision. Empty if new_revision_available is false.
    """
    version_deprecated: builtins.bool
    """The current version is on the deprecation schedule, component (master or node group)
    should be upgraded.
    """
    def __init__(
        self,
        *,
        current_version: builtins.str = ...,
        new_revision_available: builtins.bool = ...,
        new_revision_summary: builtins.str = ...,
        version_deprecated: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["current_version", b"current_version", "new_revision_available", b"new_revision_available", "new_revision_summary", b"new_revision_summary", "version_deprecated", b"version_deprecated"]) -> None: ...

global___VersionInfo = VersionInfo

@typing.final
class UpdateVersionSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VERSION_FIELD_NUMBER: builtins.int
    LATEST_REVISION_FIELD_NUMBER: builtins.int
    version: builtins.str
    """Request update to a newer version of Kubernetes (1.x -> 1.y)."""
    latest_revision: builtins.bool
    """Request update to the latest revision for the current version."""
    def __init__(
        self,
        *,
        version: builtins.str = ...,
        latest_revision: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["latest_revision", b"latest_revision", "specifier", b"specifier", "version", b"version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["latest_revision", b"latest_revision", "specifier", b"specifier", "version", b"version"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["specifier", b"specifier"]) -> typing.Literal["version", "latest_revision"] | None: ...

global___UpdateVersionSpec = UpdateVersionSpec
