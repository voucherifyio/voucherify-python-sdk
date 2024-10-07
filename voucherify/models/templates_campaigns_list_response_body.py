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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.campaign_template import CampaignTemplate
from typing import Optional, Set
from typing_extensions import Self

class TemplatesCampaignsListResponseBody(BaseModel):
    """
    Response body schema for **GET** `/v1/templates/campaign`.
    """ # noqa: E501
    object: Optional[StrictStr] = Field(default='list', description="The type of the object represented by JSON. This object stores information about campaign templates.")
    data_ref: Optional[StrictStr] = Field(default='data', description="Identifies the name of the JSON property that contains the array of campaign templates.")
    data: Optional[List[CampaignTemplate]] = Field(default=None, description="Dictionary that contains an array of campaign templates.")
    total: Optional[StrictInt] = Field(default=None, description="Total number of templates, regardless of the applied query parameters. Displayed only if the `include_total` query paremeter is set to `true`.")
    has_more: Optional[StrictBool] = Field(default=None, description="As query results are always limited (by the limit parameter), the `has_more` flag indicates if there are more records for given filter parameters. This lets you know if you can run another request to get more records returned in the results.")
    more_starting_after: Optional[StrictStr] = Field(default=None, description="Returns an ID that can be used to return another page of results. Use the template ID in the `starting_after_id` query parameter to display another page of the results starting after the template with that ID.")
    __properties: ClassVar[List[str]] = ["object", "data_ref", "data", "total", "has_more", "more_starting_after"]

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
        """Create an instance of TemplatesCampaignsListResponseBody from a JSON string"""
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
        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if data_ref (nullable) is None
        # and model_fields_set contains the field
        if self.data_ref is None and "data_ref" in self.model_fields_set:
            _dict['data_ref'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if has_more (nullable) is None
        # and model_fields_set contains the field
        if self.has_more is None and "has_more" in self.model_fields_set:
            _dict['has_more'] = None

        # set to None if more_starting_after (nullable) is None
        # and model_fields_set contains the field
        if self.more_starting_after is None and "more_starting_after" in self.model_fields_set:
            _dict['more_starting_after'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TemplatesCampaignsListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'data',
            "data": [CampaignTemplate.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "total": obj.get("total"),
            "has_more": obj.get("has_more"),
            "more_starting_after": obj.get("more_starting_after")
        })
        return _obj


