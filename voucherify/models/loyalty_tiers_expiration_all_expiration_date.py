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
from voucherify.models.loyalty_tiers_expiration_all_expiration_date_rounding import LoyaltyTiersExpirationAllExpirationDateRounding
from typing import Optional, Set
from typing_extensions import Self

class LoyaltyTiersExpirationAllExpirationDate(BaseModel):
    """
    Defines the conditions for the expiration date of a tier.
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="What triggers the tier to expire for a customer.     `END_OF_PERIOD`: Expire tier at the end of the period.     `END_OF_NEXT_PERIOD`:  Expire tier at the end of the next period.   `BALANCE_DROP`: Tier expires when the points balance drops below the required range of the tier.   `CUSTOM`: Tier expires after a certain time period passes following the instance the points balance drops below the required range of the tier.")
    extend: Optional[StrictStr] = Field(default=None, description="Extend the expiration by adding extra months or days in ISO 8601 format. The tier will remain active even though it reaches its expiration time period. For example, a tier with a duration of `P3M` will be valid for an additional duration of 3 months and a tier with a duration of `P1D` will be valid for an additional duration of 1 day.")
    rounding: Optional[LoyaltyTiersExpirationAllExpirationDateRounding] = None
    __properties: ClassVar[List[str]] = ["type", "extend", "rounding"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['END_OF_PERIOD', 'END_OF_NEXT_PERIOD', 'BALANCE_DROP', 'CUSTOM']):
            raise ValueError("must be one of enum values ('END_OF_PERIOD', 'END_OF_NEXT_PERIOD', 'BALANCE_DROP', 'CUSTOM')")
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
        """Create an instance of LoyaltyTiersExpirationAllExpirationDate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rounding
        if self.rounding:
            _dict['rounding'] = self.rounding.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if extend (nullable) is None
        # and model_fields_set contains the field
        if self.extend is None and "extend" in self.model_fields_set:
            _dict['extend'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltyTiersExpirationAllExpirationDate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "extend": obj.get("extend"),
            "rounding": LoyaltyTiersExpirationAllExpirationDateRounding.from_dict(obj["rounding"]) if obj.get("rounding") is not None else None
        })
        return _obj

