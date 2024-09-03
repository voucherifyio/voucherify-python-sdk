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
from voucherify.models.promotion_stack_base import PromotionStackBase
from voucherify.models.promotions_stacks_update_response_body_tiers import PromotionsStacksUpdateResponseBodyTiers
from typing import Optional, Set
from typing_extensions import Self

class PromotionsStacksUpdateResponseBody(BaseModel):
    """
    Response body schema for **PUT** `v1/promotions/{campaignId}/stacks/{stackId}`.
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Promotion stack name.")
    tiers: Optional[PromotionsStacksUpdateResponseBodyTiers] = None
    id: Optional[StrictStr] = Field(default=None, description="Unique promotion stack ID.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the promotion stack was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the promotion stack was updated. The value is shown in the ISO 8601 format.")
    campaign_id: Optional[StrictStr] = Field(default=None, description="Promotion stack's parent campaign's unique ID.")
    object: Optional[StrictStr] = Field(default='promotion_stack', description="The type of the object represented by JSON. ")
    category_id: Optional[StrictStr] = Field(default=None, description="Promotion stack category ID.")
    categories: Optional[List[PromotionStackBase]] = Field(default=None, description="Details about the category assigned to the promotion stack.")
    __properties: ClassVar[List[str]] = ["name", "tiers", "id", "created_at", "updated_at", "campaign_id", "object", "category_id", "categories"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['promotion_stack']):
            raise ValueError("must be one of enum values ('promotion_stack')")
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
        """Create an instance of PromotionsStacksUpdateResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tiers
        if self.tiers:
            _dict['tiers'] = self.tiers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item_categories in self.categories:
                if _item_categories:
                    _items.append(_item_categories.to_dict())
            _dict['categories'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if tiers (nullable) is None
        # and model_fields_set contains the field
        if self.tiers is None and "tiers" in self.model_fields_set:
            _dict['tiers'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if campaign_id (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_id is None and "campaign_id" in self.model_fields_set:
            _dict['campaign_id'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PromotionsStacksUpdateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "tiers": PromotionsStacksUpdateResponseBodyTiers.from_dict(obj["tiers"]) if obj.get("tiers") is not None else None,
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "campaign_id": obj.get("campaign_id"),
            "object": obj.get("object") if obj.get("object") is not None else 'promotion_stack',
            "category_id": obj.get("category_id"),
            "categories": [PromotionStackBase.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None
        })
        return _obj


