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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LoyaltiesRewardsCreateAssignmentResponseBodyParametersLoyalty(BaseModel):
    """
    Defines the equivalent points value of the reward.
    """ # noqa: E501
    points: Optional[StrictInt] = Field(default=None, description="The number of points required to redeem the reward.")
    auto_redeem: Optional[StrictBool] = Field(default=None, description="Determines if the reward is redeemed automatically when the customer reaches the sufficient number of points to redeem it. Value `true` means that the automatic reward redemption is active. Only one reward can be set to be redeemed automatically in a loyalty campaign, i.e. only one can have the value `true`.")
    __properties: ClassVar[List[str]] = ["points", "auto_redeem"]

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
        """Create an instance of LoyaltiesRewardsCreateAssignmentResponseBodyParametersLoyalty from a JSON string"""
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

        # set to None if auto_redeem (nullable) is None
        # and model_fields_set contains the field
        if self.auto_redeem is None and "auto_redeem" in self.model_fields_set:
            _dict['auto_redeem'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltiesRewardsCreateAssignmentResponseBodyParametersLoyalty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "points": obj.get("points"),
            "auto_redeem": obj.get("auto_redeem")
        })
        return _obj


