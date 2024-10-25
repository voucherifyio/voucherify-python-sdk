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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.applicable_to_result_list import ApplicableToResultList
from voucherify.models.category_with_stacking_rules_type import CategoryWithStackingRulesType
from voucherify.models.inapplicable_to_result_list import InapplicableToResultList
from voucherify.models.order_calculated import OrderCalculated
from voucherify.models.validations_validate_response_body_redeemables_item_result import ValidationsValidateResponseBodyRedeemablesItemResult
from typing import Optional, Set
from typing_extensions import Self

class ValidationsValidateResponseBodyRedeemablesItem(BaseModel):
    """
    ValidationsValidateResponseBodyRedeemablesItem
    """ # noqa: E501
    status: Optional[StrictStr] = None
    id: Optional[StrictStr] = Field(default=None, description="Redeemable ID, i.e. the voucher code.")
    object: Optional[StrictStr] = Field(default=None, description="Redeemable's object type.")
    order: Optional[OrderCalculated] = None
    applicable_to: Optional[ApplicableToResultList] = None
    inapplicable_to: Optional[InapplicableToResultList] = None
    result: Optional[ValidationsValidateResponseBodyRedeemablesItemResult] = None
    metadata: Optional[Dict[str, Any]] = None
    categories: Optional[List[CategoryWithStackingRulesType]] = None
    __properties: ClassVar[List[str]] = ["status", "id", "object", "order", "applicable_to", "inapplicable_to", "result", "metadata", "categories"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['APPLICABLE', 'INAPPLICABLE', 'SKIPPED']):
            raise ValueError("must be one of enum values ('APPLICABLE', 'INAPPLICABLE', 'SKIPPED')")
        return value

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['voucher', 'promotion_tier']):
            raise ValueError("must be one of enum values ('voucher', 'promotion_tier')")
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
        """Create an instance of ValidationsValidateResponseBodyRedeemablesItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of applicable_to
        if self.applicable_to:
            _dict['applicable_to'] = self.applicable_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of inapplicable_to
        if self.inapplicable_to:
            _dict['inapplicable_to'] = self.inapplicable_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item_categories in self.categories:
                if _item_categories:
                    _items.append(_item_categories.to_dict())
            _dict['categories'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidationsValidateResponseBodyRedeemablesItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "id": obj.get("id"),
            "object": obj.get("object"),
            "order": OrderCalculated.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "applicable_to": ApplicableToResultList.from_dict(obj["applicable_to"]) if obj.get("applicable_to") is not None else None,
            "inapplicable_to": InapplicableToResultList.from_dict(obj["inapplicable_to"]) if obj.get("inapplicable_to") is not None else None,
            "result": ValidationsValidateResponseBodyRedeemablesItemResult.from_dict(obj["result"]) if obj.get("result") is not None else None,
            "metadata": obj.get("metadata"),
            "categories": [CategoryWithStackingRulesType.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None
        })
        return _obj


