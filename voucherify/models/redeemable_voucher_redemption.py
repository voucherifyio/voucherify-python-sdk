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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RedeemableVoucherRedemption(BaseModel):
    """
    Stores a summary of redemptions that have been applied to the voucher.
    """ # noqa: E501
    quantity: Optional[StrictInt] = Field(default=None, description="How many times a voucher can be redeemed. A `null` value means unlimited.")
    redeemed_quantity: Optional[StrictInt] = Field(default=None, description="How many times a voucher has already been redeemed.")
    redeemed_points: Optional[StrictInt] = Field(default=None, description="Total loyalty points redeemed.")
    object: Optional[StrictStr] = Field(default='list', description="The type of the object represented is by default `list`. To get this list, you need to make a call to the endpoint returned in the url attribute.")
    url: Optional[StrictStr] = Field(default=None, description="The endpoint where this list of redemptions can be accessed using a **GET** method. `/v1/vouchers/{voucher_code}/redemptions`")
    __properties: ClassVar[List[str]] = ["quantity", "redeemed_quantity", "redeemed_points", "object", "url"]

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
        """Create an instance of RedeemableVoucherRedemption from a JSON string"""
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
        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if redeemed_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.redeemed_quantity is None and "redeemed_quantity" in self.model_fields_set:
            _dict['redeemed_quantity'] = None

        # set to None if redeemed_points (nullable) is None
        # and model_fields_set contains the field
        if self.redeemed_points is None and "redeemed_points" in self.model_fields_set:
            _dict['redeemed_points'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RedeemableVoucherRedemption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantity": obj.get("quantity"),
            "redeemed_quantity": obj.get("redeemed_quantity"),
            "redeemed_points": obj.get("redeemed_points"),
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "url": obj.get("url")
        })
        return _obj


