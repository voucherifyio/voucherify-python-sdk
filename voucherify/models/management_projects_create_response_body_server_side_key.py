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

class ManagementProjectsCreateResponseBodyServerSideKey(BaseModel):
    """
    Contains the `app_id` and `app_token` to authenticate server-side requests.
    """ # noqa: E501
    app_id: Optional[StrictStr] = Field(default=None, description="Application ID to be used as `X-App-Id` header in every HTTP request.")
    app_token: Optional[StrictStr] = Field(default=None, description="Application token to be used as `X-App-Token` header in every HTTP request.  The application token (secret key) for the server-side authentication is visible in the Project Settings for 14 days when it is first generated in a newly-created project. Write your application token down and keep it in a safe place.")
    __properties: ClassVar[List[str]] = ["app_id", "app_token"]

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
        """Create an instance of ManagementProjectsCreateResponseBodyServerSideKey from a JSON string"""
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
        # set to None if app_id (nullable) is None
        # and model_fields_set contains the field
        if self.app_id is None and "app_id" in self.model_fields_set:
            _dict['app_id'] = None

        # set to None if app_token (nullable) is None
        # and model_fields_set contains the field
        if self.app_token is None and "app_token" in self.model_fields_set:
            _dict['app_token'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagementProjectsCreateResponseBodyServerSideKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_id": obj.get("app_id"),
            "app_token": obj.get("app_token")
        })
        return _obj


