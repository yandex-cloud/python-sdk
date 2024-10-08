"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class RuleSetDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class RuleDescription(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ID_FIELD_NUMBER: builtins.int
        ANOMALY_SCORE_FIELD_NUMBER: builtins.int
        PARANOIA_LEVEL_FIELD_NUMBER: builtins.int
        id: builtins.str
        """ID of the rule"""
        anomaly_score: builtins.int
        """Numeric anomaly value, i.e., a potential attack indicator.
        The higher this value, the more likely it is that the request that satisfies the rule is an attack.
        See [documentation](/docs/smartwebsecurity/concepts/waf#anomaly).
        """
        paranoia_level: builtins.int
        """Paranoia level classifies rules according to their aggression.
        The higher the paranoia level, the better your protection, but also the higher the probability of WAF false positives.
        See [documentation](/docs/smartwebsecurity/concepts/waf#paranoia).
        """
        def __init__(
            self,
            *,
            id: builtins.str = ...,
            anomaly_score: builtins.int = ...,
            paranoia_level: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["anomaly_score", b"anomaly_score", "id", b"id", "paranoia_level", b"paranoia_level"]) -> None: ...

    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    RULES_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the rule set"""
    version: builtins.str
    """Version of the rule set"""
    id: builtins.str
    """ID of the rule set"""
    @property
    def rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RuleSetDescriptor.RuleDescription]:
        """List of rules"""

    def __init__(
        self,
        *,
        name: builtins.str = ...,
        version: builtins.str = ...,
        id: builtins.str = ...,
        rules: collections.abc.Iterable[global___RuleSetDescriptor.RuleDescription] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id", "name", b"name", "rules", b"rules", "version", b"version"]) -> None: ...

global___RuleSetDescriptor = RuleSetDescriptor
