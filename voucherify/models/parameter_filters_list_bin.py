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
from voucherify.models.junction import Junction
from voucherify.models.parameter_filters_list_bin_id import ParameterFiltersListBinId
from voucherify.models.parameter_filters_list_bin_resource_id import ParameterFiltersListBinResourceId
from voucherify.models.parameter_filters_list_bin_resource_name import ParameterFiltersListBinResourceName
from voucherify.models.parameter_filters_list_bin_resource_type import ParameterFiltersListBinResourceType
from typing import Optional, Set
from typing_extensions import Self

class ParameterFiltersListBin(BaseModel):
    """
    ParameterFiltersListBin
    """ # noqa: E501
    junction: Optional[Junction] = None
    id: Optional[ParameterFiltersListBinId] = None
    resource_type: Optional[ParameterFiltersListBinResourceType] = None
    resource_name: Optional[ParameterFiltersListBinResourceName] = None
    resource_id: Optional[ParameterFiltersListBinResourceId] = None
    __properties: ClassVar[List[str]] = ["junction", "id", "resource_type", "resource_name", "resource_id"]

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
        """Create an instance of ParameterFiltersListBin from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_type
        if self.resource_type:
            _dict['resource_type'] = self.resource_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_name
        if self.resource_name:
            _dict['resource_name'] = self.resource_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_id
        if self.resource_id:
            _dict['resource_id'] = self.resource_id.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if resource_type (nullable) is None
        # and model_fields_set contains the field
        if self.resource_type is None and "resource_type" in self.model_fields_set:
            _dict['resource_type'] = None

        # set to None if resource_name (nullable) is None
        # and model_fields_set contains the field
        if self.resource_name is None and "resource_name" in self.model_fields_set:
            _dict['resource_name'] = None

        # set to None if resource_id (nullable) is None
        # and model_fields_set contains the field
        if self.resource_id is None and "resource_id" in self.model_fields_set:
            _dict['resource_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParameterFiltersListBin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "junction": obj.get("junction"),
            "id": ParameterFiltersListBinId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "resource_type": ParameterFiltersListBinResourceType.from_dict(obj["resource_type"]) if obj.get("resource_type") is not None else None,
            "resource_name": ParameterFiltersListBinResourceName.from_dict(obj["resource_name"]) if obj.get("resource_name") is not None else None,
            "resource_id": ParameterFiltersListBinResourceId.from_dict(obj["resource_id"]) if obj.get("resource_id") is not None else None
        })
        return _obj


