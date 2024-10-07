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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.order_calculated import OrderCalculated
from voucherify.models.session import Session
from voucherify.models.stacking_rules import StackingRules
from voucherify.models.validations_redeemable_inapplicable import ValidationsRedeemableInapplicable
from voucherify.models.validations_redeemable_skipped import ValidationsRedeemableSkipped
from voucherify.models.validations_validate_response_body_redeemables_item import ValidationsValidateResponseBodyRedeemablesItem
from typing import Optional, Set
from typing_extensions import Self

class ValidationsValidateResponseBody(BaseModel):
    """
    Response body schema for **POST** `v1/validations`.
    """ # noqa: E501
    valid: Optional[StrictBool] = Field(default=None, description="The result of the validation. It takes all of the redeemables into account and returns a `false` if at least one redeemable is inapplicable. Returns `true` if all redeemables are applicable.")
    redeemables: Optional[List[ValidationsValidateResponseBodyRedeemablesItem]] = None
    skipped_redeemables: Optional[List[ValidationsRedeemableSkipped]] = Field(default=None, description="Lists validation results of each skipped redeemable.")
    inapplicable_redeemables: Optional[List[ValidationsRedeemableInapplicable]] = Field(default=None, description="Lists validation results of each inapplicable redeemable.")
    order: Optional[OrderCalculated] = None
    tracking_id: Optional[StrictStr] = Field(default=None, description="Hashed customer source ID.")
    session: Optional[Session] = None
    stacking_rules: StackingRules
    __properties: ClassVar[List[str]] = ["valid", "redeemables", "skipped_redeemables", "inapplicable_redeemables", "order", "tracking_id", "session", "stacking_rules"]

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
        """Create an instance of ValidationsValidateResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in redeemables (list)
        _items = []
        if self.redeemables:
            for _item_redeemables in self.redeemables:
                if _item_redeemables:
                    _items.append(_item_redeemables.to_dict())
            _dict['redeemables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in skipped_redeemables (list)
        _items = []
        if self.skipped_redeemables:
            for _item_skipped_redeemables in self.skipped_redeemables:
                if _item_skipped_redeemables:
                    _items.append(_item_skipped_redeemables.to_dict())
            _dict['skipped_redeemables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inapplicable_redeemables (list)
        _items = []
        if self.inapplicable_redeemables:
            for _item_inapplicable_redeemables in self.inapplicable_redeemables:
                if _item_inapplicable_redeemables:
                    _items.append(_item_inapplicable_redeemables.to_dict())
            _dict['inapplicable_redeemables'] = _items
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session
        if self.session:
            _dict['session'] = self.session.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stacking_rules
        if self.stacking_rules:
            _dict['stacking_rules'] = self.stacking_rules.to_dict()
        # set to None if valid (nullable) is None
        # and model_fields_set contains the field
        if self.valid is None and "valid" in self.model_fields_set:
            _dict['valid'] = None

        # set to None if redeemables (nullable) is None
        # and model_fields_set contains the field
        if self.redeemables is None and "redeemables" in self.model_fields_set:
            _dict['redeemables'] = None

        # set to None if skipped_redeemables (nullable) is None
        # and model_fields_set contains the field
        if self.skipped_redeemables is None and "skipped_redeemables" in self.model_fields_set:
            _dict['skipped_redeemables'] = None

        # set to None if inapplicable_redeemables (nullable) is None
        # and model_fields_set contains the field
        if self.inapplicable_redeemables is None and "inapplicable_redeemables" in self.model_fields_set:
            _dict['inapplicable_redeemables'] = None

        # set to None if tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_id is None and "tracking_id" in self.model_fields_set:
            _dict['tracking_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidationsValidateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "valid": obj.get("valid"),
            "redeemables": [ValidationsValidateResponseBodyRedeemablesItem.from_dict(_item) for _item in obj["redeemables"]] if obj.get("redeemables") is not None else None,
            "skipped_redeemables": [ValidationsRedeemableSkipped.from_dict(_item) for _item in obj["skipped_redeemables"]] if obj.get("skipped_redeemables") is not None else None,
            "inapplicable_redeemables": [ValidationsRedeemableInapplicable.from_dict(_item) for _item in obj["inapplicable_redeemables"]] if obj.get("inapplicable_redeemables") is not None else None,
            "order": OrderCalculated.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "tracking_id": obj.get("tracking_id"),
            "session": Session.from_dict(obj["session"]) if obj.get("session") is not None else None,
            "stacking_rules": StackingRules.from_dict(obj["stacking_rules"]) if obj.get("stacking_rules") is not None else None
        })
        return _obj


