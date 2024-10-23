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
from voucherify.models.campaign_loyalty_card import CampaignLoyaltyCard
from voucherify.models.campaign_loyalty_voucher_redemption import CampaignLoyaltyVoucherRedemption
from voucherify.models.code_config import CodeConfig
from typing import Optional, Set
from typing_extensions import Self

class CampaignLoyaltyVoucher(BaseModel):
    """
    Schema model for a discount voucher.
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default='LOYALTY_CARD', description="Type of voucher.")
    loyalty_card: CampaignLoyaltyCard
    redemption: Optional[CampaignLoyaltyVoucherRedemption] = None
    code_config: Optional[CodeConfig] = None
    __properties: ClassVar[List[str]] = ["type", "loyalty_card", "redemption", "code_config"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOYALTY_CARD']):
            raise ValueError("must be one of enum values ('LOYALTY_CARD')")
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
        """Create an instance of CampaignLoyaltyVoucher from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of loyalty_card
        if self.loyalty_card:
            _dict['loyalty_card'] = self.loyalty_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code_config
        if self.code_config:
            _dict['code_config'] = self.code_config.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if redemption (nullable) is None
        # and model_fields_set contains the field
        if self.redemption is None and "redemption" in self.model_fields_set:
            _dict['redemption'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CampaignLoyaltyVoucher from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type") if obj.get("type") is not None else 'LOYALTY_CARD',
            "loyalty_card": CampaignLoyaltyCard.from_dict(obj["loyalty_card"]) if obj.get("loyalty_card") is not None else None,
            "redemption": CampaignLoyaltyVoucherRedemption.from_dict(obj["redemption"]) if obj.get("redemption") is not None else None,
            "code_config": CodeConfig.from_dict(obj["code_config"]) if obj.get("code_config") is not None else None
        })
        return _obj

