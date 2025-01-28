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
from typing_extensions import Annotated
from voucherify.models.access_settings import AccessSettings
from voucherify.models.campaign_loyalty_voucher import CampaignLoyaltyVoucher
from voucherify.models.validity_hours import ValidityHours
from voucherify.models.validity_timeframe import ValidityTimeframe
from typing import Optional, Set
from typing_extensions import Self

class LoyaltiesCreateCampaignRequestBody(BaseModel):
    """
    Request body schema for **POST** `/loyalties`.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Campaign name.")
    description: Optional[StrictStr] = Field(default=None, description="An optional field to keep any extra textual information about the campaign such as a campaign description and details.")
    type: Optional[StrictStr] = Field(default=None, description="Defines whether the campaign can be updated with new vouchers after campaign creation or if the campaign consists of standalone vouchers.  - `AUTO_UPDATE`: the campaign is dynamic, i.e. vouchers will generate based on set criteria -  `STATIC`: vouchers need to be manually published")
    join_once: Optional[StrictBool] = Field(default=None, description="If this value is set to `true`, customers will be able to join the campaign only once.")
    auto_join: Optional[StrictBool] = Field(default=None, description="Indicates whether customers will be able to auto-join a loyalty campaign if any earning rule is fulfilled.")
    use_voucher_metadata_schema: Optional[StrictBool] = Field(default=None, description="Flag indicating whether the campaign is to use the voucher's metadata schema instead of the campaign metadata schema.")
    vouchers_count: Optional[StrictInt] = Field(default=None, description="Total number of unique vouchers in campaign (size of campaign).")
    start_date: Optional[datetime] = Field(default=None, description="Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(default=None, description="Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date.")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[List[StrictInt]] = Field(default=None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    activity_duration_after_publishing: Optional[StrictStr] = Field(default=None, description="Defines the amount of time the vouchers will be active after publishing. The value is shown in the ISO 8601 format. For example, a voucher with the value of P24D will be valid for a duration of 24 days.")
    category_id: Optional[StrictStr] = Field(default=None, description="Unique category ID that this campaign belongs to. Either pass this parameter OR the `category`.")
    category: Optional[StrictStr] = Field(default=None, description="The category assigned to the campaign. Either pass this parameter OR the `category_id`.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the campaign. A set of key/value pairs that you can attach to a campaign object. It can be useful for storing additional information about the campaign in a structured format.")
    access_settings: Optional[AccessSettings] = None
    validation_rules: Optional[Annotated[List[StrictStr], Field(max_length=1)]] = Field(default=None, description="Array containing the ID of the validation rule associated with the promotion tier.")
    campaign_type: Optional[StrictStr] = Field(default='LOYALTY_PROGRAM', description="Type of campaign.")
    voucher: Optional[CampaignLoyaltyVoucher] = None
    __properties: ClassVar[List[str]] = ["name", "description", "type", "join_once", "auto_join", "use_voucher_metadata_schema", "vouchers_count", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "validity_hours", "activity_duration_after_publishing", "category_id", "category", "metadata", "access_settings", "validation_rules", "campaign_type", "voucher"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AUTO_UPDATE', 'STATIC']):
            raise ValueError("must be one of enum values ('AUTO_UPDATE', 'STATIC')")
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

    @field_validator('campaign_type')
    def campaign_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOYALTY_PROGRAM']):
            raise ValueError("must be one of enum values ('LOYALTY_PROGRAM')")
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
        """Create an instance of LoyaltiesCreateCampaignRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_settings
        if self.access_settings:
            _dict['access_settings'] = self.access_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if join_once (nullable) is None
        # and model_fields_set contains the field
        if self.join_once is None and "join_once" in self.model_fields_set:
            _dict['join_once'] = None

        # set to None if auto_join (nullable) is None
        # and model_fields_set contains the field
        if self.auto_join is None and "auto_join" in self.model_fields_set:
            _dict['auto_join'] = None

        # set to None if use_voucher_metadata_schema (nullable) is None
        # and model_fields_set contains the field
        if self.use_voucher_metadata_schema is None and "use_voucher_metadata_schema" in self.model_fields_set:
            _dict['use_voucher_metadata_schema'] = None

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

        # set to None if activity_duration_after_publishing (nullable) is None
        # and model_fields_set contains the field
        if self.activity_duration_after_publishing is None and "activity_duration_after_publishing" in self.model_fields_set:
            _dict['activity_duration_after_publishing'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if validation_rules (nullable) is None
        # and model_fields_set contains the field
        if self.validation_rules is None and "validation_rules" in self.model_fields_set:
            _dict['validation_rules'] = None

        # set to None if campaign_type (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_type is None and "campaign_type" in self.model_fields_set:
            _dict['campaign_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltiesCreateCampaignRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "join_once": obj.get("join_once"),
            "auto_join": obj.get("auto_join"),
            "use_voucher_metadata_schema": obj.get("use_voucher_metadata_schema"),
            "vouchers_count": obj.get("vouchers_count"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj["validity_timeframe"]) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj["validity_hours"]) if obj.get("validity_hours") is not None else None,
            "activity_duration_after_publishing": obj.get("activity_duration_after_publishing"),
            "category_id": obj.get("category_id"),
            "category": obj.get("category"),
            "metadata": obj.get("metadata"),
            "access_settings": AccessSettings.from_dict(obj["access_settings"]) if obj.get("access_settings") is not None else None,
            "validation_rules": obj.get("validation_rules"),
            "campaign_type": obj.get("campaign_type") if obj.get("campaign_type") is not None else 'LOYALTY_PROGRAM',
            "voucher": CampaignLoyaltyVoucher.from_dict(obj["voucher"]) if obj.get("voucher") is not None else None
        })
        return _obj


