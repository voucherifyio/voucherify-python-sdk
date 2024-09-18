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
from voucherify.models.junction import Junction
from voucherify.models.qualifications_field_conditions import QualificationsFieldConditions
from voucherify.models.qualifications_option_filters_campaign_type import QualificationsOptionFiltersCampaignType
from voucherify.models.qualifications_option_filters_holder_role import QualificationsOptionFiltersHolderRole
from voucherify.models.qualifications_option_filters_resource_type import QualificationsOptionFiltersResourceType
from typing import Optional, Set
from typing_extensions import Self

class QualificationsOptionFilters(BaseModel):
    """
    A set of filters to return only a specific category or type of redeemable.
    """ # noqa: E501
    junction: Optional[Junction] = None
    category_id: Optional[QualificationsFieldConditions] = None
    campaign_id: Optional[QualificationsFieldConditions] = None
    campaign_type: Optional[QualificationsOptionFiltersCampaignType] = None
    resource_id: Optional[QualificationsFieldConditions] = None
    resource_type: Optional[QualificationsOptionFiltersResourceType] = None
    voucher_type: Optional[QualificationsFieldConditions] = None
    code: Optional[QualificationsFieldConditions] = None
    holder_role: Optional[QualificationsOptionFiltersHolderRole] = None
    __properties: ClassVar[List[str]] = ["junction", "category_id", "campaign_id", "campaign_type", "resource_id", "resource_type", "voucher_type", "code", "holder_role"]

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
        """Create an instance of QualificationsOptionFilters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of category_id
        if self.category_id:
            _dict['category_id'] = self.category_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_id
        if self.campaign_id:
            _dict['campaign_id'] = self.campaign_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_type
        if self.campaign_type:
            _dict['campaign_type'] = self.campaign_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_id
        if self.resource_id:
            _dict['resource_id'] = self.resource_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_type
        if self.resource_type:
            _dict['resource_type'] = self.resource_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher_type
        if self.voucher_type:
            _dict['voucher_type'] = self.voucher_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code
        if self.code:
            _dict['code'] = self.code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of holder_role
        if self.holder_role:
            _dict['holder_role'] = self.holder_role.to_dict()
        # set to None if campaign_type (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_type is None and "campaign_type" in self.model_fields_set:
            _dict['campaign_type'] = None

        # set to None if resource_type (nullable) is None
        # and model_fields_set contains the field
        if self.resource_type is None and "resource_type" in self.model_fields_set:
            _dict['resource_type'] = None

        # set to None if holder_role (nullable) is None
        # and model_fields_set contains the field
        if self.holder_role is None and "holder_role" in self.model_fields_set:
            _dict['holder_role'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QualificationsOptionFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "junction": obj.get("junction"),
            "category_id": QualificationsFieldConditions.from_dict(obj["category_id"]) if obj.get("category_id") is not None else None,
            "campaign_id": QualificationsFieldConditions.from_dict(obj["campaign_id"]) if obj.get("campaign_id") is not None else None,
            "campaign_type": QualificationsOptionFiltersCampaignType.from_dict(obj["campaign_type"]) if obj.get("campaign_type") is not None else None,
            "resource_id": QualificationsFieldConditions.from_dict(obj["resource_id"]) if obj.get("resource_id") is not None else None,
            "resource_type": QualificationsOptionFiltersResourceType.from_dict(obj["resource_type"]) if obj.get("resource_type") is not None else None,
            "voucher_type": QualificationsFieldConditions.from_dict(obj["voucher_type"]) if obj.get("voucher_type") is not None else None,
            "code": QualificationsFieldConditions.from_dict(obj["code"]) if obj.get("code") is not None else None,
            "holder_role": QualificationsOptionFiltersHolderRole.from_dict(obj["holder_role"]) if obj.get("holder_role") is not None else None
        })
        return _obj


