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
from voucherify.models.parameter_filters_list_campaigns_campaign_status import ParameterFiltersListCampaignsCampaignStatus
from voucherify.models.parameter_filters_list_campaigns_categories import ParameterFiltersListCampaignsCategories
from voucherify.models.parameter_filters_list_campaigns_category_ids import ParameterFiltersListCampaignsCategoryIds
from voucherify.models.parameter_filters_list_campaigns_is_referral_code import ParameterFiltersListCampaignsIsReferralCode
from voucherify.models.parameter_filters_list_campaigns_validity_timeframe import ParameterFiltersListCampaignsValidityTimeframe
from voucherify.models.parameter_filters_list_campaigns_voucher_type import ParameterFiltersListCampaignsVoucherType
from typing import Optional, Set
from typing_extensions import Self

class ParameterFiltersListCampaigns(BaseModel):
    """
    ParameterFiltersListCampaigns
    """ # noqa: E501
    campaign_status: Optional[ParameterFiltersListCampaignsCampaignStatus] = None
    is_referral_code: Optional[ParameterFiltersListCampaignsIsReferralCode] = None
    validity_timeframe: Optional[ParameterFiltersListCampaignsValidityTimeframe] = None
    voucher_type: Optional[ParameterFiltersListCampaignsVoucherType] = None
    categories: Optional[ParameterFiltersListCampaignsCategories] = None
    category_ids: Optional[ParameterFiltersListCampaignsCategoryIds] = None
    junction: Optional[Junction] = None
    __properties: ClassVar[List[str]] = ["campaign_status", "is_referral_code", "validity_timeframe", "voucher_type", "categories", "category_ids", "junction"]

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
        """Create an instance of ParameterFiltersListCampaigns from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of campaign_status
        if self.campaign_status:
            _dict['campaign_status'] = self.campaign_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_referral_code
        if self.is_referral_code:
            _dict['is_referral_code'] = self.is_referral_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher_type
        if self.voucher_type:
            _dict['voucher_type'] = self.voucher_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of categories
        if self.categories:
            _dict['categories'] = self.categories.to_dict()
        # override the default output from pydantic by calling `to_dict()` of category_ids
        if self.category_ids:
            _dict['category_ids'] = self.category_ids.to_dict()
        # set to None if campaign_status (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_status is None and "campaign_status" in self.model_fields_set:
            _dict['campaign_status'] = None

        # set to None if is_referral_code (nullable) is None
        # and model_fields_set contains the field
        if self.is_referral_code is None and "is_referral_code" in self.model_fields_set:
            _dict['is_referral_code'] = None

        # set to None if validity_timeframe (nullable) is None
        # and model_fields_set contains the field
        if self.validity_timeframe is None and "validity_timeframe" in self.model_fields_set:
            _dict['validity_timeframe'] = None

        # set to None if voucher_type (nullable) is None
        # and model_fields_set contains the field
        if self.voucher_type is None and "voucher_type" in self.model_fields_set:
            _dict['voucher_type'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if category_ids (nullable) is None
        # and model_fields_set contains the field
        if self.category_ids is None and "category_ids" in self.model_fields_set:
            _dict['category_ids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParameterFiltersListCampaigns from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaign_status": ParameterFiltersListCampaignsCampaignStatus.from_dict(obj["campaign_status"]) if obj.get("campaign_status") is not None else None,
            "is_referral_code": ParameterFiltersListCampaignsIsReferralCode.from_dict(obj["is_referral_code"]) if obj.get("is_referral_code") is not None else None,
            "validity_timeframe": ParameterFiltersListCampaignsValidityTimeframe.from_dict(obj["validity_timeframe"]) if obj.get("validity_timeframe") is not None else None,
            "voucher_type": ParameterFiltersListCampaignsVoucherType.from_dict(obj["voucher_type"]) if obj.get("voucher_type") is not None else None,
            "categories": ParameterFiltersListCampaignsCategories.from_dict(obj["categories"]) if obj.get("categories") is not None else None,
            "category_ids": ParameterFiltersListCampaignsCategoryIds.from_dict(obj["category_ids"]) if obj.get("category_ids") is not None else None,
            "junction": obj.get("junction")
        })
        return _obj


