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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.management_projects_custom_event_schemas_update_request_body_schema import ManagementProjectsCustomEventSchemasUpdateRequestBodySchema
from typing import Optional, Set
from typing_extensions import Self

class ManagementProjectsCustomEventSchemasUpdateRequestBody(BaseModel):
    """
    Request body schema for **POST** `/management/v1/projects/{projectId}/custom-event-schema/{customEventSchemaId}`.
    """ # noqa: E501
    var_schema: Optional[ManagementProjectsCustomEventSchemasUpdateRequestBodySchema] = Field(default=None, alias="schema")
    __properties: ClassVar[List[str]] = ["schema"]

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
        """Create an instance of ManagementProjectsCustomEventSchemasUpdateRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # set to None if var_schema (nullable) is None
        # and model_fields_set contains the field
        if self.var_schema is None and "var_schema" in self.model_fields_set:
            _dict['schema'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagementProjectsCustomEventSchemasUpdateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "schema": ManagementProjectsCustomEventSchemasUpdateRequestBodySchema.from_dict(obj["schema"]) if obj.get("schema") is not None else None
        })
        return _obj


