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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from voucherify.models.discount_unit_multiple_one_unit import DiscountUnitMultipleOneUnit
from voucherify.models.simple_sku_discount_unit import SimpleSkuDiscountUnit
from voucherify.models.validations_validate_response_body_redeemables_item_result_discount_product import ValidationsValidateResponseBodyRedeemablesItemResultDiscountProduct
from typing import Optional, Set
from typing_extensions import Self

class ValidationsValidateResponseBodyRedeemablesItemResultDiscount(BaseModel):
    """
    ValidationsValidateResponseBodyRedeemablesItemResultDiscount
    """ # noqa: E501
    type: Optional[StrictStr] = None
    amount_off: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount taken off the subtotal of a price. Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $10 discount is written as 1000.")
    amount_off_formula: Optional[StrictStr] = None
    aggregated_amount_limit: Optional[StrictInt] = Field(default=None, description="Maximum discount amount per order.")
    effect: Optional[StrictStr] = None
    is_dynamic: Optional[StrictBool] = Field(default=None, description="Flag indicating whether the discount was calculated using a formula.")
    unit_off: Optional[StrictInt] = Field(default=None, description="Number of units to be granted a full value discount.")
    unit_off_formula: Optional[StrictStr] = Field(default=None, description="Formula used to calculate the number of units.")
    unit_type: Optional[StrictStr] = Field(default=None, description="The product deemed as free, chosen from product inventory (e.g. time, items).")
    product: Optional[ValidationsValidateResponseBodyRedeemablesItemResultDiscountProduct] = None
    sku: Optional[SimpleSkuDiscountUnit] = None
    units: Optional[List[DiscountUnitMultipleOneUnit]] = None
    percent_off: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The percent discount that the customer will receive.")
    percent_off_formula: Optional[StrictStr] = None
    amount_limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Upper limit allowed to be applied as a discount. Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $6 maximum discount is written as 600.")
    fixed_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sets a fixed value for an order total or the item price. The value is multiplied by 100 to precisely represent 2 decimal places. For example, a $10 discount is written as 1000. If the fixed amount is calculated by the formula, i.e. the `fixed_amount_formula` parameter is present in the fixed amount definition, this value becomes the **fallback value**. As a result, if the formula cannot be calculated due to missing metadata, for example, this value will be used as the fixed value.")
    fixed_amount_formula: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["type", "amount_off", "amount_off_formula", "aggregated_amount_limit", "effect", "is_dynamic", "unit_off", "unit_off_formula", "unit_type", "product", "sku", "units", "percent_off", "percent_off_formula", "amount_limit", "fixed_amount", "fixed_amount_formula"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AMOUNT', 'UNIT', 'PERCENT', 'FIXED']):
            raise ValueError("must be one of enum values ('AMOUNT', 'UNIT', 'PERCENT', 'FIXED')")
        return value

    @field_validator('effect')
    def effect_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['APPLY_TO_ORDER', 'APPLY_TO_ITEMS', 'APPLY_TO_ITEMS_PROPORTIONALLY', 'APPLY_TO_ITEMS_PROPORTIONALLY_BY_QUANTITY', 'APPLY_TO_ITEMS_BY_QUANTITY', 'ADD_MISSING_ITEMS', 'ADD_NEW_ITEMS', 'ADD_MANY_ITEMS']):
            raise ValueError("must be one of enum values ('APPLY_TO_ORDER', 'APPLY_TO_ITEMS', 'APPLY_TO_ITEMS_PROPORTIONALLY', 'APPLY_TO_ITEMS_PROPORTIONALLY_BY_QUANTITY', 'APPLY_TO_ITEMS_BY_QUANTITY', 'ADD_MISSING_ITEMS', 'ADD_NEW_ITEMS', 'ADD_MANY_ITEMS')")
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
        """Create an instance of ValidationsValidateResponseBodyRedeemablesItemResultDiscount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sku
        if self.sku:
            _dict['sku'] = self.sku.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in units (list)
        _items = []
        if self.units:
            for _item_units in self.units:
                if _item_units:
                    _items.append(_item_units.to_dict())
            _dict['units'] = _items
        # set to None if amount_off (nullable) is None
        # and model_fields_set contains the field
        if self.amount_off is None and "amount_off" in self.model_fields_set:
            _dict['amount_off'] = None

        # set to None if amount_off_formula (nullable) is None
        # and model_fields_set contains the field
        if self.amount_off_formula is None and "amount_off_formula" in self.model_fields_set:
            _dict['amount_off_formula'] = None

        # set to None if aggregated_amount_limit (nullable) is None
        # and model_fields_set contains the field
        if self.aggregated_amount_limit is None and "aggregated_amount_limit" in self.model_fields_set:
            _dict['aggregated_amount_limit'] = None

        # set to None if is_dynamic (nullable) is None
        # and model_fields_set contains the field
        if self.is_dynamic is None and "is_dynamic" in self.model_fields_set:
            _dict['is_dynamic'] = None

        # set to None if unit_off (nullable) is None
        # and model_fields_set contains the field
        if self.unit_off is None and "unit_off" in self.model_fields_set:
            _dict['unit_off'] = None

        # set to None if unit_off_formula (nullable) is None
        # and model_fields_set contains the field
        if self.unit_off_formula is None and "unit_off_formula" in self.model_fields_set:
            _dict['unit_off_formula'] = None

        # set to None if unit_type (nullable) is None
        # and model_fields_set contains the field
        if self.unit_type is None and "unit_type" in self.model_fields_set:
            _dict['unit_type'] = None

        # set to None if units (nullable) is None
        # and model_fields_set contains the field
        if self.units is None and "units" in self.model_fields_set:
            _dict['units'] = None

        # set to None if percent_off (nullable) is None
        # and model_fields_set contains the field
        if self.percent_off is None and "percent_off" in self.model_fields_set:
            _dict['percent_off'] = None

        # set to None if percent_off_formula (nullable) is None
        # and model_fields_set contains the field
        if self.percent_off_formula is None and "percent_off_formula" in self.model_fields_set:
            _dict['percent_off_formula'] = None

        # set to None if amount_limit (nullable) is None
        # and model_fields_set contains the field
        if self.amount_limit is None and "amount_limit" in self.model_fields_set:
            _dict['amount_limit'] = None

        # set to None if fixed_amount (nullable) is None
        # and model_fields_set contains the field
        if self.fixed_amount is None and "fixed_amount" in self.model_fields_set:
            _dict['fixed_amount'] = None

        # set to None if fixed_amount_formula (nullable) is None
        # and model_fields_set contains the field
        if self.fixed_amount_formula is None and "fixed_amount_formula" in self.model_fields_set:
            _dict['fixed_amount_formula'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidationsValidateResponseBodyRedeemablesItemResultDiscount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "amount_off": obj.get("amount_off"),
            "amount_off_formula": obj.get("amount_off_formula"),
            "aggregated_amount_limit": obj.get("aggregated_amount_limit"),
            "effect": obj.get("effect"),
            "is_dynamic": obj.get("is_dynamic"),
            "unit_off": obj.get("unit_off"),
            "unit_off_formula": obj.get("unit_off_formula"),
            "unit_type": obj.get("unit_type"),
            "product": ValidationsValidateResponseBodyRedeemablesItemResultDiscountProduct.from_dict(obj["product"]) if obj.get("product") is not None else None,
            "sku": SimpleSkuDiscountUnit.from_dict(obj["sku"]) if obj.get("sku") is not None else None,
            "units": [DiscountUnitMultipleOneUnit.from_dict(_item) for _item in obj["units"]] if obj.get("units") is not None else None,
            "percent_off": obj.get("percent_off"),
            "percent_off_formula": obj.get("percent_off_formula"),
            "amount_limit": obj.get("amount_limit"),
            "fixed_amount": obj.get("fixed_amount"),
            "fixed_amount_formula": obj.get("fixed_amount_formula")
        })
        return _obj


