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
from voucherify.models.order_calculated import OrderCalculated
from voucherify.models.redemption import Redemption
from voucherify.models.validations_redeemable_inapplicable import ValidationsRedeemableInapplicable
from voucherify.models.validations_redeemable_skipped import ValidationsRedeemableSkipped
from typing import Optional, Set
from typing_extensions import Self

class RedemptionsRedeemResponseBody(BaseModel):
    """
    Response body schema for **POST** `v1/redemptions`.
    """ # noqa: E501
    redemptions: Optional[List[Redemption]] = None
    parent_redemption: Optional[Redemption] = None
    order: Optional[OrderCalculated] = None
    inapplicable_redeemables: Optional[List[ValidationsRedeemableInapplicable]] = Field(default=None, description="Lists validation results of each inapplicable redeemable.")
    skipped_redeemables: Optional[List[ValidationsRedeemableSkipped]] = Field(default=None, description="Lists validation results of each redeemable. If a redeemable can be applied, the API returns `\"status\": \"APPLICABLE\"`.")
    __properties: ClassVar[List[str]] = ["redemptions", "parent_redemption", "order", "inapplicable_redeemables", "skipped_redeemables"]

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
        """Create an instance of RedemptionsRedeemResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in redemptions (list)
        _items = []
        if self.redemptions:
            for _item_redemptions in self.redemptions:
                if _item_redemptions:
                    _items.append(_item_redemptions.to_dict())
            _dict['redemptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of parent_redemption
        if self.parent_redemption:
            _dict['parent_redemption'] = self.parent_redemption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in inapplicable_redeemables (list)
        _items = []
        if self.inapplicable_redeemables:
            for _item_inapplicable_redeemables in self.inapplicable_redeemables:
                if _item_inapplicable_redeemables:
                    _items.append(_item_inapplicable_redeemables.to_dict())
            _dict['inapplicable_redeemables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in skipped_redeemables (list)
        _items = []
        if self.skipped_redeemables:
            for _item_skipped_redeemables in self.skipped_redeemables:
                if _item_skipped_redeemables:
                    _items.append(_item_skipped_redeemables.to_dict())
            _dict['skipped_redeemables'] = _items
        # set to None if redemptions (nullable) is None
        # and model_fields_set contains the field
        if self.redemptions is None and "redemptions" in self.model_fields_set:
            _dict['redemptions'] = None

        # set to None if inapplicable_redeemables (nullable) is None
        # and model_fields_set contains the field
        if self.inapplicable_redeemables is None and "inapplicable_redeemables" in self.model_fields_set:
            _dict['inapplicable_redeemables'] = None

        # set to None if skipped_redeemables (nullable) is None
        # and model_fields_set contains the field
        if self.skipped_redeemables is None and "skipped_redeemables" in self.model_fields_set:
            _dict['skipped_redeemables'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RedemptionsRedeemResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "redemptions": [Redemption.from_dict(_item) for _item in obj["redemptions"]] if obj.get("redemptions") is not None else None,
            "parent_redemption": Redemption.from_dict(obj["parent_redemption"]) if obj.get("parent_redemption") is not None else None,
            "order": OrderCalculated.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "inapplicable_redeemables": [ValidationsRedeemableInapplicable.from_dict(_item) for _item in obj["inapplicable_redeemables"]] if obj.get("inapplicable_redeemables") is not None else None,
            "skipped_redeemables": [ValidationsRedeemableSkipped.from_dict(_item) for _item in obj["skipped_redeemables"]] if obj.get("skipped_redeemables") is not None else None
        })
        return _obj


