"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.mdb.postgresql.v1.perf_diag_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListRawStatementsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FROM_TIME_FIELD_NUMBER: builtins.int
    TO_TIME_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of a PostgreSQL cluster to request query statistics for.

    To get a PostgreSQL cluster ID, use the [ClusterService.List] method.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of the results is larger than [page_size], the service returns [ListRawStatementsResponse.next_page_token]. You can use it to get the next page of the results in subsequent requests."""
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the [ListRawStatementsResponse.next_page_token] returned by the previous SQL statement list request."""
    @property
    def from_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Beginning of the period for which you need to request data (in the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format)."""

    @property
    def to_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """End of the period for which you need to request data (in the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format)."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        from_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        to_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["from_time", b"from_time", "to_time", b"to_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "from_time", b"from_time", "page_size", b"page_size", "page_token", b"page_token", "to_time", b"to_time"]) -> None: ...

global___ListRawStatementsRequest = ListRawStatementsRequest

@typing.final
class ListRawSessionStatesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    FROM_TIME_FIELD_NUMBER: builtins.int
    TO_TIME_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of a PostgreSQL cluster to request session statistics for.

    To get a PostgreSQL cluster ID, use the [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of the results is larger than [page_size], the service returns [ListRawSessionStatesResponse.next_page_token]. You can use it to get the next page of the results in subsequent requests."""
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the [ListRawSessionStatesResponse.next_page_token] returned by the previous PostgreSQL session list request."""
    @property
    def from_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Beginning of the period for which you need to request data (in the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format)."""

    @property
    def to_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """End of the period for which you need to request data (in the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format)."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        from_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        to_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["from_time", b"from_time", "to_time", b"to_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "from_time", b"from_time", "page_size", b"page_size", "page_token", b"page_token", "to_time", b"to_time"]) -> None: ...

global___ListRawSessionStatesRequest = ListRawSessionStatesRequest

@typing.final
class ListRawSessionStatesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SESSION_STATES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results when requesting the PostgreSQL session list. If the number of the results is larger than [ListRawSessionStatesRequest.page_size], use the [next_page_token] as the value for the [ListRawSessionStatesRequest.page_token] parameter in the next request. Each subsequent request will have its own [next_page_token] to continue paging through the results."""
    @property
    def session_states(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.postgresql.v1.perf_diag_pb2.SessionState]:
        """List of PostgreSQL sessions."""

    def __init__(
        self,
        *,
        session_states: collections.abc.Iterable[yandex.cloud.mdb.postgresql.v1.perf_diag_pb2.SessionState] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "session_states", b"session_states"]) -> None: ...

global___ListRawSessionStatesResponse = ListRawSessionStatesResponse

@typing.final
class ListRawStatementsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATEMENTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results when requesting the PostgreSQL session list. If the number of the results is larger than [ListRawStatementsRequest.page_size], use the [next_page_token] as the value for the [ListRawStatementsRequest.page_token] parameter in the next request. Each subsequent request will have its own [next_page_token] to continue paging through the results."""
    @property
    def statements(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.postgresql.v1.perf_diag_pb2.QueryStatement]:
        """List of SQL statements (queries)."""

    def __init__(
        self,
        *,
        statements: collections.abc.Iterable[yandex.cloud.mdb.postgresql.v1.perf_diag_pb2.QueryStatement] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "statements", b"statements"]) -> None: ...

global___ListRawStatementsResponse = ListRawStatementsResponse