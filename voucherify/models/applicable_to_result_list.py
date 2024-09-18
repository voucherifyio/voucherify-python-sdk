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
from typing_extensions import Annotated
from voucherify.models.applicable_to import ApplicableTo
from typing import Optional, Set
from typing_extensions import Self

class ApplicableToResultList(BaseModel):
    """
    ApplicableToResultList
    """ # noqa: E501
    data: Optional[List[ApplicableTo]] = Field(default=None, description="Contains array of items to which the discount can apply.")
    total: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Total number of objects defining included products, SKUs, or product collections.")
    object: Optional[StrictStr] = Field(default='list', description="The type of the object represented by JSON.")
    data_ref: Optional[StrictStr] = Field(default='data', description="The type of the object represented by JSON.")
    __properties: ClassVar[List[str]] = ["data", "total", "object", "data_ref"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['list']):
            raise ValueError("must be one of enum values ('list')")
        return value

    @field_validator('data_ref')
    def data_ref_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['data']):
            raise ValueError("must be one of enum values ('data')")
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
        """Create an instance of ApplicableToResultList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['data'] = _items
        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if data_ref (nullable) is None
        # and model_fields_set contains the field
        if self.data_ref is None and "data_ref" in self.model_fields_set:
            _dict['data_ref'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApplicableToResultList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [ApplicableTo.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "total": obj.get("total"),
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'data'
        })
        return _obj


