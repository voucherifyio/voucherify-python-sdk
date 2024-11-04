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
from voucherify.models.category import Category
from voucherify.models.redemption_entry_promotion_tier_action import RedemptionEntryPromotionTierAction
from voucherify.models.redemption_entry_promotion_tier_campaign import RedemptionEntryPromotionTierCampaign
from voucherify.models.redemption_entry_promotion_tier_summary import RedemptionEntryPromotionTierSummary
from voucherify.models.validation_rule_assignments_list import ValidationRuleAssignmentsList
from voucherify.models.validity_hours import ValidityHours
from voucherify.models.validity_timeframe import ValidityTimeframe
from typing import Optional, Set
from typing_extensions import Self

class RedemptionEntryPromotionTier(BaseModel):
    """
    RedemptionEntryPromotionTier
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique promotion tier ID.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the promotion tier was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the promotion tier was updated. The value is shown in the ISO 8601 format.")
    name: Optional[StrictStr] = Field(default=None, description="Name of the promotion tier.")
    banner: Optional[StrictStr] = Field(default=None, description="Text to be displayed to your customers on your website.")
    action: Optional[RedemptionEntryPromotionTierAction] = None
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the promotion tier. A set of key/value pairs that you can attach to a promotion tier object. It can be useful for storing additional information about the promotion tier in a structured format.")
    hierarchy: Optional[StrictInt] = Field(default=None, description="The promotions hierarchy defines the order in which the discounts from different tiers will be applied to a customer's order. If a customer qualifies for discounts from more than one tier, discounts will be applied in the order defined in the hierarchy.")
    promotion_id: Optional[StrictStr] = Field(default=None, description="Promotion unique ID.")
    campaign: Optional[RedemptionEntryPromotionTierCampaign] = None
    campaign_id: Optional[StrictStr] = Field(default=None, description="Promotion tier's parent campaign's unique ID.")
    active: Optional[StrictBool] = Field(default=None, description="A flag to toggle the promotion tier on or off. You can disable a promotion tier even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* promotion tier - `false` indicates an *inactive* promotion tier")
    start_date: Optional[datetime] = Field(default=None, description="Activation timestamp defines when the promotion tier starts to be active in ISO 8601 format. Promotion tier is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(default=None, description="Activation timestamp defines when the promotion tier expires in ISO 8601 format. Promotion tier is *inactive after* this date. ")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[List[StrictInt]] = Field(default=None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    summary: Optional[RedemptionEntryPromotionTierSummary] = None
    object: Optional[StrictStr] = Field(default='promotion_tier', description="The type of the object represented by JSON. This object stores information about the promotion tier.")
    validation_rule_assignments: Optional[ValidationRuleAssignmentsList] = None
    category_id: Optional[StrictStr] = Field(default=None, description="Promotion tier category ID.")
    categories: Optional[List[Category]] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "name", "banner", "action", "metadata", "hierarchy", "promotion_id", "campaign", "campaign_id", "active", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "validity_hours", "summary", "object", "validation_rule_assignments", "category_id", "categories"]

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
        """Create an instance of RedemptionEntryPromotionTier from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_hours
        if self.validity_hours:
            _dict['validity_hours'] = self.validity_hours.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validation_rule_assignments
        if self.validation_rule_assignments:
            _dict['validation_rule_assignments'] = self.validation_rule_assignments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item_categories in self.categories:
                if _item_categories:
                    _items.append(_item_categories.to_dict())
            _dict['categories'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if banner (nullable) is None
        # and model_fields_set contains the field
        if self.banner is None and "banner" in self.model_fields_set:
            _dict['banner'] = None

        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if hierarchy (nullable) is None
        # and model_fields_set contains the field
        if self.hierarchy is None and "hierarchy" in self.model_fields_set:
            _dict['hierarchy'] = None

        # set to None if promotion_id (nullable) is None
        # and model_fields_set contains the field
        if self.promotion_id is None and "promotion_id" in self.model_fields_set:
            _dict['promotion_id'] = None

        # set to None if campaign (nullable) is None
        # and model_fields_set contains the field
        if self.campaign is None and "campaign" in self.model_fields_set:
            _dict['campaign'] = None

        # set to None if campaign_id (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_id is None and "campaign_id" in self.model_fields_set:
            _dict['campaign_id'] = None

        # set to None if active (nullable) is None
        # and model_fields_set contains the field
        if self.active is None and "active" in self.model_fields_set:
            _dict['active'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['start_date'] = None

        # set to None if expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date is None and "expiration_date" in self.model_fields_set:
            _dict['expiration_date'] = None

        # set to None if summary (nullable) is None
        # and model_fields_set contains the field
        if self.summary is None and "summary" in self.model_fields_set:
            _dict['summary'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RedemptionEntryPromotionTier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "name": obj.get("name"),
            "banner": obj.get("banner"),
            "action": RedemptionEntryPromotionTierAction.from_dict(obj["action"]) if obj.get("action") is not None else None,
            "metadata": obj.get("metadata"),
            "hierarchy": obj.get("hierarchy"),
            "promotion_id": obj.get("promotion_id"),
            "campaign": RedemptionEntryPromotionTierCampaign.from_dict(obj["campaign"]) if obj.get("campaign") is not None else None,
            "campaign_id": obj.get("campaign_id"),
            "active": obj.get("active"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj["validity_timeframe"]) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj["validity_hours"]) if obj.get("validity_hours") is not None else None,
            "summary": RedemptionEntryPromotionTierSummary.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'promotion_tier',
            "validation_rule_assignments": ValidationRuleAssignmentsList.from_dict(obj["validation_rule_assignments"]) if obj.get("validation_rule_assignments") is not None else None,
            "category_id": obj.get("category_id"),
            "categories": [Category.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None
        })
        return _obj


