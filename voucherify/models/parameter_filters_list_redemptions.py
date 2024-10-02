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
from voucherify.models.parameter_filters_list_redemptions_campaign_name import ParameterFiltersListRedemptionsCampaignName
from voucherify.models.parameter_filters_list_redemptions_customer_id import ParameterFiltersListRedemptionsCustomerId
from voucherify.models.parameter_filters_list_redemptions_failure_code import ParameterFiltersListRedemptionsFailureCode
from voucherify.models.parameter_filters_list_redemptions_object import ParameterFiltersListRedemptionsObject
from voucherify.models.parameter_filters_list_redemptions_parent_redemption_id import ParameterFiltersListRedemptionsParentRedemptionId
from voucherify.models.parameter_filters_list_redemptions_related_object_id import ParameterFiltersListRedemptionsRelatedObjectId
from voucherify.models.parameter_filters_list_redemptions_related_object_parent_id import ParameterFiltersListRedemptionsRelatedObjectParentId
from voucherify.models.parameter_filters_list_redemptions_result import ParameterFiltersListRedemptionsResult
from voucherify.models.parameter_filters_list_redemptions_user_login import ParameterFiltersListRedemptionsUserLogin
from voucherify.models.parameter_filters_list_redemptions_voucher_code import ParameterFiltersListRedemptionsVoucherCode
from typing import Optional, Set
from typing_extensions import Self

class ParameterFiltersListRedemptions(BaseModel):
    """
    ParameterFiltersListRedemptions
    """ # noqa: E501
    voucher_code: Optional[ParameterFiltersListRedemptionsVoucherCode] = None
    related_object_id: Optional[ParameterFiltersListRedemptionsRelatedObjectId] = None
    related_object_parent_id: Optional[ParameterFiltersListRedemptionsRelatedObjectParentId] = None
    parent_redemption_id: Optional[ParameterFiltersListRedemptionsParentRedemptionId] = None
    failure_code: Optional[ParameterFiltersListRedemptionsFailureCode] = None
    result: Optional[ParameterFiltersListRedemptionsResult] = None
    object: Optional[ParameterFiltersListRedemptionsObject] = None
    customer_id: Optional[ParameterFiltersListRedemptionsCustomerId] = None
    campaign_name: Optional[ParameterFiltersListRedemptionsCampaignName] = None
    user_login: Optional[ParameterFiltersListRedemptionsUserLogin] = None
    junction: Optional[Junction] = None
    __properties: ClassVar[List[str]] = ["voucher_code", "related_object_id", "related_object_parent_id", "parent_redemption_id", "failure_code", "result", "object", "customer_id", "campaign_name", "user_login", "junction"]

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
        """Create an instance of ParameterFiltersListRedemptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of voucher_code
        if self.voucher_code:
            _dict['voucher_code'] = self.voucher_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of related_object_id
        if self.related_object_id:
            _dict['related_object_id'] = self.related_object_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of related_object_parent_id
        if self.related_object_parent_id:
            _dict['related_object_parent_id'] = self.related_object_parent_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_redemption_id
        if self.parent_redemption_id:
            _dict['parent_redemption_id'] = self.parent_redemption_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of failure_code
        if self.failure_code:
            _dict['failure_code'] = self.failure_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict['object'] = self.object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customer_id'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_name
        if self.campaign_name:
            _dict['campaign_name'] = self.campaign_name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_login
        if self.user_login:
            _dict['user_login'] = self.user_login.to_dict()
        # set to None if voucher_code (nullable) is None
        # and model_fields_set contains the field
        if self.voucher_code is None and "voucher_code" in self.model_fields_set:
            _dict['voucher_code'] = None

        # set to None if related_object_id (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_id is None and "related_object_id" in self.model_fields_set:
            _dict['related_object_id'] = None

        # set to None if related_object_parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_parent_id is None and "related_object_parent_id" in self.model_fields_set:
            _dict['related_object_parent_id'] = None

        # set to None if parent_redemption_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_redemption_id is None and "parent_redemption_id" in self.model_fields_set:
            _dict['parent_redemption_id'] = None

        # set to None if failure_code (nullable) is None
        # and model_fields_set contains the field
        if self.failure_code is None and "failure_code" in self.model_fields_set:
            _dict['failure_code'] = None

        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict['result'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customer_id'] = None

        # set to None if campaign_name (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_name is None and "campaign_name" in self.model_fields_set:
            _dict['campaign_name'] = None

        # set to None if user_login (nullable) is None
        # and model_fields_set contains the field
        if self.user_login is None and "user_login" in self.model_fields_set:
            _dict['user_login'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParameterFiltersListRedemptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "voucher_code": ParameterFiltersListRedemptionsVoucherCode.from_dict(obj["voucher_code"]) if obj.get("voucher_code") is not None else None,
            "related_object_id": ParameterFiltersListRedemptionsRelatedObjectId.from_dict(obj["related_object_id"]) if obj.get("related_object_id") is not None else None,
            "related_object_parent_id": ParameterFiltersListRedemptionsRelatedObjectParentId.from_dict(obj["related_object_parent_id"]) if obj.get("related_object_parent_id") is not None else None,
            "parent_redemption_id": ParameterFiltersListRedemptionsParentRedemptionId.from_dict(obj["parent_redemption_id"]) if obj.get("parent_redemption_id") is not None else None,
            "failure_code": ParameterFiltersListRedemptionsFailureCode.from_dict(obj["failure_code"]) if obj.get("failure_code") is not None else None,
            "result": ParameterFiltersListRedemptionsResult.from_dict(obj["result"]) if obj.get("result") is not None else None,
            "object": ParameterFiltersListRedemptionsObject.from_dict(obj["object"]) if obj.get("object") is not None else None,
            "customer_id": ParameterFiltersListRedemptionsCustomerId.from_dict(obj["customer_id"]) if obj.get("customer_id") is not None else None,
            "campaign_name": ParameterFiltersListRedemptionsCampaignName.from_dict(obj["campaign_name"]) if obj.get("campaign_name") is not None else None,
            "user_login": ParameterFiltersListRedemptionsUserLogin.from_dict(obj["user_login"]) if obj.get("user_login") is not None else None,
            "junction": obj.get("junction")
        })
        return _obj


