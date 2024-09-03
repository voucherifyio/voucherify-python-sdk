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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.loyalties_rewards_update_assignment_request_body_parameters_loyalty import LoyaltiesRewardsUpdateAssignmentRequestBodyParametersLoyalty
from typing import Optional, Set
from typing_extensions import Self

class LoyaltiesRewardsUpdateAssignmentRequestBodyParameters(BaseModel):
    """
    An object that defines the price of the reward in loyalty points.
    """ # noqa: E501
    loyalty: Optional[LoyaltiesRewardsUpdateAssignmentRequestBodyParametersLoyalty] = None
    __properties: ClassVar[List[str]] = ["loyalty"]

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
        """Create an instance of LoyaltiesRewardsUpdateAssignmentRequestBodyParameters from a JSON string"""
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
        # set to None if loyalty (nullable) is None
        # and model_fields_set contains the field
        if self.loyalty is None and "loyalty" in self.model_fields_set:
            _dict['loyalty'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltiesRewardsUpdateAssignmentRequestBodyParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "loyalty": LoyaltiesRewardsUpdateAssignmentRequestBodyParametersLoyalty.from_dict(obj["loyalty"]) if obj.get("loyalty") is not None else None
        })
        return _obj


