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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.promotion_tier import PromotionTier
from typing import Optional, Set
from typing_extensions import Self

class ClientPromotionsTiersListResponseBody(BaseModel):
    """
    Response body schema for **GET** `v1/client/v1/promotions/tiers`.
    """ # noqa: E501
    object: Optional[StrictStr] = Field(default='list', description="The type of the object represented by JSON. This object stores information about promotion tiers in a dictionary.")
    data_ref: Optional[StrictStr] = Field(default='tiers', description="Identifies the name of the attribute that contains the array of promotion tier objects.")
    tiers: Optional[List[PromotionTier]] = Field(default=None, description="Contains array of promotion tier objects.")
    total: Optional[StrictInt] = Field(default=None, description="Total number of promotion tiers.")
    has_more: Optional[StrictBool] = Field(default=None, description="As query results are always limited (by the limit parameter), the `has_more` flag indicates if there are more records for given filter parameters. This lets you know if you can run another request to get more records returned in the results.")
    __properties: ClassVar[List[str]] = ["object", "data_ref", "tiers", "total", "has_more"]

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
        """Create an instance of ClientPromotionsTiersListResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tiers (list)
        _items = []
        if self.tiers:
            for _item_tiers in self.tiers:
                if _item_tiers:
                    _items.append(_item_tiers.to_dict())
            _dict['tiers'] = _items
        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if data_ref (nullable) is None
        # and model_fields_set contains the field
        if self.data_ref is None and "data_ref" in self.model_fields_set:
            _dict['data_ref'] = None

        # set to None if tiers (nullable) is None
        # and model_fields_set contains the field
        if self.tiers is None and "tiers" in self.model_fields_set:
            _dict['tiers'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if has_more (nullable) is None
        # and model_fields_set contains the field
        if self.has_more is None and "has_more" in self.model_fields_set:
            _dict['has_more'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientPromotionsTiersListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'tiers',
            "tiers": [PromotionTier.from_dict(_item) for _item in obj["tiers"]] if obj.get("tiers") is not None else None,
            "total": obj.get("total"),
            "has_more": obj.get("has_more")
        })
        return _obj


