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
class SessionState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_FIELD_NUMBER: builtins.int
    HOST_FIELD_NUMBER: builtins.int
    PID_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    APPLICATION_NAME_FIELD_NUMBER: builtins.int
    BACKEND_START_FIELD_NUMBER: builtins.int
    XACT_START_FIELD_NUMBER: builtins.int
    QUERY_START_FIELD_NUMBER: builtins.int
    STATE_CHANGE_FIELD_NUMBER: builtins.int
    WAIT_EVENT_TYPE_FIELD_NUMBER: builtins.int
    WAIT_EVENT_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    BACKEND_TYPE_FIELD_NUMBER: builtins.int
    CLIENT_ADDR_FIELD_NUMBER: builtins.int
    CLIENT_HOSTNAME_FIELD_NUMBER: builtins.int
    CLIENT_PORT_FIELD_NUMBER: builtins.int
    BACKEND_XID_FIELD_NUMBER: builtins.int
    BACKEND_XMIN_FIELD_NUMBER: builtins.int
    BLOCKING_PIDS_FIELD_NUMBER: builtins.int
    QUERY_ID_FIELD_NUMBER: builtins.int
    host: builtins.str
    """Host of the connected client."""
    pid: builtins.int
    """Server process ID. For client connections, this is a client connection ID."""
    database: builtins.str
    """Database ID."""
    user: builtins.str
    """User ID."""
    application_name: builtins.str
    """Application name on the connected client."""
    wait_event_type: builtins.str
    """Type of event for which the backend is waiting. Such an event is called a wait event. A backend refers to the process that maintains the client connection.

    For the list of wait events, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/monitoring-stats.html#WAIT-EVENT-TABLE). If the backend is not waiting for any event, the parameter returns [NULL].
    """
    wait_event: builtins.str
    """Wait event name.

    For the list of such names, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/monitoring-stats.html#WAIT-EVENT-ACTIVITY-TABLE). If the backend is not waiting for any event, the parameter returns [NULL].
    """
    state: builtins.str
    """Current backend state. For the list of possible values, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW)."""
    query: builtins.str
    """Text of the most recent query.

    If the [state] parameter takes the value [active], the parameter shows the currently executing query. For the rest of the states, the parameter shows the last query that was executed. By default, the query text is truncated to 1024 bytes.
    """
    backend_type: builtins.str
    """Current backend type. For the list of possible values, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ACTIVITY-VIEW)."""
    client_addr: builtins.str
    """IP address of the connected client.

    The parameter returns [NULL] in the following cases:
    - The client is connected via a Unix socket on the server.
    - A given process is internal (for example, autovacuum).
    """
    client_hostname: builtins.str
    """Host name of the connected client (relevant for IP connections)."""
    client_port: builtins.int
    """TCP port number that the client is using for communication with the server.

    Returns [-1] if the client is connected via a Unix socket on the server. Returns [NULL] if a given process is internal (for example, autovacuum).
    """
    backend_xid: builtins.int
    """Top-level transaction ID, if any."""
    backend_xmin: builtins.int
    """Current [xmin horizon]."""
    blocking_pids: builtins.str
    """Process IDs that are blocking a given server process ID."""
    query_id: builtins.str
    """Query ID."""
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of collecting statistics on sessions (in the [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format)."""

    @property
    def backend_start(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when a given process was started. For client connections, this is the time when the client connected to the server."""

    @property
    def xact_start(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when a transaction of a given process was started. Returns [NULL] if no transaction is active.

        If the currently active query is the first of its transaction, the value of this parameter is equal to the value of the [query_start] parameter.
        """

    @property
    def query_start(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the currently active query was started.

        If the [state] parameter does not take the value [active], the parameter returns the time when the lastest query was started.
        """

    @property
    def state_change(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time when the [state] parameter was last changed."""

    def __init__(
        self,
        *,
        time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        host: builtins.str = ...,
        pid: builtins.int = ...,
        database: builtins.str = ...,
        user: builtins.str = ...,
        application_name: builtins.str = ...,
        backend_start: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        xact_start: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        query_start: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        state_change: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        wait_event_type: builtins.str = ...,
        wait_event: builtins.str = ...,
        state: builtins.str = ...,
        query: builtins.str = ...,
        backend_type: builtins.str = ...,
        client_addr: builtins.str = ...,
        client_hostname: builtins.str = ...,
        client_port: builtins.int = ...,
        backend_xid: builtins.int = ...,
        backend_xmin: builtins.int = ...,
        blocking_pids: builtins.str = ...,
        query_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["backend_start", b"backend_start", "query_start", b"query_start", "state_change", b"state_change", "time", b"time", "xact_start", b"xact_start"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["application_name", b"application_name", "backend_start", b"backend_start", "backend_type", b"backend_type", "backend_xid", b"backend_xid", "backend_xmin", b"backend_xmin", "blocking_pids", b"blocking_pids", "client_addr", b"client_addr", "client_hostname", b"client_hostname", "client_port", b"client_port", "database", b"database", "host", b"host", "pid", b"pid", "query", b"query", "query_id", b"query_id", "query_start", b"query_start", "state", b"state", "state_change", b"state_change", "time", b"time", "user", b"user", "wait_event", b"wait_event", "wait_event_type", b"wait_event_type", "xact_start", b"xact_start"]) -> None: ...

global___SessionState = SessionState

@typing.final
class PrimaryKey(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HOST_FIELD_NUMBER: builtins.int
    USER_FIELD_NUMBER: builtins.int
    DATABASE_FIELD_NUMBER: builtins.int
    TOPLEVEL_FIELD_NUMBER: builtins.int
    QUERY_ID_FIELD_NUMBER: builtins.int
    PLAN_ID_FIELD_NUMBER: builtins.int
    host: builtins.str
    """Host of the connected client."""
    user: builtins.str
    """User ID."""
    database: builtins.str
    """Database ID."""
    toplevel: builtins.bool
    """Returns [true] if a query is executed as a top-level SQL statement or if the [pg_stat_statements.track](https://www.postgresql.org/docs/current/pgstatstatements.html#id-1.11.7.41.9) parameter is set to the value [top]."""
    query_id: builtins.str
    """Query ID."""
    plan_id: builtins.str
    """Query planning ID."""
    def __init__(
        self,
        *,
        host: builtins.str = ...,
        user: builtins.str = ...,
        database: builtins.str = ...,
        toplevel: builtins.bool = ...,
        query_id: builtins.str = ...,
        plan_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["database", b"database", "host", b"host", "plan_id", b"plan_id", "query_id", b"query_id", "toplevel", b"toplevel", "user", b"user"]) -> None: ...

global___PrimaryKey = PrimaryKey

@typing.final
class QueryStats(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIME_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    NORMALIZED_PLAN_FIELD_NUMBER: builtins.int
    EXAMPLE_PLAN_FIELD_NUMBER: builtins.int
    PLANS_FIELD_NUMBER: builtins.int
    TOTAL_PLAN_TIME_FIELD_NUMBER: builtins.int
    MIN_PLAN_TIME_FIELD_NUMBER: builtins.int
    MAX_PLAN_TIME_FIELD_NUMBER: builtins.int
    MEAN_PLAN_TIME_FIELD_NUMBER: builtins.int
    STDDEV_PLAN_TIME_FIELD_NUMBER: builtins.int
    CALLS_FIELD_NUMBER: builtins.int
    TOTAL_TIME_FIELD_NUMBER: builtins.int
    MIN_TIME_FIELD_NUMBER: builtins.int
    MAX_TIME_FIELD_NUMBER: builtins.int
    MEAN_TIME_FIELD_NUMBER: builtins.int
    STDDEV_TIME_FIELD_NUMBER: builtins.int
    ROWS_FIELD_NUMBER: builtins.int
    SHARED_BLKS_HIT_FIELD_NUMBER: builtins.int
    SHARED_BLKS_READ_FIELD_NUMBER: builtins.int
    SHARED_BLKS_DIRTIED_FIELD_NUMBER: builtins.int
    SHARED_BLKS_WRITTEN_FIELD_NUMBER: builtins.int
    LOCAL_BLKS_HIT_FIELD_NUMBER: builtins.int
    LOCAL_BLKS_READ_FIELD_NUMBER: builtins.int
    LOCAL_BLKS_DIRTIED_FIELD_NUMBER: builtins.int
    LOCAL_BLKS_WRITTEN_FIELD_NUMBER: builtins.int
    TEMP_BLKS_READ_FIELD_NUMBER: builtins.int
    TEMP_BLKS_WRITTEN_FIELD_NUMBER: builtins.int
    BLK_READ_TIME_FIELD_NUMBER: builtins.int
    BLK_WRITE_TIME_FIELD_NUMBER: builtins.int
    TEMP_BLK_READ_TIME_FIELD_NUMBER: builtins.int
    TEMP_BLK_WRITE_TIME_FIELD_NUMBER: builtins.int
    WAL_RECORDS_FIELD_NUMBER: builtins.int
    WAL_FPI_FIELD_NUMBER: builtins.int
    WAL_BYTES_FIELD_NUMBER: builtins.int
    JIT_FUNCTIONS_FIELD_NUMBER: builtins.int
    JIT_GENERATION_TIME_FIELD_NUMBER: builtins.int
    JIT_INLINING_COUNT_FIELD_NUMBER: builtins.int
    JIT_INLINING_TIME_FIELD_NUMBER: builtins.int
    JIT_OPTIMIZATION_COUNT_FIELD_NUMBER: builtins.int
    JIT_OPTIMIZATION_TIME_FIELD_NUMBER: builtins.int
    JIT_EMISSION_COUNT_FIELD_NUMBER: builtins.int
    JIT_EMISSION_TIME_FIELD_NUMBER: builtins.int
    STARTUP_COST_FIELD_NUMBER: builtins.int
    TOTAL_COST_FIELD_NUMBER: builtins.int
    PLAN_ROWS_FIELD_NUMBER: builtins.int
    PLAN_WIDTH_FIELD_NUMBER: builtins.int
    READS_FIELD_NUMBER: builtins.int
    WRITES_FIELD_NUMBER: builtins.int
    USER_TIME_FIELD_NUMBER: builtins.int
    SYSTEM_TIME_FIELD_NUMBER: builtins.int
    query: builtins.str
    """Statement text."""
    normalized_plan: builtins.str
    """Normalized query plan."""
    example_plan: builtins.str
    """Example of a query execution plan (without normalization)."""
    plans: builtins.int
    """Number of times that a query was planned.

    The parameter returns a non-zero value if the [pg_stat_statements.track_planning](https://www.postgresql.org/docs/current/pgstatstatements.html#id-1.11.7.41.9) parameter is enabled.
    """
    total_plan_time: builtins.float
    """Total time taken to plan a query, in milliseconds.

    The parameter returns a non-zero value if the [pg_stat_statements.track_planning] parameter is enabled.
    """
    min_plan_time: builtins.float
    """Minimum time taken to plan a query, in milliseconds.

    The parameter returns a non-zero value if the [pg_stat_statements.track_planning] parameter is enabled.
    """
    max_plan_time: builtins.float
    """Maximum time taken to plan a query, in milliseconds.

    The parameter returns a non-zero value if the [pg_stat_statements.track_planning] parameter is enabled.
    """
    mean_plan_time: builtins.float
    """Average time taken to plan a query, in milliseconds.

    The parameter returns a non-zero value if the [pg_stat_statements.track_planning] parameter is enabled.
    """
    stddev_plan_time: builtins.float
    """Population standard deviation of the time taken to plan a query, in milliseconds.

    The parameter returns a non-zero value if the [pg_stat_statements.track_planning] parameter is enabled.
    """
    calls: builtins.int
    """Number of times that a query was executed."""
    total_time: builtins.float
    """Total time taken to execute a query, in milliseconds.
    total_exec_time
    """
    min_time: builtins.float
    """Minimum time taken to execute a query, in milliseconds.
    min_exec_time
    """
    max_time: builtins.float
    """Maximum time taken to execute a query, in milliseconds.
    max_exec_time
    """
    mean_time: builtins.float
    """Average time taken to execute a query, in milliseconds.
    mean_exec_time
    """
    stddev_time: builtins.float
    """Population standard deviation of the time taken to execute a query, in milliseconds.
    stddev_exec_time
    """
    rows: builtins.int
    """Number of retrieved or affected rows."""
    shared_blks_hit: builtins.int
    """Number of shared blocks that are hit from cache."""
    shared_blks_read: builtins.int
    """Number of read shared blocks."""
    shared_blks_dirtied: builtins.int
    """Number of 'dirtied' shared blocks."""
    shared_blks_written: builtins.int
    """Number of written shared blocks."""
    local_blks_hit: builtins.int
    """Number of local blocks that are hit from cache."""
    local_blks_read: builtins.int
    """Number of read local blocks."""
    local_blks_dirtied: builtins.int
    """Number of 'dirtied' local blocks."""
    local_blks_written: builtins.int
    """Number of written local blocks."""
    temp_blks_read: builtins.int
    """Number of read temporary blocks."""
    temp_blks_written: builtins.int
    """Number of written temporary blocks."""
    blk_read_time: builtins.float
    """Time taken to read data blocks, in milliseconds.

    The parameter returns a non-zero value if the [track_io_timing](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-IO-TIMING) parameter is enabled.
    """
    blk_write_time: builtins.float
    """Time taken to record data blocks, in milliseconds.

    The parameter returns a non-zero value if the [track_io_timing] parameter is enabled.
    """
    temp_blk_read_time: builtins.float
    """Time taken to read temporary data blocks, in milliseconds.

    The parameter returns a non-zero value if the [track_io_timing] parameter is enabled.
    """
    temp_blk_write_time: builtins.float
    """Time taken to record temporary data blocks, in milliseconds.

    The parameter returns a non-zero value if the [track_io_timing] parameter is enabled.
    """
    wal_records: builtins.int
    """Number of WAL records generated during a given period."""
    wal_fpi: builtins.int
    """Number of WAL full page images generated during a given period."""
    wal_bytes: builtins.int
    """Number of WAL logs generated during a given period, in bytes."""
    jit_functions: builtins.int
    """Number of JIT-compiled functions."""
    jit_generation_time: builtins.float
    """Time taken to generate JIT code, in milliseconds."""
    jit_inlining_count: builtins.int
    """Number of times that functions have been inlined."""
    jit_inlining_time: builtins.float
    """Time taken to inline functions, in milliseconds."""
    jit_optimization_count: builtins.int
    """Number of times that a query was optimized."""
    jit_optimization_time: builtins.float
    """Time taken to optimize a query, in milliseconds."""
    jit_emission_count: builtins.int
    """Number of times that code was emitted."""
    jit_emission_time: builtins.float
    """Time taken to emit code."""
    startup_cost: builtins.int
    """Cost of receiving a response to a query before the first row of the response is issued."""
    total_cost: builtins.int
    """Cost of receiving a response to a query when all the rows of the response are issued."""
    plan_rows: builtins.int
    """Expected number of rows that a given plan node should issue."""
    plan_width: builtins.int
    """Expected average size of rows that a given plan node should issue."""
    reads: builtins.int
    """Number of bytes that the filesystem layer has read."""
    writes: builtins.int
    """Number of bytes that the filesystem layer has written."""
    user_time: builtins.float
    """User CPU time used."""
    system_time: builtins.float
    """System CPU time used."""
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of collecting statistics on planning and execution of queries."""

    def __init__(
        self,
        *,
        time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        query: builtins.str = ...,
        normalized_plan: builtins.str = ...,
        example_plan: builtins.str = ...,
        plans: builtins.int = ...,
        total_plan_time: builtins.float = ...,
        min_plan_time: builtins.float = ...,
        max_plan_time: builtins.float = ...,
        mean_plan_time: builtins.float = ...,
        stddev_plan_time: builtins.float = ...,
        calls: builtins.int = ...,
        total_time: builtins.float = ...,
        min_time: builtins.float = ...,
        max_time: builtins.float = ...,
        mean_time: builtins.float = ...,
        stddev_time: builtins.float = ...,
        rows: builtins.int = ...,
        shared_blks_hit: builtins.int = ...,
        shared_blks_read: builtins.int = ...,
        shared_blks_dirtied: builtins.int = ...,
        shared_blks_written: builtins.int = ...,
        local_blks_hit: builtins.int = ...,
        local_blks_read: builtins.int = ...,
        local_blks_dirtied: builtins.int = ...,
        local_blks_written: builtins.int = ...,
        temp_blks_read: builtins.int = ...,
        temp_blks_written: builtins.int = ...,
        blk_read_time: builtins.float = ...,
        blk_write_time: builtins.float = ...,
        temp_blk_read_time: builtins.float = ...,
        temp_blk_write_time: builtins.float = ...,
        wal_records: builtins.int = ...,
        wal_fpi: builtins.int = ...,
        wal_bytes: builtins.int = ...,
        jit_functions: builtins.int = ...,
        jit_generation_time: builtins.float = ...,
        jit_inlining_count: builtins.int = ...,
        jit_inlining_time: builtins.float = ...,
        jit_optimization_count: builtins.int = ...,
        jit_optimization_time: builtins.float = ...,
        jit_emission_count: builtins.int = ...,
        jit_emission_time: builtins.float = ...,
        startup_cost: builtins.int = ...,
        total_cost: builtins.int = ...,
        plan_rows: builtins.int = ...,
        plan_width: builtins.int = ...,
        reads: builtins.int = ...,
        writes: builtins.int = ...,
        user_time: builtins.float = ...,
        system_time: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["time", b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["blk_read_time", b"blk_read_time", "blk_write_time", b"blk_write_time", "calls", b"calls", "example_plan", b"example_plan", "jit_emission_count", b"jit_emission_count", "jit_emission_time", b"jit_emission_time", "jit_functions", b"jit_functions", "jit_generation_time", b"jit_generation_time", "jit_inlining_count", b"jit_inlining_count", "jit_inlining_time", b"jit_inlining_time", "jit_optimization_count", b"jit_optimization_count", "jit_optimization_time", b"jit_optimization_time", "local_blks_dirtied", b"local_blks_dirtied", "local_blks_hit", b"local_blks_hit", "local_blks_read", b"local_blks_read", "local_blks_written", b"local_blks_written", "max_plan_time", b"max_plan_time", "max_time", b"max_time", "mean_plan_time", b"mean_plan_time", "mean_time", b"mean_time", "min_plan_time", b"min_plan_time", "min_time", b"min_time", "normalized_plan", b"normalized_plan", "plan_rows", b"plan_rows", "plan_width", b"plan_width", "plans", b"plans", "query", b"query", "reads", b"reads", "rows", b"rows", "shared_blks_dirtied", b"shared_blks_dirtied", "shared_blks_hit", b"shared_blks_hit", "shared_blks_read", b"shared_blks_read", "shared_blks_written", b"shared_blks_written", "startup_cost", b"startup_cost", "stddev_plan_time", b"stddev_plan_time", "stddev_time", b"stddev_time", "system_time", b"system_time", "temp_blk_read_time", b"temp_blk_read_time", "temp_blk_write_time", b"temp_blk_write_time", "temp_blks_read", b"temp_blks_read", "temp_blks_written", b"temp_blks_written", "time", b"time", "total_cost", b"total_cost", "total_plan_time", b"total_plan_time", "total_time", b"total_time", "user_time", b"user_time", "wal_bytes", b"wal_bytes", "wal_fpi", b"wal_fpi", "wal_records", b"wal_records", "writes", b"writes"]) -> None: ...

global___QueryStats = QueryStats

@typing.final
class QueryStatement(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    STATS_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___PrimaryKey:
        """Primary keys in tables with the statistics on planning and execution of queries."""

    @property
    def stats(self) -> global___QueryStats:
        """Statistics on planning and execution of queries."""

    def __init__(
        self,
        *,
        key: global___PrimaryKey | None = ...,
        stats: global___QueryStats | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["key", b"key", "stats", b"stats"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "stats", b"stats"]) -> None: ...

global___QueryStatement = QueryStatement