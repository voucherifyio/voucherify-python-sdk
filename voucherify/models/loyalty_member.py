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
from voucherify.models.loyalty_member_loyalty_card import LoyaltyMemberLoyaltyCard
from voucherify.models.loyalty_member_publish import LoyaltyMemberPublish
from voucherify.models.loyalty_member_redemption import LoyaltyMemberRedemption
from voucherify.models.validity_hours import ValidityHours
from voucherify.models.validity_timeframe import ValidityTimeframe
from voucherify.models.voucher_assets import VoucherAssets
from typing import Optional, Set
from typing_extensions import Self

class LoyaltyMember(BaseModel):
    """
    This is an object representing a loyalty member.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Assigned by the Voucherify API, identifies the voucher.")
    code: Optional[StrictStr] = Field(default=None, description="A code that identifies a voucher. Pattern can use all letters of the English alphabet, Arabic numerals, and special characters.")
    campaign: Optional[StrictStr] = Field(default=None, description="A unique campaign name, identifies the voucher's parent campaign.")
    campaign_id: Optional[StrictStr] = Field(default=None, description="Assigned by the Voucherify API, identifies the voucher's parent campaign.")
    category: Optional[StrictStr] = Field(default=None, description="Tag defining the category that this voucher belongs to.")
    category_id: Optional[StrictStr] = Field(default=None, description="Unique category ID assigned by Voucherify.")
    type: Optional[StrictStr] = Field(default='LOYALTY_CARD', description="Defines the type of the voucher. ")
    discount: Optional[Dict[str, Any]] = None
    gift: Optional[Dict[str, Any]] = None
    loyalty_card: Optional[LoyaltyMemberLoyaltyCard] = None
    start_date: Optional[datetime] = Field(default=None, description="Activation timestamp defines when the code starts to be active in ISO 8601 format. Voucher is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(default=None, description="Expiration timestamp defines when the code expires in ISO 8601 format.  Voucher is *inactive after* this date.")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[List[StrictInt]] = Field(default=None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    active: Optional[StrictBool] = Field(default=None, description="A flag to toggle the voucher on or off. You can disable a voucher even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* voucher - `false` indicates an *inactive* voucher")
    additional_info: Optional[StrictStr] = Field(default=None, description="An optional field to keep any extra textual information about the code such as a code description and details.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the code. A set of key/value pairs that you can attach to a voucher object. It can be useful for storing additional information about the voucher in a structured format.")
    assets: Optional[VoucherAssets] = None
    is_referral_code: Optional[StrictBool] = Field(default=None, description="This is always false for loyalty members.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the voucher was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the voucher was last updated in ISO 8601 format.")
    holder_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the customer who owns the voucher.")
    object: Optional[StrictStr] = Field(default='voucher', description="The type of the object represented by JSON. Default is `voucher`.")
    publish: Optional[LoyaltyMemberPublish] = None
    redemption: Optional[LoyaltyMemberRedemption] = None
    __properties: ClassVar[List[str]] = ["id", "code", "campaign", "campaign_id", "category", "category_id", "type", "discount", "gift", "loyalty_card", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "validity_hours", "active", "additional_info", "metadata", "assets", "is_referral_code", "created_at", "updated_at", "holder_id", "object", "publish", "redemption"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOYALTY_CARD']):
            raise ValueError("must be one of enum values ('LOYALTY_CARD')")
        return value

    @field_validator('validity_day_of_week')
    def validity_day_of_week_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set([0, 1, 2, 3, 4, 5, 6]):
                raise ValueError("each list item must be one of (0, 1, 2, 3, 4, 5, 6)")
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
        """Create an instance of LoyaltyMember from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_hours
        if self.validity_hours:
            _dict['validity_hours'] = self.validity_hours.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of publish
        if self.publish:
            _dict['publish'] = self.publish.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

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

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if discount (nullable) is None
        # and model_fields_set contains the field
        if self.discount is None and "discount" in self.model_fields_set:
            _dict['discount'] = None

        # set to None if gift (nullable) is None
        # and model_fields_set contains the field
        if self.gift is None and "gift" in self.model_fields_set:
            _dict['gift'] = None

        # set to None if loyalty_card (nullable) is None
        # and model_fields_set contains the field
        if self.loyalty_card is None and "loyalty_card" in self.model_fields_set:
            _dict['loyalty_card'] = None

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

        # set to None if is_referral_code (nullable) is None
        # and model_fields_set contains the field
        if self.is_referral_code is None and "is_referral_code" in self.model_fields_set:
            _dict['is_referral_code'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if holder_id (nullable) is None
        # and model_fields_set contains the field
        if self.holder_id is None and "holder_id" in self.model_fields_set:
            _dict['holder_id'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if publish (nullable) is None
        # and model_fields_set contains the field
        if self.publish is None and "publish" in self.model_fields_set:
            _dict['publish'] = None

        # set to None if redemption (nullable) is None
        # and model_fields_set contains the field
        if self.redemption is None and "redemption" in self.model_fields_set:
            _dict['redemption'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltyMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "code": obj.get("code"),
            "campaign": obj.get("campaign"),
            "campaign_id": obj.get("campaign_id"),
            "category": obj.get("category"),
            "category_id": obj.get("category_id"),
            "type": obj.get("type") if obj.get("type") is not None else 'LOYALTY_CARD',
            "discount": obj.get("discount"),
            "gift": obj.get("gift"),
            "loyalty_card": LoyaltyMemberLoyaltyCard.from_dict(obj["loyalty_card"]) if obj.get("loyalty_card") is not None else None,
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj["validity_timeframe"]) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj["validity_hours"]) if obj.get("validity_hours") is not None else None,
            "active": obj.get("active"),
            "additional_info": obj.get("additional_info"),
            "metadata": obj.get("metadata"),
            "assets": VoucherAssets.from_dict(obj["assets"]) if obj.get("assets") is not None else None,
            "is_referral_code": obj.get("is_referral_code"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "holder_id": obj.get("holder_id"),
            "object": obj.get("object") if obj.get("object") is not None else 'voucher',
            "publish": LoyaltyMemberPublish.from_dict(obj["publish"]) if obj.get("publish") is not None else None,
            "redemption": LoyaltyMemberRedemption.from_dict(obj["redemption"]) if obj.get("redemption") is not None else None
        })
        return _obj


