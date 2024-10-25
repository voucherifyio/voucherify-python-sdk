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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.product_collections_create_response_body_products_item import ProductCollectionsCreateResponseBodyProductsItem
from typing import Optional, Set
from typing_extensions import Self

class ProductCollectionsCreateResponseBody(BaseModel):
    """
    Response body schema for **POST** `v1/product-collections`.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Product collection ID.")
    name: Optional[StrictStr] = Field(default=None, description="Unique user-defined product collection name.")
    type: Optional[StrictStr] = Field(default=None, description="Describes whether the product collection is dynamic (products come in and leave based on set criteria) or static (manually selected products).")
    filter: Optional[Dict[str, Any]] = Field(default=None, description="Defines a set of criteria and boundary conditions for an `AUTO_UPDATE` product collection type.")
    products: Optional[List[ProductCollectionsCreateResponseBodyProductsItem]] = Field(default=None, description="Defines a set of products for a `STATIC` product collection type.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the product collection was created. The value is shown in the ISO 8601 format.")
    object: Optional[StrictStr] = Field(default='products_collection', description="The type of the object represented by JSON. This object stores information about the static product collection.")
    __properties: ClassVar[List[str]] = ["id", "name", "type", "filter", "products", "created_at", "object"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['STATIC', 'AUTO_UPDATE']):
            raise ValueError("must be one of enum values ('STATIC', 'AUTO_UPDATE')")
        return value

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['products_collection']):
            raise ValueError("must be one of enum values ('products_collection')")
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
        """Create an instance of ProductCollectionsCreateResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item_products in self.products:
                if _item_products:
                    _items.append(_item_products.to_dict())
            _dict['products'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if filter (nullable) is None
        # and model_fields_set contains the field
        if self.filter is None and "filter" in self.model_fields_set:
            _dict['filter'] = None

        # set to None if products (nullable) is None
        # and model_fields_set contains the field
        if self.products is None and "products" in self.model_fields_set:
            _dict['products'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductCollectionsCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "filter": obj.get("filter"),
            "products": [ProductCollectionsCreateResponseBodyProductsItem.from_dict(_item) for _item in obj["products"]] if obj.get("products") is not None else None,
            "created_at": obj.get("created_at"),
            "object": obj.get("object") if obj.get("object") is not None else 'products_collection'
        })
        return _obj


