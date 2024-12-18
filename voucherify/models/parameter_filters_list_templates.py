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
from voucherify.models.parameter_filters_list_templates_campaign_type import ParameterFiltersListTemplatesCampaignType
from voucherify.models.parameter_filters_list_templates_id import ParameterFiltersListTemplatesId
from voucherify.models.parameter_filters_list_templates_name import ParameterFiltersListTemplatesName
from typing import Optional, Set
from typing_extensions import Self

class ParameterFiltersListTemplates(BaseModel):
    """
    ParameterFiltersListTemplates
    """ # noqa: E501
    junction: Optional[Junction] = None
    id: Optional[ParameterFiltersListTemplatesId] = None
    name: Optional[ParameterFiltersListTemplatesName] = None
    campaign_type: Optional[ParameterFiltersListTemplatesCampaignType] = None
    __properties: ClassVar[List[str]] = ["junction", "id", "name", "campaign_type"]

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
        """Create an instance of ParameterFiltersListTemplates from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_type
        if self.campaign_type:
            _dict['campaign_type'] = self.campaign_type.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if campaign_type (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_type is None and "campaign_type" in self.model_fields_set:
            _dict['campaign_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParameterFiltersListTemplates from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "junction": obj.get("junction"),
            "id": ParameterFiltersListTemplatesId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "name": ParameterFiltersListTemplatesName.from_dict(obj["name"]) if obj.get("name") is not None else None,
            "campaign_type": ParameterFiltersListTemplatesCampaignType.from_dict(obj["campaign_type"]) if obj.get("campaign_type") is not None else None
        })
        return _obj


