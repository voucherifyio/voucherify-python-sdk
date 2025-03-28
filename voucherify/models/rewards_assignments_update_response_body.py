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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.rewards_assignments_update_response_body_parameters import RewardsAssignmentsUpdateResponseBodyParameters
from typing import Optional, Set
from typing_extensions import Self

class RewardsAssignmentsUpdateResponseBody(BaseModel):
    """
    Response body schema for **PUT** `v1/rewards/{rewardId}/assignments/{assignmentId}`.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique reward assignment ID, assigned by Voucherify.")
    reward_id: Optional[StrictStr] = Field(default=None, description="Associated reward ID.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the reward assignment was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the reward assignment was updated. The value is shown in the ISO 8601 format.")
    object: Optional[StrictStr] = Field(default='reward_assignment', description="The type of the object represented by the JSON. This object stores information about the reward assignment.")
    related_object_id: Optional[StrictStr] = Field(default=None, description="Related object ID to which the reward was assigned.")
    related_object_type: Optional[StrictStr] = Field(default='campaign', description="Related object type to which the reward was assigned.")
    parameters: Optional[RewardsAssignmentsUpdateResponseBodyParameters] = None
    __properties: ClassVar[List[str]] = ["id", "reward_id", "created_at", "updated_at", "object", "related_object_id", "related_object_type", "parameters"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['reward_assignment']):
            raise ValueError("must be one of enum values ('reward_assignment')")
        return value

    @field_validator('related_object_type')
    def related_object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['campaign']):
            raise ValueError("must be one of enum values ('campaign')")
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
        """Create an instance of RewardsAssignmentsUpdateResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if reward_id (nullable) is None
        # and model_fields_set contains the field
        if self.reward_id is None and "reward_id" in self.model_fields_set:
            _dict['reward_id'] = None

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

        # set to None if related_object_id (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_id is None and "related_object_id" in self.model_fields_set:
            _dict['related_object_id'] = None

        # set to None if related_object_type (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_type is None and "related_object_type" in self.model_fields_set:
            _dict['related_object_type'] = None

        # set to None if parameters (nullable) is None
        # and model_fields_set contains the field
        if self.parameters is None and "parameters" in self.model_fields_set:
            _dict['parameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RewardsAssignmentsUpdateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "reward_id": obj.get("reward_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "object": obj.get("object") if obj.get("object") is not None else 'reward_assignment',
            "related_object_id": obj.get("related_object_id"),
            "related_object_type": obj.get("related_object_type") if obj.get("related_object_type") is not None else 'campaign',
            "parameters": RewardsAssignmentsUpdateResponseBodyParameters.from_dict(obj["parameters"]) if obj.get("parameters") is not None else None
        })
        return _obj


