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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.customer_id import CustomerId
from voucherify.models.order_calculated_item import OrderCalculatedItem
from voucherify.models.referrer_id import ReferrerId
from typing import Optional, Set
from typing_extensions import Self

class OrdersUpdateResponseBody(BaseModel):
    """
    Response body schema for **PUT** `v1/orders/{orderId}`.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique ID assigned by Voucherify of an existing order that will be linked to the redemption of this request.")
    source_id: Optional[StrictStr] = Field(default=None, description="Unique source ID of an existing order that will be linked to the redemption of this request.")
    status: Optional[StrictStr] = Field(default=None, description="The order status.")
    amount: Optional[StrictInt] = Field(default=None, description="A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items' amounts.")
    initial_amount: Optional[StrictInt] = Field(default=None, description="A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items' amounts.")
    discount_amount: Optional[StrictInt] = Field(default=None, description="Sum of all order-level discounts applied to the order.")
    items_discount_amount: Optional[StrictInt] = Field(default=None, description="Sum of all product-specific discounts applied to the order.")
    total_discount_amount: Optional[StrictInt] = Field(default=None, description="Sum of all order-level AND all product-specific discounts applied to the order.")
    total_amount: Optional[StrictInt] = Field(default=None, description="Order amount after undoing all the discounts through the rollback redemption.")
    applied_discount_amount: Optional[StrictInt] = Field(default=None, description="This field shows the order-level discount applied.")
    items_applied_discount_amount: Optional[StrictInt] = Field(default=None, description="Sum of all product-specific discounts applied in a particular request.   `sum(items, i => i.applied_discount_amount)`")
    total_applied_discount_amount: Optional[StrictInt] = Field(default=None, description="Sum of all order-level AND all product-specific discounts applied in a particular request.   `total_applied_discount_amount` = `applied_discount_amount` + `items_applied_discount_amount`")
    items: Optional[List[OrderCalculatedItem]] = Field(default=None, description="Array of items applied to the order. It can include up 500 items.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="A set of custom key/value pairs that you can attach to an order. It can be useful for storing additional information about the order in a structured format. It can be used to define business validation rules or discount formulas.")
    object: Optional[StrictStr] = Field(default='order', description="The type of the object represented by JSON.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the order was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the order was last updated in ISO 8601 format.")
    customer_id: Optional[StrictStr] = Field(default=None, description="Unique customer ID of the customer making the purchase.")
    referrer_id: Optional[StrictStr] = Field(default=None, description="Unique referrer ID.")
    customer: Optional[CustomerId] = None
    referrer: Optional[ReferrerId] = None
    redemptions: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["id", "source_id", "status", "amount", "initial_amount", "discount_amount", "items_discount_amount", "total_discount_amount", "total_amount", "applied_discount_amount", "items_applied_discount_amount", "total_applied_discount_amount", "items", "metadata", "object", "created_at", "updated_at", "customer_id", "referrer_id", "customer", "referrer", "redemptions"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['CREATED', 'PAID', 'CANCELED', 'FULFILLED']):
            raise ValueError("must be one of enum values ('CREATED', 'PAID', 'CANCELED', 'FULFILLED')")
        return value

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['order']):
            raise ValueError("must be one of enum values ('order')")
        return value

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
        """Create an instance of OrdersUpdateResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of referrer
        if self.referrer:
            _dict['referrer'] = self.referrer.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['source_id'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if amount (nullable) is None
        # and model_fields_set contains the field
        if self.amount is None and "amount" in self.model_fields_set:
            _dict['amount'] = None

        # set to None if initial_amount (nullable) is None
        # and model_fields_set contains the field
        if self.initial_amount is None and "initial_amount" in self.model_fields_set:
            _dict['initial_amount'] = None

        # set to None if discount_amount (nullable) is None
        # and model_fields_set contains the field
        if self.discount_amount is None and "discount_amount" in self.model_fields_set:
            _dict['discount_amount'] = None

        # set to None if items_discount_amount (nullable) is None
        # and model_fields_set contains the field
        if self.items_discount_amount is None and "items_discount_amount" in self.model_fields_set:
            _dict['items_discount_amount'] = None

        # set to None if total_discount_amount (nullable) is None
        # and model_fields_set contains the field
        if self.total_discount_amount is None and "total_discount_amount" in self.model_fields_set:
            _dict['total_discount_amount'] = None

        # set to None if total_amount (nullable) is None
        # and model_fields_set contains the field
        if self.total_amount is None and "total_amount" in self.model_fields_set:
            _dict['total_amount'] = None

        # set to None if applied_discount_amount (nullable) is None
        # and model_fields_set contains the field
        if self.applied_discount_amount is None and "applied_discount_amount" in self.model_fields_set:
            _dict['applied_discount_amount'] = None

        # set to None if items_applied_discount_amount (nullable) is None
        # and model_fields_set contains the field
        if self.items_applied_discount_amount is None and "items_applied_discount_amount" in self.model_fields_set:
            _dict['items_applied_discount_amount'] = None

        # set to None if total_applied_discount_amount (nullable) is None
        # and model_fields_set contains the field
        if self.total_applied_discount_amount is None and "total_applied_discount_amount" in self.model_fields_set:
            _dict['total_applied_discount_amount'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customer_id'] = None

        # set to None if referrer_id (nullable) is None
        # and model_fields_set contains the field
        if self.referrer_id is None and "referrer_id" in self.model_fields_set:
            _dict['referrer_id'] = None

        # set to None if redemptions (nullable) is None
        # and model_fields_set contains the field
        if self.redemptions is None and "redemptions" in self.model_fields_set:
            _dict['redemptions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrdersUpdateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "status": obj.get("status"),
            "amount": obj.get("amount"),
            "initial_amount": obj.get("initial_amount"),
            "discount_amount": obj.get("discount_amount"),
            "items_discount_amount": obj.get("items_discount_amount"),
            "total_discount_amount": obj.get("total_discount_amount"),
            "total_amount": obj.get("total_amount"),
            "applied_discount_amount": obj.get("applied_discount_amount"),
            "items_applied_discount_amount": obj.get("items_applied_discount_amount"),
            "total_applied_discount_amount": obj.get("total_applied_discount_amount"),
            "items": [OrderCalculatedItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "metadata": obj.get("metadata"),
            "object": obj.get("object") if obj.get("object") is not None else 'order',
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "customer_id": obj.get("customer_id"),
            "referrer_id": obj.get("referrer_id"),
            "customer": CustomerId.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "referrer": ReferrerId.from_dict(obj["referrer"]) if obj.get("referrer") is not None else None,
            "redemptions": obj.get("redemptions")
        })
        return _obj


