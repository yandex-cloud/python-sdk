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

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class S3APIGetObjectResponse(google.protobuf.message.Message):
    """Represents a response of the get object request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class MetadataEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    ETAG_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    ACCEPT_RANGES_FIELD_NUMBER: builtins.int
    CACHE_CONTROL_FIELD_NUMBER: builtins.int
    CONTENT_DISPOSITION_FIELD_NUMBER: builtins.int
    CONTENT_ENCODING_FIELD_NUMBER: builtins.int
    CONTENT_LANGUAGE_FIELD_NUMBER: builtins.int
    CONTENT_LENGTH_FIELD_NUMBER: builtins.int
    CONTENT_RANGE_FIELD_NUMBER: builtins.int
    CONTENT_TYPE_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    EXPIRES_AT_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_AT_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    STORAGE_CLASS_FIELD_NUMBER: builtins.int
    SERVER_SIDE_ENCRYPTION_FIELD_NUMBER: builtins.int
    SSE_KMS_KEY_ID_FIELD_NUMBER: builtins.int
    OBJECT_LOCK_MODE_FIELD_NUMBER: builtins.int
    OBJECT_LOCK_RETAIN_UNTIL_DATE_FIELD_NUMBER: builtins.int
    OBJECT_LOCK_LEGAL_HOLD_STATUS_FIELD_NUMBER: builtins.int
    etag: builtins.str
    """MD5 hash of the object."""
    request_id: builtins.str
    """Unique request ID."""
    accept_ranges: builtins.str
    """Indicates that a range of bytes was specified in the request."""
    cache_control: builtins.str
    """Specifies caching behavior along the request/reply chain."""
    content_disposition: builtins.str
    """Specifies presentational information for the object."""
    content_encoding: builtins.str
    """Indicates what content encodings have been applied to the object."""
    content_language: builtins.str
    """The language the content is in."""
    content_length: builtins.int
    """Size of the body in bytes."""
    content_range: builtins.str
    """The portion of the object returned in the response."""
    content_type: builtins.str
    """A standard MIME type describing the format of the object data."""
    version_id: builtins.str
    """Version ID of the object."""
    storage_class: builtins.str
    """Provides storage class information of the object."""
    server_side_encryption: builtins.str
    """Encryption algorithm used to encrypt the object."""
    sse_kms_key_id: builtins.str
    """ID of the key KMS."""
    object_lock_mode: builtins.str
    """Type of retention put on the object."""
    object_lock_legal_hold_status: builtins.str
    """Type of legal hold put on the object"""
    @property
    def expires_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date and time at which the object is no longer cacheable."""

    @property
    def last_modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Date and time when the object was last modified."""

    @property
    def metadata(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Object user-defined metadata."""

    @property
    def object_lock_retain_until_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Date and time until which the object is retained"""

    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        request_id: builtins.str = ...,
        accept_ranges: builtins.str = ...,
        cache_control: builtins.str = ...,
        content_disposition: builtins.str = ...,
        content_encoding: builtins.str = ...,
        content_language: builtins.str = ...,
        content_length: builtins.int = ...,
        content_range: builtins.str = ...,
        content_type: builtins.str = ...,
        version_id: builtins.str = ...,
        expires_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        metadata: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        storage_class: builtins.str = ...,
        server_side_encryption: builtins.str = ...,
        sse_kms_key_id: builtins.str = ...,
        object_lock_mode: builtins.str = ...,
        object_lock_retain_until_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        object_lock_legal_hold_status: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["expires_at", b"expires_at", "last_modified_at", b"last_modified_at", "object_lock_retain_until_date", b"object_lock_retain_until_date"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["accept_ranges", b"accept_ranges", "cache_control", b"cache_control", "content_disposition", b"content_disposition", "content_encoding", b"content_encoding", "content_language", b"content_language", "content_length", b"content_length", "content_range", b"content_range", "content_type", b"content_type", "etag", b"etag", "expires_at", b"expires_at", "last_modified_at", b"last_modified_at", "metadata", b"metadata", "object_lock_legal_hold_status", b"object_lock_legal_hold_status", "object_lock_mode", b"object_lock_mode", "object_lock_retain_until_date", b"object_lock_retain_until_date", "request_id", b"request_id", "server_side_encryption", b"server_side_encryption", "sse_kms_key_id", b"sse_kms_key_id", "storage_class", b"storage_class", "version_id", b"version_id"]) -> None: ...

global___S3APIGetObjectResponse = S3APIGetObjectResponse

@typing.final
class S3APIPutObjectResponse(google.protobuf.message.Message):
    """Represents a response of the put object request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    etag: builtins.str
    """MD5 hash of the object."""
    request_id: builtins.str
    """Unique request ID."""
    version_id: builtins.str
    """Version ID of the object."""
    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        request_id: builtins.str = ...,
        version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["etag", b"etag", "request_id", b"request_id", "version_id", b"version_id"]) -> None: ...

global___S3APIPutObjectResponse = S3APIPutObjectResponse

@typing.final
class S3APIDeleteObjectResponse(google.protobuf.message.Message):
    """Represents a response of the delete object request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    version_id: builtins.str
    """Version ID of the object."""
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id", "version_id", b"version_id"]) -> None: ...

global___S3APIDeleteObjectResponse = S3APIDeleteObjectResponse

@typing.final
class CopyObjectResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ETAG_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_AT_FIELD_NUMBER: builtins.int
    etag: builtins.str
    """Returns the ETag of the new object."""
    @property
    def last_modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Creation date of the object."""

    def __init__(
        self,
        *,
        etag: builtins.str = ...,
        last_modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["last_modified_at", b"last_modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["etag", b"etag", "last_modified_at", b"last_modified_at"]) -> None: ...

global___CopyObjectResult = CopyObjectResult

@typing.final
class S3APICopyObjectResponse(google.protobuf.message.Message):
    """Represents a response of the copy object request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COPY_OBJECT_RESULT_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    COPY_SOURCE_VERSION_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    copy_source_version_id: builtins.str
    """Version ID of the source object that was copied."""
    version_id: builtins.str
    """Version ID of the newly created copy."""
    @property
    def copy_object_result(self) -> global___CopyObjectResult:
        """Container for all response elements."""

    def __init__(
        self,
        *,
        copy_object_result: global___CopyObjectResult | None = ...,
        request_id: builtins.str = ...,
        copy_source_version_id: builtins.str = ...,
        version_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["copy_object_result", b"copy_object_result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["copy_object_result", b"copy_object_result", "copy_source_version_id", b"copy_source_version_id", "request_id", b"request_id", "version_id", b"version_id"]) -> None: ...

global___S3APICopyObjectResponse = S3APICopyObjectResponse

@typing.final
class SuccessfullyDeletedObject(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    DELETE_MARKER_FIELD_NUMBER: builtins.int
    DELETE_MARKER_VERSION_ID_FIELD_NUMBER: builtins.int
    key: builtins.str
    """The name of the deleted object."""
    version_id: builtins.str
    """The version ID of the deleted object."""
    delete_marker: builtins.bool
    """Specifies whether the versioned object that was permanently deleted was (true) or was not (false) a delete marker."""
    delete_marker_version_id: builtins.str
    """The version ID of the delete marker created as a result of the DELETE operation."""
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        version_id: builtins.str = ...,
        delete_marker: builtins.bool = ...,
        delete_marker_version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["delete_marker", b"delete_marker", "delete_marker_version_id", b"delete_marker_version_id", "key", b"key", "version_id", b"version_id"]) -> None: ...

global___SuccessfullyDeletedObject = SuccessfullyDeletedObject

@typing.final
class DeleteObjectError(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    key: builtins.str
    """The error key."""
    version_id: builtins.str
    """The version ID of the error."""
    code: builtins.str
    """The error code is a string that uniquely identifies an error condition."""
    msg: builtins.str
    """The error message contains a generic description of the error condition in English."""
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        version_id: builtins.str = ...,
        code: builtins.str = ...,
        msg: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["code", b"code", "key", b"key", "msg", b"msg", "version_id", b"version_id"]) -> None: ...

global___DeleteObjectError = DeleteObjectError

@typing.final
class S3APIDeleteObjectsResponse(google.protobuf.message.Message):
    """Represents a response of the delete objects request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DELETED_FIELD_NUMBER: builtins.int
    ERRORS_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    @property
    def deleted(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SuccessfullyDeletedObject]:
        """List of successfully deleted objects"""

    @property
    def errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeleteObjectError]:
        """List of objects that attempted to be deleted but encountered an error"""

    def __init__(
        self,
        *,
        deleted: collections.abc.Iterable[global___SuccessfullyDeletedObject] | None = ...,
        errors: collections.abc.Iterable[global___DeleteObjectError] | None = ...,
        request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["deleted", b"deleted", "errors", b"errors", "request_id", b"request_id"]) -> None: ...

global___S3APIDeleteObjectsResponse = S3APIDeleteObjectsResponse

@typing.final
class S3APIPutObjectRetentionResponse(google.protobuf.message.Message):
    """Represents a response of the put object retention request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id"]) -> None: ...

global___S3APIPutObjectRetentionResponse = S3APIPutObjectRetentionResponse

@typing.final
class ObjectLockRetention(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MODE_FIELD_NUMBER: builtins.int
    RETAIN_UNTIL_DATE_FIELD_NUMBER: builtins.int
    mode: builtins.str
    """Indicates the Retention mode for the specified object."""
    @property
    def retain_until_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """The date on which this object lock retention will expire."""

    def __init__(
        self,
        *,
        mode: builtins.str = ...,
        retain_until_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["retain_until_date", b"retain_until_date"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["mode", b"mode", "retain_until_date", b"retain_until_date"]) -> None: ...

global___ObjectLockRetention = ObjectLockRetention

@typing.final
class S3APIGetObjectRetentionResponse(google.protobuf.message.Message):
    """Represents a response of the get object retention request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    RETENTION_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    @property
    def retention(self) -> global___ObjectLockRetention:
        """An object retention settings."""

    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        retention: global___ObjectLockRetention | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["retention", b"retention"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id", "retention", b"retention"]) -> None: ...

global___S3APIGetObjectRetentionResponse = S3APIGetObjectRetentionResponse

@typing.final
class S3APIPutObjectLegalHoldResponse(google.protobuf.message.Message):
    """Represents a response of the put object retention request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id"]) -> None: ...

global___S3APIPutObjectLegalHoldResponse = S3APIPutObjectLegalHoldResponse

@typing.final
class ObjectLockLegalHold(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    status: builtins.str
    """Indicates whether the specified object has a legal hold in place."""
    def __init__(
        self,
        *,
        status: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["status", b"status"]) -> None: ...

global___ObjectLockLegalHold = ObjectLockLegalHold

@typing.final
class S3APIGetObjectLegalHoldResponse(google.protobuf.message.Message):
    """Represents a response of the get object legal hold request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    LEGAL_HOLD_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    @property
    def legal_hold(self) -> global___ObjectLockLegalHold:
        """The current legal hold status for the specified object."""

    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        legal_hold: global___ObjectLockLegalHold | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["legal_hold", b"legal_hold"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["legal_hold", b"legal_hold", "request_id", b"request_id"]) -> None: ...

global___S3APIGetObjectLegalHoldResponse = S3APIGetObjectLegalHoldResponse

@typing.final
class S3APIPutObjectTaggingResponse(google.protobuf.message.Message):
    """Represents a response of put object tagging request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    version_id: builtins.str
    """The versionId of the object the tag-set was added to."""
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id", "version_id", b"version_id"]) -> None: ...

global___S3APIPutObjectTaggingResponse = S3APIPutObjectTaggingResponse

@typing.final
class ObjectTag(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.str
    """Key of the object tag."""
    value: builtins.str
    """Value of the object tag."""
    def __init__(
        self,
        *,
        key: builtins.str = ...,
        value: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

global___ObjectTag = ObjectTag

@typing.final
class S3APIGetObjectTaggingResponse(google.protobuf.message.Message):
    """Represents a response of get object tagging request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    TAG_SET_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    version_id: builtins.str
    """The versionId of the object for which you got the tagging information."""
    @property
    def tag_set(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ObjectTag]:
        """Contains the tag set."""

    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        version_id: builtins.str = ...,
        tag_set: collections.abc.Iterable[global___ObjectTag] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id", "tag_set", b"tag_set", "version_id", b"version_id"]) -> None: ...

global___S3APIGetObjectTaggingResponse = S3APIGetObjectTaggingResponse

@typing.final
class S3APIDeleteObjectTaggingResponse(google.protobuf.message.Message):
    """Represents a response of delete object tagging request to S3."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    VERSION_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """Unique request ID."""
    version_id: builtins.str
    """The versionId of the object the tag-set was removed from."""
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        version_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id", "version_id", b"version_id"]) -> None: ...

global___S3APIDeleteObjectTaggingResponse = S3APIDeleteObjectTaggingResponse
