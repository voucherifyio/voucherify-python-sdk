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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProductsSkusUpdateRequestBody(BaseModel):
    """
    Request body schema for **PUT** `v1/products/{productId}/skus/{skuId}`.
    """ # noqa: E501
    sku: Optional[StrictStr] = Field(default=None, description="Unique user-defined SKU name.")
    price: Optional[StrictInt] = Field(default=None, description="SKU unit price. Value is multiplied by 100 to precisely represent 2 decimal places. For example `10000 cents` for `$100.00`.")
    currency: Optional[StrictStr] = Field(default=None, description="SKU price currency.")
    attributes: Optional[Dict[str, Any]] = Field(default=None, description="The attributes object stores values for all custom attributes inherited by the SKU from the parent product. A set of key/value pairs that are attached to a SKU object and are unique to each SKU within a product family.")
    image_url: Optional[StrictStr] = Field(default=None, description="The HTTPS URL pointing to the .png or .jpg file that will be used to render the SKU image.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the SKU. A set of key/value pairs that you can attach to a SKU object. It can be useful for storing additional information about the SKU in a structured format.")
    __properties: ClassVar[List[str]] = ["sku", "price", "currency", "attributes", "image_url", "metadata"]

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
        """Create an instance of ProductsSkusUpdateRequestBody from a JSON string"""
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
        # set to None if sku (nullable) is None
        # and model_fields_set contains the field
        if self.sku is None and "sku" in self.model_fields_set:
            _dict['sku'] = None

        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if attributes (nullable) is None
        # and model_fields_set contains the field
        if self.attributes is None and "attributes" in self.model_fields_set:
            _dict['attributes'] = None

        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict['image_url'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductsSkusUpdateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sku": obj.get("sku"),
            "price": obj.get("price"),
            "currency": obj.get("currency"),
            "attributes": obj.get("attributes"),
            "image_url": obj.get("image_url"),
            "metadata": obj.get("metadata")
        })
        return _obj

