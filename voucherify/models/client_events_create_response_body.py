# coding: utf-8

"""
    Voucherify API

    Voucherify promotion engine REST API. Please see https://docs.voucherify.io/docs for more details.

    The version of the OpenAPI document: v2018-08-01
    Contact: support@voucherify.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.simple_customer_required_object_type import SimpleCustomerRequiredObjectType
from typing import Optional, Set
from typing_extensions import Self

class ClientEventsCreateResponseBody(BaseModel):
    """
    Response body schema for **POST** `v1/events`.
    """ # noqa: E501
    object: Optional[StrictStr] = Field(default='event', description="The object represented is an `event`.")
    type: Optional[StrictStr] = Field(default=None, description="The event name.")
    customer: SimpleCustomerRequiredObjectType
    referral: Optional[Dict[str, Any]] = Field(default=None, description="A `null` referral object.")
    loyalty: Optional[Dict[str, Any]] = Field(default=None, description="A `null` loyalty object.")
    metadata: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["object", "type", "customer", "referral", "loyalty", "metadata"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['event']):
            raise ValueError("must be one of enum values ('event')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ClientEventsCreateResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if referral (nullable) is None
        # and model_fields_set contains the field
        if self.referral is None and "referral" in self.model_fields_set:
            _dict['referral'] = None

        # set to None if loyalty (nullable) is None
        # and model_fields_set contains the field
        if self.loyalty is None and "loyalty" in self.model_fields_set:
            _dict['loyalty'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientEventsCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'event',
            "type": obj.get("type"),
            "customer": SimpleCustomerRequiredObjectType.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "referral": obj.get("referral"),
            "loyalty": obj.get("loyalty"),
            "metadata": obj.get("metadata")
        })
        return _obj

