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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ManagementProjectsUsersInviteCreateRequestBody(BaseModel):
    """
    Request body schema for **POST** `/management/v1/projects/users/invite`.
    """ # noqa: E501
    email: Optional[StrictStr] = Field(default=None, description="Email address to which the invitation will be sent. Must be a valid email address.")
    first_name: Optional[StrictStr] = Field(default=None, description="First name of the person who will receive the invitation. The name will be used in the user profile.")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name of the person who will receive the invitation. The name will be used in the user profile.")
    projects: Optional[Dict[str, Any]] = Field(default=None, description="In the key, provide the project ID to which the new user will be assigned. In the value, provide the role which the user will have in the project. The predefined Voucherify roles are: `ADMIN`, `USER`, `VIEWER`, `MERCHANT`, `USER_RESTRICTED` (for the Areas and Stores, an Enterprise feature). Send a custom role ID (Enterprise feature) to assign a custom role.")
    __properties: ClassVar[List[str]] = ["email", "first_name", "last_name", "projects"]

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
        """Create an instance of ManagementProjectsUsersInviteCreateRequestBody from a JSON string"""
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
        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['first_name'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['last_name'] = None

        # set to None if projects (nullable) is None
        # and model_fields_set contains the field
        if self.projects is None and "projects" in self.model_fields_set:
            _dict['projects'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagementProjectsUsersInviteCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "projects": obj.get("projects")
        })
        return _obj

