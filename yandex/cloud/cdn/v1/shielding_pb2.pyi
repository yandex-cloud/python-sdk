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
class ShieldingDetails(google.protobuf.message.Message):
    """Message representing the details of a shielding server."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOCATION_ID_FIELD_NUMBER: builtins.int
    DATA_CENTER_FIELD_NUMBER: builtins.int
    COUNTRY_FIELD_NUMBER: builtins.int
    CITY_FIELD_NUMBER: builtins.int
    location_id: builtins.int
    """Unique identifier for the geographical location of the shielding server."""
    data_center: builtins.str
    """Name of the data center where the shielding server is located."""
    country: builtins.str
    """Country where the shielding server's data center is located, useful for understanding geographical distribution."""
    city: builtins.str
    """City where the shielding server's data center is situated, providing a more precise location than just the country."""
    def __init__(
        self,
        *,
        location_id: builtins.int = ...,
        data_center: builtins.str = ...,
        country: builtins.str = ...,
        city: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["city", b"city", "country", b"country", "data_center", b"data_center", "location_id", b"location_id"]) -> None: ...

global___ShieldingDetails = ShieldingDetails
