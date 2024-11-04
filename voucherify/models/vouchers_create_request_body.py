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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.code_config import CodeConfig
from voucherify.models.discount import Discount
from voucherify.models.gift import Gift
from voucherify.models.simple_loyalty_card import SimpleLoyaltyCard
from voucherify.models.validity_hours import ValidityHours
from voucherify.models.validity_timeframe import ValidityTimeframe
from voucherify.models.vouchers_create_request_body_redemption import VouchersCreateRequestBodyRedemption
from typing import Optional, Set
from typing_extensions import Self

class VouchersCreateRequestBody(BaseModel):
    """
    VouchersCreateRequestBody
    """ # noqa: E501
    code: Optional[StrictStr] = Field(default=None, description="Code that identifies a voucher. The pattern can use all the letters of the English alphabet, Arabic numerals, and special characters. Pass this attribute in the request body to create a distinct code. Otherwise, either use the `code_config` object to set the rules that the Voucherify API will use to create a random code, or don't pass any code and Voucherify will generate a random code.")
    campaign: Optional[StrictStr] = Field(default=None, description="Identifies the voucher's parent campaign using a unique campaign name.")
    campaign_id: Optional[StrictStr] = Field(default=None, description="Identifies the voucher's parent campaign using a unique campaign ID assigned by the Voucherify API.")
    category: Optional[StrictStr] = Field(default=None, description="The name of the category that this voucher belongs to. Useful when listing vouchers with the [List Vouchers](ref:list-vouchers) endpoint.")
    category_id: Optional[StrictStr] = Field(default=None, description="Unique identifier assigned by Voucherify to the name of the category that this voucher belongs to. Useful when listing vouchers with the [List Vouchers](ref:list-vouchers) endpoint.")
    start_date: Optional[datetime] = Field(default=None, description="Start date defines when the code starts to be active. Activation timestamp is presented in the ISO 8601 format. Voucher is *inactive before* this date.")
    expiration_date: Optional[datetime] = Field(default=None, description="Expiration date defines when the code expires. Expiration timestamp is presented in the ISO 8601 format.  Voucher is *inactive after* this date.")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[List[StrictInt]] = Field(default=None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    active: Optional[StrictBool] = Field(default=None, description="A flag to toggle the voucher on or off. You can disable a voucher even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* voucher - `false` indicates an *inactive* voucher")
    additional_info: Optional[StrictStr] = Field(default=None, description="An optional field to keep any extra textual information about the code such as a code description and details.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the code. A set of key/value pairs that you can attach to a voucher object. It can be useful for storing additional information about the voucher in a structured format.")
    validation_rules: Optional[List[StrictStr]] = Field(default=None, description="Array containing the ID of the validation rule associated with the voucher.")
    redemption: Optional[VouchersCreateRequestBodyRedemption] = None
    type: Optional[StrictStr] = None
    loyalty_card: Optional[SimpleLoyaltyCard] = None
    code_config: Optional[CodeConfig] = None
    gift: Optional[Gift] = None
    discount: Optional[Discount] = None
    __properties: ClassVar[List[str]] = ["code", "campaign", "campaign_id", "category", "category_id", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "validity_hours", "active", "additional_info", "metadata", "validation_rules", "redemption", "type", "loyalty_card", "code_config", "gift", "discount"]

    @field_validator('validity_day_of_week')
    def validity_day_of_week_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set([0, 1, 2, 3, 4, 5, 6]):
                raise ValueError("each list item must be one of (0, 1, 2, 3, 4, 5, 6)")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOYALTY_CARD', 'GIFT_VOUCHER', 'DISCOUNT_VOUCHER']):
            raise ValueError("must be one of enum values ('LOYALTY_CARD', 'GIFT_VOUCHER', 'DISCOUNT_VOUCHER')")
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
        """Create an instance of VouchersCreateRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_hours
        if self.validity_hours:
            _dict['validity_hours'] = self.validity_hours.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_card
        if self.loyalty_card:
            _dict['loyalty_card'] = self.loyalty_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code_config
        if self.code_config:
            _dict['code_config'] = self.code_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['discount'] = self.discount.to_dict()
        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and "code" in self.model_fields_set:
            _dict['code'] = None

        # set to None if campaign (nullable) is None
        # and model_fields_set contains the field
        if self.campaign is None and "campaign" in self.model_fields_set:
            _dict['campaign'] = None

        # set to None if campaign_id (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_id is None and "campaign_id" in self.model_fields_set:
            _dict['campaign_id'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['start_date'] = None

        # set to None if expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date is None and "expiration_date" in self.model_fields_set:
            _dict['expiration_date'] = None

        # set to None if active (nullable) is None
        # and model_fields_set contains the field
        if self.active is None and "active" in self.model_fields_set:
            _dict['active'] = None

        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additional_info'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if validation_rules (nullable) is None
        # and model_fields_set contains the field
        if self.validation_rules is None and "validation_rules" in self.model_fields_set:
            _dict['validation_rules'] = None

        # set to None if redemption (nullable) is None
        # and model_fields_set contains the field
        if self.redemption is None and "redemption" in self.model_fields_set:
            _dict['redemption'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VouchersCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "campaign": obj.get("campaign"),
            "campaign_id": obj.get("campaign_id"),
            "category": obj.get("category"),
            "category_id": obj.get("category_id"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj["validity_timeframe"]) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj["validity_hours"]) if obj.get("validity_hours") is not None else None,
            "active": obj.get("active"),
            "additional_info": obj.get("additional_info"),
            "metadata": obj.get("metadata"),
            "validation_rules": obj.get("validation_rules"),
            "redemption": VouchersCreateRequestBodyRedemption.from_dict(obj["redemption"]) if obj.get("redemption") is not None else None,
            "type": obj.get("type"),
            "loyalty_card": SimpleLoyaltyCard.from_dict(obj["loyalty_card"]) if obj.get("loyalty_card") is not None else None,
            "code_config": CodeConfig.from_dict(obj["code_config"]) if obj.get("code_config") is not None else None,
            "gift": Gift.from_dict(obj["gift"]) if obj.get("gift") is not None else None,
            "discount": Discount.from_dict(obj["discount"]) if obj.get("discount") is not None else None
        })
        return _obj


