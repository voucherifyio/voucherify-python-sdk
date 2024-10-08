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
from voucherify.models.redemption_entry import RedemptionEntry
from typing import Optional, Set
from typing_extensions import Self

class VouchersRedemptionGetResponseBody(BaseModel):
    """
    Response body schema for **GET** `v1/vouchers/{code}/redemption`.
    """ # noqa: E501
    quantity: Optional[StrictInt] = Field(default=None, description="The maximum number of times a voucher can be redeemed.")
    redeemed_quantity: Optional[StrictInt] = Field(default=None, description="The number of times the voucher was redeemed successfully.")
    object: Optional[StrictStr] = Field(default='list', description="The type of the object represented by JSON. This object stores information about redemptions in a dictionary.")
    url: Optional[StrictStr] = Field(default=None, description="URL")
    data_ref: Optional[StrictStr] = Field(default='redemption_entries', description="Identifies the name of the attribute that contains the array of `redemption_entries`.")
    total: Optional[StrictInt] = Field(default=None, description="Total number of redemption objects.")
    redemption_entries: List[RedemptionEntry] = Field(description="Contains the array of successful and failed redemption objects.")
    __properties: ClassVar[List[str]] = ["quantity", "redeemed_quantity", "object", "url", "data_ref", "total", "redemption_entries"]

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
        """Create an instance of VouchersRedemptionGetResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in redemption_entries (list)
        _items = []
        if self.redemption_entries:
            for _item_redemption_entries in self.redemption_entries:
                if _item_redemption_entries:
                    _items.append(_item_redemption_entries.to_dict())
            _dict['redemption_entries'] = _items
        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if redeemed_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.redeemed_quantity is None and "redeemed_quantity" in self.model_fields_set:
            _dict['redeemed_quantity'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if data_ref (nullable) is None
        # and model_fields_set contains the field
        if self.data_ref is None and "data_ref" in self.model_fields_set:
            _dict['data_ref'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VouchersRedemptionGetResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantity": obj.get("quantity"),
            "redeemed_quantity": obj.get("redeemed_quantity"),
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "url": obj.get("url"),
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'redemption_entries',
            "total": obj.get("total"),
            "redemption_entries": [RedemptionEntry.from_dict(_item) for _item in obj["redemption_entries"]] if obj.get("redemption_entries") is not None else None
        })
        return _obj


