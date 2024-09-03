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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class CustomerReferralsCampaignsItem(BaseModel):
    """
    Contains information about the source of the referral.
    """ # noqa: E501
    campaign_id: StrictStr = Field(description="Unique campaign ID, assigned by Voucherify.")
    referrer_id: StrictStr = Field(description="Unique referrer ID, assigned by Voucherify. This is the customer ID of a customer that is referring this customer.")
    related_object_id: StrictStr = Field(description="Related object id")
    related_object_type: StrictStr = Field(description="Related object type, i.e. `redemption`.")
    var_date: datetime = Field(description="Timestamp representing the date and time when the customer was referred in ISO 8601 format.", alias="date")
    __properties: ClassVar[List[str]] = ["campaign_id", "referrer_id", "related_object_id", "related_object_type", "date"]

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
        """Create an instance of CustomerReferralsCampaignsItem from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerReferralsCampaignsItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaign_id": obj.get("campaign_id"),
            "referrer_id": obj.get("referrer_id"),
            "related_object_id": obj.get("related_object_id"),
            "related_object_type": obj.get("related_object_type"),
            "date": obj.get("date")
        })
        return _obj


