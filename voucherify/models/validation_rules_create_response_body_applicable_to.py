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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.applicable_to import ApplicableTo
from typing import Optional, Set
from typing_extensions import Self

class ValidationRulesCreateResponseBodyApplicableTo(BaseModel):
    """
    ValidationRulesCreateResponseBodyApplicableTo
    """ # noqa: E501
    excluded: Optional[List[ApplicableTo]] = Field(default=None, description="Defines which items are excluded from a discount.")
    included: Optional[List[ApplicableTo]] = Field(default=None, description="Defines which items are included in a discount.")
    included_all: Optional[StrictBool] = Field(default=None, description="Indicates whether all items are included in the discount.")
    __properties: ClassVar[List[str]] = ["excluded", "included", "included_all"]

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
        """Create an instance of ValidationRulesCreateResponseBodyApplicableTo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in excluded (list)
        _items = []
        if self.excluded:
            for _item_excluded in self.excluded:
                if _item_excluded:
                    _items.append(_item_excluded.to_dict())
            _dict['excluded'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in included (list)
        _items = []
        if self.included:
            for _item_included in self.included:
                if _item_included:
                    _items.append(_item_included.to_dict())
            _dict['included'] = _items
        # set to None if excluded (nullable) is None
        # and model_fields_set contains the field
        if self.excluded is None and "excluded" in self.model_fields_set:
            _dict['excluded'] = None

        # set to None if included (nullable) is None
        # and model_fields_set contains the field
        if self.included is None and "included" in self.model_fields_set:
            _dict['included'] = None

        # set to None if included_all (nullable) is None
        # and model_fields_set contains the field
        if self.included_all is None and "included_all" in self.model_fields_set:
            _dict['included_all'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidationRulesCreateResponseBodyApplicableTo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excluded": [ApplicableTo.from_dict(_item) for _item in obj["excluded"]] if obj.get("excluded") is not None else None,
            "included": [ApplicableTo.from_dict(_item) for _item in obj["included"]] if obj.get("included") is not None else None,
            "included_all": obj.get("included_all")
        })
        return _obj


