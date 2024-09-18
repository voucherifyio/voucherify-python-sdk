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
from typing import Optional, Set
from typing_extensions import Self

class LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsSubtotalAmount(BaseModel):
    """
    Defines the ratio based on the property defined in the calculation_type parameter. For every set of value (1, 10, etc) defined in the every parameter for the property defined in calculation_type, give the customer the number of points defined in the points parameter. In other words, for every calculation_type, give points.
    """ # noqa: E501
    every: Optional[StrictInt] = Field(default=None, description="Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $10 order amount is written as 1000.")
    points: Optional[StrictInt] = Field(default=None, description="Number of points to be awarded, i.e. how many points to be added to the loyalty card.")
    object: Optional[StrictStr] = Field(default=None, description="Type of object taken under consideration.")
    id: Optional[StrictStr] = Field(default=None, description="Unique ID of the resource, i.e. pc_75U0dHlr7u75BJodrW1AE3t6, prod_0bae32322150fd0546, or sku_0b7d7dfb090be5c619.")
    __properties: ClassVar[List[str]] = ["every", "points", "object", "id"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['products_collection', 'product', 'sku']):
            raise ValueError("must be one of enum values ('products_collection', 'product', 'sku')")
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
        """Create an instance of LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsSubtotalAmount from a JSON string"""
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
        # set to None if every (nullable) is None
        # and model_fields_set contains the field
        if self.every is None and "every" in self.model_fields_set:
            _dict['every'] = None

        # set to None if points (nullable) is None
        # and model_fields_set contains the field
        if self.points is None and "points" in self.model_fields_set:
            _dict['points'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyOrderItemsSubtotalAmount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "every": obj.get("every"),
            "points": obj.get("points"),
            "object": obj.get("object"),
            "id": obj.get("id")
        })
        return _obj


