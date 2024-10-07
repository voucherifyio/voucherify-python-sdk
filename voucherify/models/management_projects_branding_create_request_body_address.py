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

class ManagementProjectsBrandingCreateRequestBodyAddress(BaseModel):
    """
    Defines the address details.
    """ # noqa: E501
    street: Optional[StrictStr] = Field(default=None, description="Defines the brand's street.")
    city: Optional[StrictStr] = Field(default=None, description="Defines the brand's city.")
    postal: Optional[StrictStr] = Field(default=None, description="Defines the brand's postal code.")
    state: Optional[StrictStr] = Field(default=None, description="Defines the brand's state or similar administrative area.")
    country: Optional[StrictStr] = Field(default=None, description="Defines the brand's country.")
    __properties: ClassVar[List[str]] = ["street", "city", "postal", "state", "country"]

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
        """Create an instance of ManagementProjectsBrandingCreateRequestBodyAddress from a JSON string"""
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
        # set to None if street (nullable) is None
        # and model_fields_set contains the field
        if self.street is None and "street" in self.model_fields_set:
            _dict['street'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if postal (nullable) is None
        # and model_fields_set contains the field
        if self.postal is None and "postal" in self.model_fields_set:
            _dict['postal'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagementProjectsBrandingCreateRequestBodyAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "street": obj.get("street"),
            "city": obj.get("city"),
            "postal": obj.get("postal"),
            "state": obj.get("state"),
            "country": obj.get("country")
        })
        return _obj


