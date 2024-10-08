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
from voucherify.models.list_publications_item_voucher import ListPublicationsItemVoucher
from voucherify.models.publications_list_response_body_publications_item_metadata import PublicationsListResponseBodyPublicationsItemMetadata
from typing import Optional, Set
from typing_extensions import Self

class PublicationsListResponseBodyPublicationsItem(BaseModel):
    """
    PublicationsListResponseBodyPublicationsItem
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique publication ID, assigned by Voucherify.")
    object: Optional[StrictStr] = Field(default='publication', description="The type of the object represented by the JSON. This object stores information about the `publication`.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the publication was created. The value is shown in the ISO 8601 format.")
    customer_id: Optional[StrictStr] = Field(default=None, description="Unique customer ID of the customer receiving the publication.")
    tracking_id: Optional[StrictStr] = Field(default=None, description="Customer's `source_id`.")
    metadata: Optional[PublicationsListResponseBodyPublicationsItemMetadata] = None
    channel: Optional[StrictStr] = Field(default=None, description="How the publication was originated. It can be your own custom channel or an example value provided here.")
    source_id: Optional[StrictStr] = Field(default=None, description="The merchant's publication ID if it is different from the Voucherify publication ID. It's an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. ")
    customer: Optional[CustomerWithSummaryLoyaltyReferrals] = None
    vouchers: Optional[List[StrictStr]] = Field(default=None, description="Contains the voucher IDs that was assigned by Voucherify. and Contains the unique voucher codes that was assigned by Voucherify.")
    vouchers_id: Optional[List[StrictStr]] = Field(default=None, description="Contains the unique internal voucher IDs that was assigned by Voucherify.")
    result: Optional[StrictStr] = None
    voucher: Optional[ListPublicationsItemVoucher] = None
    failure_code: Optional[StrictStr] = Field(default=None, description="Generic reason as to why the create publication operation failed.")
    failure_message: Optional[StrictStr] = Field(default=None, description="This parameter will provide more expanded reason as to why the create publication operation failed.")
    __properties: ClassVar[List[str]] = ["id", "object", "created_at", "customer_id", "tracking_id", "metadata", "channel", "source_id", "customer", "vouchers", "vouchers_id", "result", "voucher", "failure_code", "failure_message"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['publication']):
            raise ValueError("must be one of enum values ('publication')")
        return value

    @field_validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SUCCESS', 'FAILURE']):
            raise ValueError("must be one of enum values ('SUCCESS', 'FAILURE')")
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
        """Create an instance of PublicationsListResponseBodyPublicationsItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
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

        # set to None if channel (nullable) is None
        # and model_fields_set contains the field
        if self.channel is None and "channel" in self.model_fields_set:
            _dict['channel'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['source_id'] = None

        # set to None if vouchers_id (nullable) is None
        # and model_fields_set contains the field
        if self.vouchers_id is None and "vouchers_id" in self.model_fields_set:
            _dict['vouchers_id'] = None

        # set to None if failure_code (nullable) is None
        # and model_fields_set contains the field
        if self.failure_code is None and "failure_code" in self.model_fields_set:
            _dict['failure_code'] = None

        # set to None if failure_message (nullable) is None
        # and model_fields_set contains the field
        if self.failure_message is None and "failure_message" in self.model_fields_set:
            _dict['failure_message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicationsListResponseBodyPublicationsItem from a dict"""
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
            "metadata": PublicationsListResponseBodyPublicationsItemMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "channel": obj.get("channel"),
            "source_id": obj.get("source_id"),
            "customer": CustomerWithSummaryLoyaltyReferrals.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "vouchers": obj.get("vouchers"),
            "vouchers_id": obj.get("vouchers_id"),
            "result": obj.get("result"),
            "voucher": ListPublicationsItemVoucher.from_dict(obj["voucher"]) if obj.get("voucher") is not None else None,
            "failure_code": obj.get("failure_code"),
            "failure_message": obj.get("failure_message")
        })
        return _obj


