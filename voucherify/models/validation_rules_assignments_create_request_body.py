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
from typing import Optional, Set
from typing_extensions import Self

class ValidationRulesAssignmentsCreateRequestBody(BaseModel):
    """
    Request body schema for **POST** `v1/validation-rules/{validationRuleId}/assignments`.
    """ # noqa: E501
    related_object_type: Optional[StrictStr] = Field(default='voucher', description="Defines the related object, e.g. `voucher`.")
    related_object_id: Optional[StrictStr] = Field(default=None, description="Unique related object ID assigned by Voucherify, e.g. `v_lfZi4rcEGe0sN9gmnj40bzwK2FH6QUno` for a voucher.")
    __properties: ClassVar[List[str]] = ["related_object_type", "related_object_id"]

    @field_validator('related_object_type')
    def related_object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['voucher', 'promotion_tier', 'campaign', 'earning_rule', 'distribution', 'reward_assignment']):
            raise ValueError("must be one of enum values ('voucher', 'promotion_tier', 'campaign', 'earning_rule', 'distribution', 'reward_assignment')")
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
        """Create an instance of ValidationRulesAssignmentsCreateRequestBody from a JSON string"""
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
        # set to None if related_object_type (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_type is None and "related_object_type" in self.model_fields_set:
            _dict['related_object_type'] = None

        # set to None if related_object_id (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_id is None and "related_object_id" in self.model_fields_set:
            _dict['related_object_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidationRulesAssignmentsCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "related_object_type": obj.get("related_object_type") if obj.get("related_object_type") is not None else 'voucher',
            "related_object_id": obj.get("related_object_id")
        })
        return _obj


