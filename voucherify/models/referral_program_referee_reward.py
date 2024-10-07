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
from voucherify.models.referral_program_referee_reward_related_object_parent import ReferralProgramRefereeRewardRelatedObjectParent
from typing import Optional, Set
from typing_extensions import Self

class ReferralProgramRefereeReward(BaseModel):
    """
    Defines the referee reward.
    """ # noqa: E501
    related_object_parent: Optional[ReferralProgramRefereeRewardRelatedObjectParent] = None
    type: Optional[StrictStr] = Field(default=None, description="Type of reward.")
    amount: Optional[StrictStr] = Field(default=None, description="Define the number of `points` to add to a loyalty card or `credits` to the balance on a gift card. In case of the gift card, the value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000.")
    __properties: ClassVar[List[str]] = ["related_object_parent", "type", "amount"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOYALTY_CARD', 'GIFT_VOUCHER']):
            raise ValueError("must be one of enum values ('LOYALTY_CARD', 'GIFT_VOUCHER')")
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
        """Create an instance of ReferralProgramRefereeReward from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of related_object_parent
        if self.related_object_parent:
            _dict['related_object_parent'] = self.related_object_parent.to_dict()
        # set to None if related_object_parent (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_parent is None and "related_object_parent" in self.model_fields_set:
            _dict['related_object_parent'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if amount (nullable) is None
        # and model_fields_set contains the field
        if self.amount is None and "amount" in self.model_fields_set:
            _dict['amount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReferralProgramRefereeReward from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "related_object_parent": ReferralProgramRefereeRewardRelatedObjectParent.from_dict(obj["related_object_parent"]) if obj.get("related_object_parent") is not None else None,
            "type": obj.get("type"),
            "amount": obj.get("amount")
        })
        return _obj


