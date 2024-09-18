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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.customers_permanent_deletion_create_response_body_data_json import CustomersPermanentDeletionCreateResponseBodyDataJson
from typing import Optional, Set
from typing_extensions import Self

class CustomersPermanentDeletionCreateResponseBody(BaseModel):
    """
    Response body schema for **POST** `v1/customers/{customerId}/permanent-deletion`.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique permanent deletion object ID.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the customer was requested to be deleted in ISO 8601 format.")
    related_object_id: Optional[StrictStr] = Field(default=None, description="Unique customer ID that is being deleted.")
    related_object: Optional[StrictStr] = Field(default='customer', description="Object being deleted.")
    status: Optional[StrictStr] = Field(default='DONE', description="Deletion status.")
    data_json: Optional[CustomersPermanentDeletionCreateResponseBodyDataJson] = None
    object: Optional[StrictStr] = Field(default='pernament_deletion', description="The type of the object represented by JSON.")
    __properties: ClassVar[List[str]] = ["id", "created_at", "related_object_id", "related_object", "status", "data_json", "object"]

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
        """Create an instance of CustomersPermanentDeletionCreateResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data_json
        if self.data_json:
            _dict['data_json'] = self.data_json.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if related_object_id (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_id is None and "related_object_id" in self.model_fields_set:
            _dict['related_object_id'] = None

        # set to None if related_object (nullable) is None
        # and model_fields_set contains the field
        if self.related_object is None and "related_object" in self.model_fields_set:
            _dict['related_object'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if data_json (nullable) is None
        # and model_fields_set contains the field
        if self.data_json is None and "data_json" in self.model_fields_set:
            _dict['data_json'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomersPermanentDeletionCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "related_object_id": obj.get("related_object_id"),
            "related_object": obj.get("related_object") if obj.get("related_object") is not None else 'customer',
            "status": obj.get("status") if obj.get("status") is not None else 'DONE',
            "data_json": CustomersPermanentDeletionCreateResponseBodyDataJson.from_dict(obj["data_json"]) if obj.get("data_json") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'pernament_deletion'
        })
        return _obj


