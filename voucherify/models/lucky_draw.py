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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class LuckyDraw(BaseModel):
    """
    Object for defining detailed information about lucky draw should be applied
    """ # noqa: E501
    winners_count: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="It represents the total number of winners in a lucky draw.")
    unique_winners_per_draw: Optional[StrictStr] = Field(default=None, description="It indicates whether each winner in a draw is unique or not.")
    unique_winners: Optional[StrictStr] = Field(default=None, description="Specifies whether each participant can win only once across multiple draws.")
    __properties: ClassVar[List[str]] = ["winners_count", "unique_winners_per_draw", "unique_winners"]

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
        """Create an instance of LuckyDraw from a JSON string"""
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
        # set to None if winners_count (nullable) is None
        # and model_fields_set contains the field
        if self.winners_count is None and "winners_count" in self.model_fields_set:
            _dict['winners_count'] = None

        # set to None if unique_winners_per_draw (nullable) is None
        # and model_fields_set contains the field
        if self.unique_winners_per_draw is None and "unique_winners_per_draw" in self.model_fields_set:
            _dict['unique_winners_per_draw'] = None

        # set to None if unique_winners (nullable) is None
        # and model_fields_set contains the field
        if self.unique_winners is None and "unique_winners" in self.model_fields_set:
            _dict['unique_winners'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LuckyDraw from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "winners_count": obj.get("winners_count"),
            "unique_winners_per_draw": obj.get("unique_winners_per_draw"),
            "unique_winners": obj.get("unique_winners")
        })
        return _obj

