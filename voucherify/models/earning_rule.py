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
from voucherify.models.earning_rule_custom_event import EarningRuleCustomEvent
from voucherify.models.earning_rule_loyalty import EarningRuleLoyalty
from voucherify.models.earning_rule_loyalty_tier import EarningRuleLoyaltyTier
from voucherify.models.earning_rule_pending_points import EarningRulePendingPoints
from voucherify.models.earning_rule_segment import EarningRuleSegment
from voucherify.models.earning_rule_source import EarningRuleSource
from voucherify.models.validity_hours import ValidityHours
from voucherify.models.validity_timeframe import ValidityTimeframe
from typing import Optional, Set
from typing_extensions import Self

class EarningRule(BaseModel):
    """
    EarningRule
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Assigned by the Voucherify API, identifies the earning rule object.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the earning rule was created. The value is shown in the ISO 8601 format.")
    loyalty: Optional[EarningRuleLoyalty] = None
    event: Optional[StrictStr] = None
    custom_event: Optional[EarningRuleCustomEvent] = None
    segment: Optional[EarningRuleSegment] = None
    loyalty_tier: Optional[EarningRuleLoyaltyTier] = None
    pending_points: Optional[EarningRulePendingPoints] = None
    source: Optional[EarningRuleSource] = None
    object: Optional[StrictStr] = Field(default='earning_rule', description="The type of the object represented by JSON. Default is earning_rule.")
    automation_id: Optional[StrictStr] = Field(default=None, description="For internal use by Voucherify.")
    start_date: Optional[StrictStr] = Field(default=None, description="Start date defines when the earning rule starts to be active. Activation timestamp is presented in the ISO 8601 format. The earning rule is inactive before this date. If you do not define the start date for an earning rule, it will inherit the campaign start date by default.")
    expiration_date: Optional[StrictStr] = Field(default=None, description="Expiration date defines when the earning rule expires. Expiration timestamp is presented in the ISO 8601 format. The earning rule is inactive after this date. If you do not define the expiration date for an earning rule, it will inherit the campaign expiration date by default.")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[List[StrictInt]] = Field(default=None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the earning rule. A set of key/value pairs that you can attach to an earning rule object. It can be useful for storing additional information about the earning rule in a structured format.")
    validation_rule_id: Optional[StrictStr] = Field(default=None, description="A unique validation rule identifier assigned by the Voucherify API. The validation rule is verified before points are added to the balance.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the earning rule was last updated in ISO 8601 format.")
    active: Optional[StrictBool] = Field(default=None, description="A flag to toggle the earning rule on or off. You can disable an earning rule even though it's within the active period defined by the start_date and expiration_date of the campaign or the earning rule's own start_date and expiration_date.  - `true` indicates an active earning rule - `false` indicates an inactive earning rule")
    __properties: ClassVar[List[str]] = ["id", "created_at", "loyalty", "event", "custom_event", "segment", "loyalty_tier", "pending_points", "source", "object", "automation_id", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "validity_hours", "metadata", "validation_rule_id", "updated_at", "active"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['earning_rule']):
            raise ValueError("must be one of enum values ('earning_rule')")
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
        """Create an instance of EarningRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of loyalty
        if self.loyalty:
            _dict['loyalty'] = self.loyalty.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_event
        if self.custom_event:
            _dict['custom_event'] = self.custom_event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of segment
        if self.segment:
            _dict['segment'] = self.segment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_tier
        if self.loyalty_tier:
            _dict['loyalty_tier'] = self.loyalty_tier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pending_points
        if self.pending_points:
            _dict['pending_points'] = self.pending_points.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_hours
        if self.validity_hours:
            _dict['validity_hours'] = self.validity_hours.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if loyalty (nullable) is None
        # and model_fields_set contains the field
        if self.loyalty is None and "loyalty" in self.model_fields_set:
            _dict['loyalty'] = None

        # set to None if custom_event (nullable) is None
        # and model_fields_set contains the field
        if self.custom_event is None and "custom_event" in self.model_fields_set:
            _dict['custom_event'] = None

        # set to None if segment (nullable) is None
        # and model_fields_set contains the field
        if self.segment is None and "segment" in self.model_fields_set:
            _dict['segment'] = None

        # set to None if loyalty_tier (nullable) is None
        # and model_fields_set contains the field
        if self.loyalty_tier is None and "loyalty_tier" in self.model_fields_set:
            _dict['loyalty_tier'] = None

        # set to None if pending_points (nullable) is None
        # and model_fields_set contains the field
        if self.pending_points is None and "pending_points" in self.model_fields_set:
            _dict['pending_points'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if automation_id (nullable) is None
        # and model_fields_set contains the field
        if self.automation_id is None and "automation_id" in self.model_fields_set:
            _dict['automation_id'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['start_date'] = None

        # set to None if expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date is None and "expiration_date" in self.model_fields_set:
            _dict['expiration_date'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if validation_rule_id (nullable) is None
        # and model_fields_set contains the field
        if self.validation_rule_id is None and "validation_rule_id" in self.model_fields_set:
            _dict['validation_rule_id'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if active (nullable) is None
        # and model_fields_set contains the field
        if self.active is None and "active" in self.model_fields_set:
            _dict['active'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EarningRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "loyalty": EarningRuleLoyalty.from_dict(obj["loyalty"]) if obj.get("loyalty") is not None else None,
            "event": obj.get("event"),
            "custom_event": EarningRuleCustomEvent.from_dict(obj["custom_event"]) if obj.get("custom_event") is not None else None,
            "segment": EarningRuleSegment.from_dict(obj["segment"]) if obj.get("segment") is not None else None,
            "loyalty_tier": EarningRuleLoyaltyTier.from_dict(obj["loyalty_tier"]) if obj.get("loyalty_tier") is not None else None,
            "pending_points": EarningRulePendingPoints.from_dict(obj["pending_points"]) if obj.get("pending_points") is not None else None,
            "source": EarningRuleSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'earning_rule',
            "automation_id": obj.get("automation_id"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj["validity_timeframe"]) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj["validity_hours"]) if obj.get("validity_hours") is not None else None,
            "metadata": obj.get("metadata"),
            "validation_rule_id": obj.get("validation_rule_id"),
            "updated_at": obj.get("updated_at"),
            "active": obj.get("active")
        })
        return _obj


