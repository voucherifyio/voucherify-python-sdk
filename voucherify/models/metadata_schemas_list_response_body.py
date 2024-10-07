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
from voucherify.models.metadata_schema_deprecated import MetadataSchemaDeprecated
from typing import Optional, Set
from typing_extensions import Self

class MetadataSchemasListResponseBody(BaseModel):
    """
    Object containing a list of metadata schemas.
    """ # noqa: E501
    object: Optional[StrictStr] = Field(default='list', description="The type of the object represented by JSON. This object stores information about the metadata schemas in a dictionary.")
    data_ref: Optional[StrictStr] = Field(default='schemas', description="Identifies the name of the attribute that contains the array of metadata schema objects.")
    schemas: Optional[List[MetadataSchemaDeprecated]] = Field(default=None, description="Array of metadata schema objects. The metadata schemas are listed by related object properties.")
    total: Optional[StrictInt] = Field(default=None, description="The total number of metadata schema objects.")
    __properties: ClassVar[List[str]] = ["object", "data_ref", "schemas", "total"]

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

        if value not in set(['schemas']):
            raise ValueError("must be one of enum values ('schemas')")
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
        """Create an instance of MetadataSchemasListResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in schemas (list)
        _items = []
        if self.schemas:
            for _item_schemas in self.schemas:
                if _item_schemas:
                    _items.append(_item_schemas.to_dict())
            _dict['schemas'] = _items
        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if data_ref (nullable) is None
        # and model_fields_set contains the field
        if self.data_ref is None and "data_ref" in self.model_fields_set:
            _dict['data_ref'] = None

        # set to None if schemas (nullable) is None
        # and model_fields_set contains the field
        if self.schemas is None and "schemas" in self.model_fields_set:
            _dict['schemas'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetadataSchemasListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'schemas',
            "schemas": [MetadataSchemaDeprecated.from_dict(_item) for _item in obj["schemas"]] if obj.get("schemas") is not None else None,
            "total": obj.get("total")
        })
        return _obj


