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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ManagementProjectsMetadataSchema(BaseModel):
    """
    Object representing a metadata schema.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the metadata schema.")
    related_object: Optional[StrictStr] = Field(default=None, description="The resource type. You can define custom metadata schemas, which have a custom `\"related_object\"` resource type. The standard metadata schemas are: `\"campaign\"`, `\"customer\"`, `\"earning_rule\"`, `\"loyalty_tier\"`, `\"order\"`, `\"order_item\"`, `\"product\"`, `\"promotion_tier\"`, `\"publication\"`, `\"redemption\"`, `\"reward\"`, `\"voucher\"`.")
    properties: Optional[Dict[str, Any]] = Field(default=None, description="Contains metadata definitions.")
    allow_defined_only: Optional[StrictBool] = Field(default=None, description="Restricts the creation of metadata fields when set to `true`. It indicates whether or not you can create new metadata definitions, e.g. in the campaign or publication manager. If set to `true`, then only the defined fields are available for assigning values.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the metadata schema was created. The value for this parameter is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the metadata schema was updated. The value for this parameter is shown in the ISO 8601 format.")
    object: Optional[StrictStr] = Field(default='metadata_schema', description="The type of the object represented by the JSON. This object stores information about the metadata schema.")
    __properties: ClassVar[List[str]] = ["id", "related_object", "properties", "allow_defined_only", "created_at", "updated_at", "object"]

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
        """Create an instance of ManagementProjectsMetadataSchema from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if related_object (nullable) is None
        # and model_fields_set contains the field
        if self.related_object is None and "related_object" in self.model_fields_set:
            _dict['related_object'] = None

        # set to None if properties (nullable) is None
        # and model_fields_set contains the field
        if self.properties is None and "properties" in self.model_fields_set:
            _dict['properties'] = None

        # set to None if allow_defined_only (nullable) is None
        # and model_fields_set contains the field
        if self.allow_defined_only is None and "allow_defined_only" in self.model_fields_set:
            _dict['allow_defined_only'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagementProjectsMetadataSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "related_object": obj.get("related_object"),
            "properties": obj.get("properties"),
            "allow_defined_only": obj.get("allow_defined_only"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "object": obj.get("object") if obj.get("object") is not None else 'metadata_schema'
        })
        return _obj


