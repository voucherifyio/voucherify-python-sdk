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
from voucherify.models.parameter_filters_list_locations_created_at import ParameterFiltersListLocationsCreatedAt
from voucherify.models.parameter_filters_list_locations_name import ParameterFiltersListLocationsName
from voucherify.models.parameter_filters_list_locations_updated_at import ParameterFiltersListLocationsUpdatedAt
from typing import Optional, Set
from typing_extensions import Self

class ParameterFiltersListLocations(BaseModel):
    """
    ParameterFiltersListLocations
    """ # noqa: E501
    name: Optional[ParameterFiltersListLocationsName] = None
    created_at: Optional[ParameterFiltersListLocationsCreatedAt] = None
    updated_at: Optional[ParameterFiltersListLocationsUpdatedAt] = None
    __properties: ClassVar[List[str]] = ["name", "created_at", "updated_at"]

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
        """Create an instance of ParameterFiltersListLocations from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_at
        if self.updated_at:
            _dict['updated_at'] = self.updated_at.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParameterFiltersListLocations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": ParameterFiltersListLocationsName.from_dict(obj["name"]) if obj.get("name") is not None else None,
            "created_at": ParameterFiltersListLocationsCreatedAt.from_dict(obj["created_at"]) if obj.get("created_at") is not None else None,
            "updated_at": ParameterFiltersListLocationsUpdatedAt.from_dict(obj["updated_at"]) if obj.get("updated_at") is not None else None
        })
        return _obj


