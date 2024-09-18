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

class ValidityHoursDailyItem(BaseModel):
    """
    Defines the reccuring period(s) when the resource will be active.
    """ # noqa: E501
    start_time: Optional[StrictStr] = Field(default=None, description="Defines the starting hour of validity in the HH:mm format. The resource is *inactive before* this time.")
    days_of_week: Optional[List[StrictInt]] = Field(default=None, description="Integer array corresponding to the particular days of the week in which the resource is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3`  Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    expiration_time: Optional[StrictStr] = Field(default=None, description="Defines the ending hour of validity in the HH:mm format. The resource is *inactive after* this time.")
    __properties: ClassVar[List[str]] = ["start_time", "days_of_week", "expiration_time"]

    @field_validator('days_of_week')
    def days_of_week_validate_enum(cls, value):
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
        """Create an instance of ValidityHoursDailyItem from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidityHoursDailyItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "start_time": obj.get("start_time"),
            "days_of_week": obj.get("days_of_week"),
            "expiration_time": obj.get("expiration_time")
        })
        return _obj


