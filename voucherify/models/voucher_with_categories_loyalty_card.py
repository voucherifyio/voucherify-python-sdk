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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class VoucherWithCategoriesLoyaltyCard(BaseModel):
    """
    Object representing loyalty card parameters. Child attributes are present only if `type` is `LOYALTY_CARD`. Defaults to `null`.
    """ # noqa: E501
    points: Optional[StrictInt] = Field(default=None, description="Total points incurred over the lifespan of the loyalty card, minus the expired points.")
    balance: Optional[StrictInt] = Field(default=None, description="Points available for reward redemption.")
    next_expiration_date: Optional[date] = Field(default=None, description="The next closest date when the next set of points are due to expire.")
    next_expiration_points: Optional[StrictInt] = Field(default=None, description="The amount of points that are set to expire next.")
    pending_points: Optional[StrictInt] = Field(default=None, description="Determines the number of pending points that will be added to the loyalty card after the predefined time.")
    __properties: ClassVar[List[str]] = ["points", "balance", "next_expiration_date", "next_expiration_points", "pending_points"]

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
        """Create an instance of VoucherWithCategoriesLoyaltyCard from a JSON string"""
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
        # set to None if points (nullable) is None
        # and model_fields_set contains the field
        if self.points is None and "points" in self.model_fields_set:
            _dict['points'] = None

        # set to None if balance (nullable) is None
        # and model_fields_set contains the field
        if self.balance is None and "balance" in self.model_fields_set:
            _dict['balance'] = None

        # set to None if next_expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.next_expiration_date is None and "next_expiration_date" in self.model_fields_set:
            _dict['next_expiration_date'] = None

        # set to None if next_expiration_points (nullable) is None
        # and model_fields_set contains the field
        if self.next_expiration_points is None and "next_expiration_points" in self.model_fields_set:
            _dict['next_expiration_points'] = None

        # set to None if pending_points (nullable) is None
        # and model_fields_set contains the field
        if self.pending_points is None and "pending_points" in self.model_fields_set:
            _dict['pending_points'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VoucherWithCategoriesLoyaltyCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "points": obj.get("points"),
            "balance": obj.get("balance"),
            "next_expiration_date": obj.get("next_expiration_date"),
            "next_expiration_points": obj.get("next_expiration_points"),
            "pending_points": obj.get("pending_points")
        })
        return _obj


