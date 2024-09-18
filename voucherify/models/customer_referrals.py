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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.customer_referrals_campaigns_item import CustomerReferralsCampaignsItem
from typing import Optional, Set
from typing_extensions import Self

class CustomerReferrals(BaseModel):
    """
    Summary of customer's referrals, in this case, the customer being the referee, i.e. information about the source of referrals and number of times the customer was referred by other customers.
    """ # noqa: E501
    total: Optional[StrictInt] = Field(default=None, description="Total number of times this customer received a referral, i.e. was referred by another customer.")
    campaigns: Optional[List[CustomerReferralsCampaignsItem]] = Field(default=None, description="Contains an array of campaigns that served as the source of a referral for the customer.")
    __properties: ClassVar[List[str]] = ["total", "campaigns"]

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
        """Create an instance of CustomerReferrals from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in campaigns (list)
        _items = []
        if self.campaigns:
            for _item_campaigns in self.campaigns:
                if _item_campaigns:
                    _items.append(_item_campaigns.to_dict())
            _dict['campaigns'] = _items
        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if campaigns (nullable) is None
        # and model_fields_set contains the field
        if self.campaigns is None and "campaigns" in self.model_fields_set:
            _dict['campaigns'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerReferrals from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total": obj.get("total"),
            "campaigns": [CustomerReferralsCampaignsItem.from_dict(_item) for _item in obj["campaigns"]] if obj.get("campaigns") is not None else None
        })
        return _obj


