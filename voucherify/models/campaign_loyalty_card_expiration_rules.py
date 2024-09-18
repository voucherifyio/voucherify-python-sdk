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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CampaignLoyaltyCardExpirationRules(BaseModel):
    """
    CampaignLoyaltyCardExpirationRules
    """ # noqa: E501
    period_type: Optional[StrictStr] = Field(default='MONTH', description="Type of period")
    period_value: Optional[StrictInt] = Field(default=None, description="Value of the period")
    rounding_type: Optional[StrictStr] = Field(default=None, description="Type of rounding")
    rounding_value: Optional[StrictInt] = Field(default=None, description="Value of rounding")
    __properties: ClassVar[List[str]] = ["period_type", "period_value", "rounding_type", "rounding_value"]

    @field_validator('period_type')
    def period_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MONTH']):
            raise ValueError("must be one of enum values ('MONTH')")
        return value

    @field_validator('rounding_type')
    def rounding_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['END_OF_MONTH', 'END_OF_QUARTER', 'END_OF_HALF_YEAR', 'END_OF_YEAR', 'PARTICULAR_MONTH']):
            raise ValueError("must be one of enum values ('END_OF_MONTH', 'END_OF_QUARTER', 'END_OF_HALF_YEAR', 'END_OF_YEAR', 'PARTICULAR_MONTH')")
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
        """Create an instance of CampaignLoyaltyCardExpirationRules from a JSON string"""
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
        # set to None if period_type (nullable) is None
        # and model_fields_set contains the field
        if self.period_type is None and "period_type" in self.model_fields_set:
            _dict['period_type'] = None

        # set to None if period_value (nullable) is None
        # and model_fields_set contains the field
        if self.period_value is None and "period_value" in self.model_fields_set:
            _dict['period_value'] = None

        # set to None if rounding_type (nullable) is None
        # and model_fields_set contains the field
        if self.rounding_type is None and "rounding_type" in self.model_fields_set:
            _dict['rounding_type'] = None

        # set to None if rounding_value (nullable) is None
        # and model_fields_set contains the field
        if self.rounding_value is None and "rounding_value" in self.model_fields_set:
            _dict['rounding_value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CampaignLoyaltyCardExpirationRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "period_type": obj.get("period_type") if obj.get("period_type") is not None else 'MONTH',
            "period_value": obj.get("period_value"),
            "rounding_type": obj.get("rounding_type"),
            "rounding_value": obj.get("rounding_value")
        })
        return _obj


