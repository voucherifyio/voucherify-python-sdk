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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.loyalties_earning_rules_create_response_body_loyalty_custom_event import LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomEvent
from voucherify.models.loyalties_earning_rules_create_response_body_loyalty_customer import LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomer
from voucherify.models.loyalties_earning_rules_create_response_body_loyalty_order import LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrder
from voucherify.models.loyalties_earning_rules_create_response_body_loyalty_order_items import LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrderItems
from typing import Optional, Set
from typing_extensions import Self

class LoyaltiesEarningRulesCreateResponseBodyLoyalty(BaseModel):
    """
    LoyaltiesEarningRulesCreateResponseBodyLoyalty
    """ # noqa: E501
    type: Optional[StrictStr] = None
    calculation_type: Optional[StrictStr] = None
    order: Optional[LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrder] = None
    order_items: Optional[LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrderItems] = None
    customer: Optional[LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomer] = None
    custom_event: Optional[LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomEvent] = None
    points: Optional[StrictInt] = Field(default=None, description="Defines how the points will be added to the loyalty card. FIXED adds a fixed number of points.")
    __properties: ClassVar[List[str]] = ["type", "calculation_type", "order", "order_items", "customer", "custom_event", "points"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PROPORTIONAL', 'FIXED']):
            raise ValueError("must be one of enum values ('PROPORTIONAL', 'FIXED')")
        return value

    @field_validator('calculation_type')
    def calculation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ORDER_AMOUNT', 'ORDER_TOTAL_AMOUNT', 'ORDER_METADATA', 'ORDER_ITEMS_QUANTITY', 'ORDER_ITEMS_AMOUNT', 'ORDER_ITEMS_SUBTOTAL_AMOUNT', 'CUSTOMER_METADATA', 'CUSTOM_EVENT_METADATA']):
            raise ValueError("must be one of enum values ('ORDER_AMOUNT', 'ORDER_TOTAL_AMOUNT', 'ORDER_METADATA', 'ORDER_ITEMS_QUANTITY', 'ORDER_ITEMS_AMOUNT', 'ORDER_ITEMS_SUBTOTAL_AMOUNT', 'CUSTOMER_METADATA', 'CUSTOM_EVENT_METADATA')")
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
        """Create an instance of LoyaltiesEarningRulesCreateResponseBodyLoyalty from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_items
        if self.order_items:
            _dict['order_items'] = self.order_items.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_event
        if self.custom_event:
            _dict['custom_event'] = self.custom_event.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if calculation_type (nullable) is None
        # and model_fields_set contains the field
        if self.calculation_type is None and "calculation_type" in self.model_fields_set:
            _dict['calculation_type'] = None

        # set to None if order (nullable) is None
        # and model_fields_set contains the field
        if self.order is None and "order" in self.model_fields_set:
            _dict['order'] = None

        # set to None if order_items (nullable) is None
        # and model_fields_set contains the field
        if self.order_items is None and "order_items" in self.model_fields_set:
            _dict['order_items'] = None

        # set to None if customer (nullable) is None
        # and model_fields_set contains the field
        if self.customer is None and "customer" in self.model_fields_set:
            _dict['customer'] = None

        # set to None if custom_event (nullable) is None
        # and model_fields_set contains the field
        if self.custom_event is None and "custom_event" in self.model_fields_set:
            _dict['custom_event'] = None

        # set to None if points (nullable) is None
        # and model_fields_set contains the field
        if self.points is None and "points" in self.model_fields_set:
            _dict['points'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltiesEarningRulesCreateResponseBodyLoyalty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "calculation_type": obj.get("calculation_type"),
            "order": LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrder.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "order_items": LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrderItems.from_dict(obj["order_items"]) if obj.get("order_items") is not None else None,
            "customer": LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomer.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "custom_event": LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomEvent.from_dict(obj["custom_event"]) if obj.get("custom_event") is not None else None,
            "points": obj.get("points")
        })
        return _obj


