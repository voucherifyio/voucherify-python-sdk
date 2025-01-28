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
from voucherify.models.access_settings_campaign_assignments_list import AccessSettingsCampaignAssignmentsList
from voucherify.models.campaign_voucher import CampaignVoucher
from voucherify.models.category import Category
from voucherify.models.loyalty_tiers_expiration_all import LoyaltyTiersExpirationAll
from voucherify.models.referral_program import ReferralProgram
from voucherify.models.validity_hours import ValidityHours
from voucherify.models.validity_timeframe import ValidityTimeframe
from typing import Optional, Set
from typing_extensions import Self

class CampaignBase(BaseModel):
    """
    This is an object representing a campaign.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique campaign ID, assigned by Voucherify.")
    name: Optional[StrictStr] = Field(default=None, description="Campaign name.")
    description: Optional[StrictStr] = Field(default=None, description="An optional field to keep any extra textual information about the campaign such as a campaign description and details.")
    campaign_type: Optional[StrictStr] = Field(default=None, description="Type of campaign.")
    type: Optional[StrictStr] = Field(default=None, description="Defines whether the campaign can be updated with new vouchers after campaign creation or if the campaign consists of standalone vouchers.  - `AUTO_UPDATE`: the campaign is dynamic, i.e. vouchers will generate based on set criteria -  `STATIC`: vouchers need to be manually published - `STANDALONE`: campaign for single vouchers")
    voucher: Optional[CampaignVoucher] = None
    auto_join: Optional[StrictBool] = Field(default=None, description="Indicates whether customers will be able to auto-join a loyalty campaign if any earning rule is fulfilled.")
    join_once: Optional[StrictBool] = Field(default=None, description="If this value is set to `true`, customers will be able to join the campaign only once. It is always `false` for standalone voucher campaigns and it cannot be changed in them.")
    use_voucher_metadata_schema: Optional[StrictBool] = Field(default=None, description="Flag indicating whether the campaign is to use the voucher's metadata schema instead of the campaign metadata schema.")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[List[StrictInt]] = Field(default=None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    activity_duration_after_publishing: Optional[StrictStr] = Field(default=None, description="Defines the amount of time the vouchers will be active after publishing. The value is shown in the ISO 8601 format. For example, a voucher with the value of P24D will be valid for a duration of 24 days.")
    vouchers_count: Optional[StrictInt] = Field(default=None, description="Total number of unique vouchers in campaign.")
    start_date: Optional[datetime] = Field(default=None, description="Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(default=None, description="Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date.")
    active: Optional[StrictBool] = Field(default=None, description="A flag to toggle the campaign on or off. You can disable a campaign even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* campaign - `false` indicates an *inactive* campaign")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the campaign. A set of key/value pairs that you can attach to a campaign object. It can be useful for storing additional information about the campaign in a structured format.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the campaign was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the campaign was last updated in ISO 8601 format.")
    category: Optional[StrictStr] = Field(default=None, description="Unique category name.")
    creation_status: Optional[StrictStr] = Field(default=None, description="Indicates the status of the campaign creation.")
    vouchers_generation_status: Optional[StrictStr] = Field(default=None, description="Indicates the status of the campaign's voucher generation.")
    readonly: Optional[StrictBool] = Field(default=None, description="Indicates whether the campaign can be only read by a restricted user in the Areas and Stores enterprise feature. It is returned only to restricted users; this field is not returned for users with other roles.")
    protected: Optional[StrictBool] = Field(default=None, description="Indicates whether the resource can be deleted.")
    category_id: Optional[StrictStr] = Field(default=None, description="Unique category ID that this campaign belongs to.")
    categories: Optional[List[Category]] = Field(default=None, description="Contains details about the category.")
    object: Optional[StrictStr] = Field(default='campaign', description="The type of the object represented by JSON. This object stores information about the campaign.")
    referral_program: Optional[ReferralProgram] = None
    loyalty_tiers_expiration: Optional[LoyaltyTiersExpirationAll] = None
    access_settings_assignments: Optional[AccessSettingsCampaignAssignmentsList] = None
    __properties: ClassVar[List[str]] = ["id", "name", "description", "campaign_type", "type", "voucher", "auto_join", "join_once", "use_voucher_metadata_schema", "validity_timeframe", "validity_day_of_week", "validity_hours", "activity_duration_after_publishing", "vouchers_count", "start_date", "expiration_date", "active", "metadata", "created_at", "updated_at", "category", "creation_status", "vouchers_generation_status", "readonly", "protected", "category_id", "categories", "object", "referral_program", "loyalty_tiers_expiration", "access_settings_assignments"]

    @field_validator('campaign_type')
    def campaign_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOYALTY_PROGRAM', 'GIFT_VOUCHERS', 'DISCOUNT_COUPONS', 'PROMOTION', 'REFERRAL_PROGRAM']):
            raise ValueError("must be one of enum values ('LOYALTY_PROGRAM', 'GIFT_VOUCHERS', 'DISCOUNT_COUPONS', 'PROMOTION', 'REFERRAL_PROGRAM')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AUTO_UPDATE', 'STATIC', 'STANDALONE']):
            raise ValueError("must be one of enum values ('AUTO_UPDATE', 'STATIC', 'STANDALONE')")
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

    @field_validator('creation_status')
    def creation_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DONE', 'IN_PROGRESS', 'FAILED', 'DRAFT', 'MODIFYING']):
            raise ValueError("must be one of enum values ('DONE', 'IN_PROGRESS', 'FAILED', 'DRAFT', 'MODIFYING')")
        return value

    @field_validator('vouchers_generation_status')
    def vouchers_generation_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DONE', 'IN_PROGRESS', 'FAILED', 'DRAFT', 'MODIFYING']):
            raise ValueError("must be one of enum values ('DONE', 'IN_PROGRESS', 'FAILED', 'DRAFT', 'MODIFYING')")
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
        """Create an instance of CampaignBase from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_hours
        if self.validity_hours:
            _dict['validity_hours'] = self.validity_hours.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item_categories in self.categories:
                if _item_categories:
                    _items.append(_item_categories.to_dict())
            _dict['categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of referral_program
        if self.referral_program:
            _dict['referral_program'] = self.referral_program.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_tiers_expiration
        if self.loyalty_tiers_expiration:
            _dict['loyalty_tiers_expiration'] = self.loyalty_tiers_expiration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of access_settings_assignments
        if self.access_settings_assignments:
            _dict['access_settings_assignments'] = self.access_settings_assignments.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if campaign_type (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_type is None and "campaign_type" in self.model_fields_set:
            _dict['campaign_type'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if auto_join (nullable) is None
        # and model_fields_set contains the field
        if self.auto_join is None and "auto_join" in self.model_fields_set:
            _dict['auto_join'] = None

        # set to None if join_once (nullable) is None
        # and model_fields_set contains the field
        if self.join_once is None and "join_once" in self.model_fields_set:
            _dict['join_once'] = None

        # set to None if use_voucher_metadata_schema (nullable) is None
        # and model_fields_set contains the field
        if self.use_voucher_metadata_schema is None and "use_voucher_metadata_schema" in self.model_fields_set:
            _dict['use_voucher_metadata_schema'] = None

        # set to None if activity_duration_after_publishing (nullable) is None
        # and model_fields_set contains the field
        if self.activity_duration_after_publishing is None and "activity_duration_after_publishing" in self.model_fields_set:
            _dict['activity_duration_after_publishing'] = None

        # set to None if vouchers_count (nullable) is None
        # and model_fields_set contains the field
        if self.vouchers_count is None and "vouchers_count" in self.model_fields_set:
            _dict['vouchers_count'] = None

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

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if creation_status (nullable) is None
        # and model_fields_set contains the field
        if self.creation_status is None and "creation_status" in self.model_fields_set:
            _dict['creation_status'] = None

        # set to None if vouchers_generation_status (nullable) is None
        # and model_fields_set contains the field
        if self.vouchers_generation_status is None and "vouchers_generation_status" in self.model_fields_set:
            _dict['vouchers_generation_status'] = None

        # set to None if readonly (nullable) is None
        # and model_fields_set contains the field
        if self.readonly is None and "readonly" in self.model_fields_set:
            _dict['readonly'] = None

        # set to None if protected (nullable) is None
        # and model_fields_set contains the field
        if self.protected is None and "protected" in self.model_fields_set:
            _dict['protected'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CampaignBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "campaign_type": obj.get("campaign_type"),
            "type": obj.get("type"),
            "voucher": CampaignVoucher.from_dict(obj["voucher"]) if obj.get("voucher") is not None else None,
            "auto_join": obj.get("auto_join"),
            "join_once": obj.get("join_once"),
            "use_voucher_metadata_schema": obj.get("use_voucher_metadata_schema"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj["validity_timeframe"]) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj["validity_hours"]) if obj.get("validity_hours") is not None else None,
            "activity_duration_after_publishing": obj.get("activity_duration_after_publishing"),
            "vouchers_count": obj.get("vouchers_count"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "active": obj.get("active"),
            "metadata": obj.get("metadata"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "category": obj.get("category"),
            "creation_status": obj.get("creation_status"),
            "vouchers_generation_status": obj.get("vouchers_generation_status"),
            "readonly": obj.get("readonly"),
            "protected": obj.get("protected"),
            "category_id": obj.get("category_id"),
            "categories": [Category.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'campaign',
            "referral_program": ReferralProgram.from_dict(obj["referral_program"]) if obj.get("referral_program") is not None else None,
            "loyalty_tiers_expiration": LoyaltyTiersExpirationAll.from_dict(obj["loyalty_tiers_expiration"]) if obj.get("loyalty_tiers_expiration") is not None else None,
            "access_settings_assignments": AccessSettingsCampaignAssignmentsList.from_dict(obj["access_settings_assignments"]) if obj.get("access_settings_assignments") is not None else None
        })
        return _obj


