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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class RewardTypeCoin(BaseModel):
    """
    Defines the ratio by mapping the number of loyalty points in points_ratio to a predefined cash amount in exchange_ratio.
    """ # noqa: E501
    exchange_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The cash equivalent of the points defined in the points_ratio property.")
    points_ratio: Optional[StrictInt] = Field(default=None, description="The number of loyalty points that will map to the predefined cash amount defined by the exchange_ratio property.")
    __properties: ClassVar[List[str]] = ["exchange_ratio", "points_ratio"]

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
        """Create an instance of RewardTypeCoin from a JSON string"""
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
        # set to None if exchange_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.exchange_ratio is None and "exchange_ratio" in self.model_fields_set:
            _dict['exchange_ratio'] = None

        # set to None if points_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.points_ratio is None and "points_ratio" in self.model_fields_set:
            _dict['points_ratio'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RewardTypeCoin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exchange_ratio": obj.get("exchange_ratio"),
            "points_ratio": obj.get("points_ratio")
        })
        return _obj


