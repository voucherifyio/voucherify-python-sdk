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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.loyalties_earning_rules_create_request_body_item_loyalty_order_items_amount import LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsAmount
from voucherify.models.loyalties_earning_rules_create_request_body_item_loyalty_order_items_quantity import LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsQuantity
from voucherify.models.loyalties_earning_rules_create_request_body_item_loyalty_order_items_subtotal_amount import LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsSubtotalAmount
from typing import Optional, Set
from typing_extensions import Self

class LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItems(BaseModel):
    """
    LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItems
    """ # noqa: E501
    quantity: Optional[LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsQuantity] = None
    amount: Optional[LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsAmount] = None
    subtotal_amount: Optional[LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsSubtotalAmount] = None
    __properties: ClassVar[List[str]] = ["quantity", "amount", "subtotal_amount"]

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
        """Create an instance of LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItems from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of quantity
        if self.quantity:
            _dict['quantity'] = self.quantity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subtotal_amount
        if self.subtotal_amount:
            _dict['subtotal_amount'] = self.subtotal_amount.to_dict()
        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if amount (nullable) is None
        # and model_fields_set contains the field
        if self.amount is None and "amount" in self.model_fields_set:
            _dict['amount'] = None

        # set to None if subtotal_amount (nullable) is None
        # and model_fields_set contains the field
        if self.subtotal_amount is None and "subtotal_amount" in self.model_fields_set:
            _dict['subtotal_amount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItems from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantity": LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsQuantity.from_dict(obj["quantity"]) if obj.get("quantity") is not None else None,
            "amount": LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsAmount.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "subtotal_amount": LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsSubtotalAmount.from_dict(obj["subtotal_amount"]) if obj.get("subtotal_amount") is not None else None
        })
        return _obj


