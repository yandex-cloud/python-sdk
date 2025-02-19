"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class SearchIndexFile(google.protobuf.message.Message):
    """Represents a file that has been indexed within a search index."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    SEARCH_INDEX_ID_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Unique identifier of the file that was used for indexing."""
    search_index_id: builtins.str
    """ID of the search index that contains this file."""
    created_by: builtins.str
    """Identifier of the subject who created the file in the search index."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp representing when the file was created."""

    def __init__(
        self,
        *,
        id: builtins.str = ...,
        search_index_id: builtins.str = ...,
        created_by: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["created_at", b"created_at", "created_by", b"created_by", "id", b"id", "search_index_id", b"search_index_id"]) -> None: ...

global___SearchIndexFile = SearchIndexFile
