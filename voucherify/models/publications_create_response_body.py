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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.customer_with_summary_loyalty_referrals import CustomerWithSummaryLoyaltyReferrals
from voucherify.models.voucher import Voucher
from typing import Optional, Set
from typing_extensions import Self

class PublicationsCreateResponseBody(BaseModel):
    """
    PublicationsCreateResponseBody
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique publication ID, assigned by Voucherify.")
    object: Optional[StrictStr] = Field(default='publication', description="The type of the object represented by the JSON. This object stores information about the `publication`.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the publication was created. The value is shown in the ISO 8601 format.")
    customer_id: Optional[StrictStr] = Field(default=None, description="Unique customer ID of the customer receiving the publication.")
    tracking_id: Optional[StrictStr] = Field(default=None, description="Customer's `source_id`.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the publication. A set of key/value pairs that you can attach to a publication object. It can be useful for storing additional information about the publication in a structured format.")
    channel: Optional[StrictStr] = Field(default='API', description="How the publication was originated. It can be your own custom channel or an example value provided here.")
    source_id: Optional[StrictStr] = Field(default=None, description="The merchant's publication ID if it is different from the Voucherify publication ID. It's an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. ")
    result: Optional[StrictStr] = Field(default='SUCCESS', description="Status of the publication attempt.")
    customer: Optional[CustomerWithSummaryLoyaltyReferrals] = None
    vouchers_id: Optional[List[StrictStr]] = Field(default=None, description="Contains the unique internal voucher ID that was assigned by Voucherify.")
    voucher: Optional[Voucher] = None
    vouchers: Optional[List[StrictStr]] = Field(default=None, description="Contains the unique voucher codes that was assigned by Voucherify.")
    __properties: ClassVar[List[str]] = ["id", "object", "created_at", "customer_id", "tracking_id", "metadata", "channel", "source_id", "result", "customer", "vouchers_id", "voucher", "vouchers"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['publication']):
            raise ValueError("must be one of enum values ('publication')")
        return value

    @field_validator('channel')
    def channel_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['API']):
            raise ValueError("must be one of enum values ('API')")
        return value

    @field_validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SUCCESS']):
            raise ValueError("must be one of enum values ('SUCCESS')")
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
        """Create an instance of PublicationsCreateResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customer_id'] = None

        # set to None if tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_id is None and "tracking_id" in self.model_fields_set:
            _dict['tracking_id'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if channel (nullable) is None
        # and model_fields_set contains the field
        if self.channel is None and "channel" in self.model_fields_set:
            _dict['channel'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['source_id'] = None

        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict['result'] = None

        # set to None if vouchers_id (nullable) is None
        # and model_fields_set contains the field
        if self.vouchers_id is None and "vouchers_id" in self.model_fields_set:
            _dict['vouchers_id'] = None

        # set to None if vouchers (nullable) is None
        # and model_fields_set contains the field
        if self.vouchers is None and "vouchers" in self.model_fields_set:
            _dict['vouchers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicationsCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "object": obj.get("object") if obj.get("object") is not None else 'publication',
            "created_at": obj.get("created_at"),
            "customer_id": obj.get("customer_id"),
            "tracking_id": obj.get("tracking_id"),
            "metadata": obj.get("metadata"),
            "channel": obj.get("channel") if obj.get("channel") is not None else 'API',
            "source_id": obj.get("source_id"),
            "result": obj.get("result") if obj.get("result") is not None else 'SUCCESS',
            "customer": CustomerWithSummaryLoyaltyReferrals.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "vouchers_id": obj.get("vouchers_id"),
            "voucher": Voucher.from_dict(obj["voucher"]) if obj.get("voucher") is not None else None,
            "vouchers": obj.get("vouchers")
        })
        return _obj


