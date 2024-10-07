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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.validation_rule_applicable_to import ValidationRuleApplicableTo
from voucherify.models.validation_rule_error import ValidationRuleError
from typing import Optional, Set
from typing_extensions import Self

class ValidationRule(BaseModel):
    """
    ValidationRule
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Custom, unique name for set of validation rules.")
    rules: Optional[Dict[str, Any]] = Field(default=None, description="Contains all the rule definitions for the validation rule. It is a set of key value pairs representing the rules and logic between the rules. The keys are numbered consecutively beginning from `1`. The values are objects containing the rule conditions.")
    error: Optional[ValidationRuleError] = None
    applicable_to: Optional[ValidationRuleApplicableTo] = None
    type: Optional[StrictStr] = Field(default='expression', description="Type of validation rule.")
    context_type: Optional[StrictStr] = Field(default='global', description="Validation rule context type.    | **Context Type** | **Definition** | |:---|:---| | earning_rule.order.paid |  | | earning_rule.custom_event |  | | earning_rule.customer.segment.entered |  | | campaign.discount_coupons |  | | campaign.discount_coupons.discount.apply_to_order |  | | campaign.discount_coupons.discount.apply_to_items |  | | campaign.discount_coupons.discount.apply_to_items_proportionally |  | | campaign.discount_coupons.discount.apply_to_items_proportionally_by_quantity |  | | campaign.discount_coupons.discount.fixed.apply_to_items |  | | campaign.gift_vouchers |  | | campaign.gift_vouchers.gift.apply_to_order |  | | campaign.gift_vouchers.gift.apply_to_items |  | | campaign.referral_program |  | | campaign.referral_program.discount.apply_to_order |  | | campaign.referral_program.discount.apply_to_items |  | | campaign.referral_program.discount.apply_to_items_proportionally |  | | campaign.referral_program.discount.apply_to_items_proportionally_by_quantity |  | | campaign.referral_program.discount.fixed.apply_to_items |  | | campaign.promotion |  | | campaign.promotion.discount.apply_to_order |  | | campaign.promotion.discount.apply_to_items |  | | campaign.promotion.discount.apply_to_items_proportionally |  | | campaign.promotion.discount.apply_to_items_proportionally_by_quantity |  | | campaign.promotion.discount.fixed.apply_to_items |  | | campaign.loyalty_program |  | | voucher.discount_voucher |  | | voucher.discount_voucher.discount.apply_to_order |  | | voucher.discount_voucher.discount.apply_to_items |  | | voucher.discount_voucher.discount.apply_to_items_proportionally |  | | voucher.discount_voucher.discount.apply_to_items_proportionally_by_quantity |  | | voucher.discount_voucher.discount.fixed.apply_to_items |  | | voucher.gift_voucher |  | | voucher.gift_voucher.gift.apply_to_order |  | | voucher.gift_voucher.gift.apply_to_items |  | | voucher.loyalty_card |  | | distribution.custom_event |  | | reward_assignment.pay_with_points |  | | global |  |")
    id: Optional[StrictStr] = Field(default=None, description="Unique validation rule ID.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the validation rule was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the validation rule was updated. The value is shown in the ISO 8601 format.")
    assignments_count: Optional[StrictInt] = Field(default=None, description="The number of instances the validation rule has been assigned to different types of redeemables.")
    object: Optional[StrictStr] = Field(default='validation_rules', description="The type of the object represented by JSON. This object stores information about the validation rule.")
    __properties: ClassVar[List[str]] = ["name", "rules", "error", "applicable_to", "type", "context_type", "id", "created_at", "updated_at", "assignments_count", "object"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['expression', 'basic', 'advanced', 'complex']):
            raise ValueError("must be one of enum values ('expression', 'basic', 'advanced', 'complex')")
        return value

    @field_validator('context_type')
    def context_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['earning_rule.order.paid', 'earning_rule.custom_event', 'earning_rule.customer.segment.entered', 'earning_rule.customer.tier.joined', 'earning_rule.customer.tier.left', 'earning_rule.customer.tier.upgraded', 'earning_rule.customer.tier.downgraded', 'earning_rule.customer.tier.prolonged', 'campaign.discount_coupons', 'campaign.discount_coupons.discount.apply_to_order', 'campaign.discount_coupons.discount.apply_to_items', 'campaign.discount_coupons.discount.apply_to_items_proportionally', 'campaign.discount_coupons.discount.apply_to_items_proportionally_by_quantity', 'campaign.discount_coupons.discount.apply_to_items_by_quantity', 'campaign.discount_coupons.discount.fixed.apply_to_items', 'campaign.discount_coupons.discount.percent.apply_to_items', 'campaign.gift_vouchers', 'campaign.gift_vouchers.gift.apply_to_order', 'campaign.gift_vouchers.gift.apply_to_items', 'campaign.referral_program', 'campaign.referral_program.discount.apply_to_order', 'campaign.referral_program.discount.apply_to_items', 'campaign.referral_program.discount.apply_to_items_proportionally', 'campaign.referral_program.discount.apply_to_items_proportionally_by_quantity', 'campaign.referral_program.discount.apply_to_items_by_quantity', 'campaign.referral_program.discount.fixed.apply_to_items', 'campaign.referral_program.discount.percent.apply_to_items', 'campaign.promotion', 'campaign.promotion.discount.apply_to_order', 'campaign.promotion.discount.apply_to_items', 'campaign.promotion.discount.apply_to_items_proportionally', 'campaign.promotion.discount.apply_to_items_proportionally_by_quantity', 'campaign.promotion.discount.apply_to_items_by_quantity', 'campaign.promotion.discount.fixed.apply_to_items', 'campaign.promotion.discount.percent.apply_to_items', 'campaign.loyalty_program', 'voucher.discount_voucher', 'voucher.discount_voucher.discount.apply_to_order', 'voucher.discount_voucher.discount.apply_to_items', 'voucher.discount_voucher.discount.apply_to_items_proportionally', 'voucher.discount_voucher.discount.apply_to_items_proportionally_by_quantity', 'voucher.discount_voucher.discount.apply_to_items_by_quantity', 'voucher.discount_voucher.discount.fixed.apply_to_items', 'voucher.discount_voucher.discount.percent.apply_to_items', 'voucher.gift_voucher', 'voucher.gift_voucher.gift.apply_to_order', 'voucher.gift_voucher.gift.apply_to_items', 'voucher.loyalty_card', 'distribution.custom_event', 'distribution.order.paid', 'distribution.order.created', 'distribution.order.canceled', 'distribution.order.updated', 'reward_assignment.pay_with_points', 'global']):
            raise ValueError("must be one of enum values ('earning_rule.order.paid', 'earning_rule.custom_event', 'earning_rule.customer.segment.entered', 'earning_rule.customer.tier.joined', 'earning_rule.customer.tier.left', 'earning_rule.customer.tier.upgraded', 'earning_rule.customer.tier.downgraded', 'earning_rule.customer.tier.prolonged', 'campaign.discount_coupons', 'campaign.discount_coupons.discount.apply_to_order', 'campaign.discount_coupons.discount.apply_to_items', 'campaign.discount_coupons.discount.apply_to_items_proportionally', 'campaign.discount_coupons.discount.apply_to_items_proportionally_by_quantity', 'campaign.discount_coupons.discount.apply_to_items_by_quantity', 'campaign.discount_coupons.discount.fixed.apply_to_items', 'campaign.discount_coupons.discount.percent.apply_to_items', 'campaign.gift_vouchers', 'campaign.gift_vouchers.gift.apply_to_order', 'campaign.gift_vouchers.gift.apply_to_items', 'campaign.referral_program', 'campaign.referral_program.discount.apply_to_order', 'campaign.referral_program.discount.apply_to_items', 'campaign.referral_program.discount.apply_to_items_proportionally', 'campaign.referral_program.discount.apply_to_items_proportionally_by_quantity', 'campaign.referral_program.discount.apply_to_items_by_quantity', 'campaign.referral_program.discount.fixed.apply_to_items', 'campaign.referral_program.discount.percent.apply_to_items', 'campaign.promotion', 'campaign.promotion.discount.apply_to_order', 'campaign.promotion.discount.apply_to_items', 'campaign.promotion.discount.apply_to_items_proportionally', 'campaign.promotion.discount.apply_to_items_proportionally_by_quantity', 'campaign.promotion.discount.apply_to_items_by_quantity', 'campaign.promotion.discount.fixed.apply_to_items', 'campaign.promotion.discount.percent.apply_to_items', 'campaign.loyalty_program', 'voucher.discount_voucher', 'voucher.discount_voucher.discount.apply_to_order', 'voucher.discount_voucher.discount.apply_to_items', 'voucher.discount_voucher.discount.apply_to_items_proportionally', 'voucher.discount_voucher.discount.apply_to_items_proportionally_by_quantity', 'voucher.discount_voucher.discount.apply_to_items_by_quantity', 'voucher.discount_voucher.discount.fixed.apply_to_items', 'voucher.discount_voucher.discount.percent.apply_to_items', 'voucher.gift_voucher', 'voucher.gift_voucher.gift.apply_to_order', 'voucher.gift_voucher.gift.apply_to_items', 'voucher.loyalty_card', 'distribution.custom_event', 'distribution.order.paid', 'distribution.order.created', 'distribution.order.canceled', 'distribution.order.updated', 'reward_assignment.pay_with_points', 'global')")
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
        """Create an instance of ValidationRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of applicable_to
        if self.applicable_to:
            _dict['applicable_to'] = self.applicable_to.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if applicable_to (nullable) is None
        # and model_fields_set contains the field
        if self.applicable_to is None and "applicable_to" in self.model_fields_set:
            _dict['applicable_to'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if context_type (nullable) is None
        # and model_fields_set contains the field
        if self.context_type is None and "context_type" in self.model_fields_set:
            _dict['context_type'] = None

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

        # set to None if assignments_count (nullable) is None
        # and model_fields_set contains the field
        if self.assignments_count is None and "assignments_count" in self.model_fields_set:
            _dict['assignments_count'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidationRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "rules": obj.get("rules"),
            "error": ValidationRuleError.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "applicable_to": ValidationRuleApplicableTo.from_dict(obj["applicable_to"]) if obj.get("applicable_to") is not None else None,
            "type": obj.get("type") if obj.get("type") is not None else 'expression',
            "context_type": obj.get("context_type") if obj.get("context_type") is not None else 'global',
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "assignments_count": obj.get("assignments_count"),
            "object": obj.get("object") if obj.get("object") is not None else 'validation_rules'
        })
        return _obj


