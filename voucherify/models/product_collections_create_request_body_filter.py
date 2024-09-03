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
from voucherify.models.field_conditions import FieldConditions
from voucherify.models.junction import Junction
from typing import Optional, Set
from typing_extensions import Self

class ProductCollectionsCreateRequestBodyFilter(BaseModel):
    """
    Defines a set of criteria and boundary conditions for an `AUTO_UPDATE` product collection type.
    """ # noqa: E501
    junction: Junction
    id: Optional[FieldConditions] = None
    product_id: Optional[FieldConditions] = None
    source_id: Optional[FieldConditions] = None
    name: Optional[FieldConditions] = None
    price: Optional[FieldConditions] = None
    object: Optional[FieldConditions] = None
    attributes: Optional[FieldConditions] = None
    metadata: Optional[FieldConditions] = None
    image_url: Optional[FieldConditions] = None
    skus: Optional[FieldConditions] = None
    created_at: Optional[FieldConditions] = None
    updated_at: Optional[FieldConditions] = None
    __properties: ClassVar[List[str]] = ["junction", "id", "product_id", "source_id", "name", "price", "object", "attributes", "metadata", "image_url", "skus", "created_at", "updated_at"]

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
        """Create an instance of ProductCollectionsCreateRequestBodyFilter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_id
        if self.product_id:
            _dict['product_id'] = self.product_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_id
        if self.source_id:
            _dict['source_id'] = self.source_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict['object'] = self.object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image_url
        if self.image_url:
            _dict['image_url'] = self.image_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of skus
        if self.skus:
            _dict['skus'] = self.skus.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_at
        if self.updated_at:
            _dict['updated_at'] = self.updated_at.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductCollectionsCreateRequestBodyFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "junction": obj.get("junction"),
            "id": FieldConditions.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "product_id": FieldConditions.from_dict(obj["product_id"]) if obj.get("product_id") is not None else None,
            "source_id": FieldConditions.from_dict(obj["source_id"]) if obj.get("source_id") is not None else None,
            "name": FieldConditions.from_dict(obj["name"]) if obj.get("name") is not None else None,
            "price": FieldConditions.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "object": FieldConditions.from_dict(obj["object"]) if obj.get("object") is not None else None,
            "attributes": FieldConditions.from_dict(obj["attributes"]) if obj.get("attributes") is not None else None,
            "metadata": FieldConditions.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "image_url": FieldConditions.from_dict(obj["image_url"]) if obj.get("image_url") is not None else None,
            "skus": FieldConditions.from_dict(obj["skus"]) if obj.get("skus") is not None else None,
            "created_at": FieldConditions.from_dict(obj["created_at"]) if obj.get("created_at") is not None else None,
            "updated_at": FieldConditions.from_dict(obj["updated_at"]) if obj.get("updated_at") is not None else None
        })
        return _obj


