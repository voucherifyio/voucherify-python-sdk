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

class ManagementProjectsBrandingCreateResponseBodyBrand(BaseModel):
    """
    Defines basic brand details.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Defines brand name.")
    privacy_policy_url: Optional[StrictStr] = Field(default=None, description="Defines the URL to the brand's privacy policy. It must be a valid URL format.")
    terms_of_use_url: Optional[StrictStr] = Field(default=None, description="Defines the URL to the brand's terms of use.  It must be a valid URL format.")
    permission_reminder: Optional[StrictStr] = Field(default=None, description="Defines the message that is displayed to customers who opted in an email newsletter.")
    website_url: Optional[StrictStr] = Field(default=None, description="Defines the URL to the brand's website. It must be a valid URL format.")
    __properties: ClassVar[List[str]] = ["name", "privacy_policy_url", "terms_of_use_url", "permission_reminder", "website_url"]

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
        """Create an instance of ManagementProjectsBrandingCreateResponseBodyBrand from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if privacy_policy_url (nullable) is None
        # and model_fields_set contains the field
        if self.privacy_policy_url is None and "privacy_policy_url" in self.model_fields_set:
            _dict['privacy_policy_url'] = None

        # set to None if terms_of_use_url (nullable) is None
        # and model_fields_set contains the field
        if self.terms_of_use_url is None and "terms_of_use_url" in self.model_fields_set:
            _dict['terms_of_use_url'] = None

        # set to None if permission_reminder (nullable) is None
        # and model_fields_set contains the field
        if self.permission_reminder is None and "permission_reminder" in self.model_fields_set:
            _dict['permission_reminder'] = None

        # set to None if website_url (nullable) is None
        # and model_fields_set contains the field
        if self.website_url is None and "website_url" in self.model_fields_set:
            _dict['website_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagementProjectsBrandingCreateResponseBodyBrand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "privacy_policy_url": obj.get("privacy_policy_url"),
            "terms_of_use_url": obj.get("terms_of_use_url"),
            "permission_reminder": obj.get("permission_reminder"),
            "website_url": obj.get("website_url")
        })
        return _obj


