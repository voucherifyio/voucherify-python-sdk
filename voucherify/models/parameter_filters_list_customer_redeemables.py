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
from voucherify.models.parameter_filters_list_customer_redeemables_campaign_id import ParameterFiltersListCustomerRedeemablesCampaignId
from voucherify.models.parameter_filters_list_customer_redeemables_campaign_type import ParameterFiltersListCustomerRedeemablesCampaignType
from voucherify.models.parameter_filters_list_customer_redeemables_created_at import ParameterFiltersListCustomerRedeemablesCreatedAt
from voucherify.models.parameter_filters_list_customer_redeemables_holder_role import ParameterFiltersListCustomerRedeemablesHolderRole
from voucherify.models.parameter_filters_list_customer_redeemables_id import ParameterFiltersListCustomerRedeemablesId
from voucherify.models.parameter_filters_list_customer_redeemables_redeemable_id import ParameterFiltersListCustomerRedeemablesRedeemableId
from voucherify.models.parameter_filters_list_customer_redeemables_redeemable_object import ParameterFiltersListCustomerRedeemablesRedeemableObject
from voucherify.models.parameter_filters_list_customer_redeemables_voucher_type import ParameterFiltersListCustomerRedeemablesVoucherType
from typing import Optional, Set
from typing_extensions import Self

class ParameterFiltersListCustomerRedeemables(BaseModel):
    """
    ParameterFiltersListCustomerRedeemables
    """ # noqa: E501
    id: Optional[ParameterFiltersListCustomerRedeemablesId] = None
    created_at: Optional[ParameterFiltersListCustomerRedeemablesCreatedAt] = None
    redeemable_id: Optional[ParameterFiltersListCustomerRedeemablesRedeemableId] = None
    redeemable_object: Optional[ParameterFiltersListCustomerRedeemablesRedeemableObject] = None
    holder_role: Optional[ParameterFiltersListCustomerRedeemablesHolderRole] = None
    campaign_id: Optional[ParameterFiltersListCustomerRedeemablesCampaignId] = None
    campaign_type: Optional[ParameterFiltersListCustomerRedeemablesCampaignType] = None
    voucher_type: Optional[ParameterFiltersListCustomerRedeemablesVoucherType] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "redeemable_id", "redeemable_object", "holder_role", "campaign_id", "campaign_type", "voucher_type"]

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
        """Create an instance of ParameterFiltersListCustomerRedeemables from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redeemable_id
        if self.redeemable_id:
            _dict['redeemable_id'] = self.redeemable_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redeemable_object
        if self.redeemable_object:
            _dict['redeemable_object'] = self.redeemable_object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of holder_role
        if self.holder_role:
            _dict['holder_role'] = self.holder_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_id
        if self.campaign_id:
            _dict['campaign_id'] = self.campaign_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_type
        if self.campaign_type:
            _dict['campaign_type'] = self.campaign_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher_type
        if self.voucher_type:
            _dict['voucher_type'] = self.voucher_type.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if redeemable_id (nullable) is None
        # and model_fields_set contains the field
        if self.redeemable_id is None and "redeemable_id" in self.model_fields_set:
            _dict['redeemable_id'] = None

        # set to None if redeemable_object (nullable) is None
        # and model_fields_set contains the field
        if self.redeemable_object is None and "redeemable_object" in self.model_fields_set:
            _dict['redeemable_object'] = None

        # set to None if holder_role (nullable) is None
        # and model_fields_set contains the field
        if self.holder_role is None and "holder_role" in self.model_fields_set:
            _dict['holder_role'] = None

        # set to None if campaign_id (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_id is None and "campaign_id" in self.model_fields_set:
            _dict['campaign_id'] = None

        # set to None if campaign_type (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_type is None and "campaign_type" in self.model_fields_set:
            _dict['campaign_type'] = None

        # set to None if voucher_type (nullable) is None
        # and model_fields_set contains the field
        if self.voucher_type is None and "voucher_type" in self.model_fields_set:
            _dict['voucher_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ParameterFiltersListCustomerRedeemables from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": ParameterFiltersListCustomerRedeemablesId.from_dict(obj["id"]) if obj.get("id") is not None else None,
            "created_at": ParameterFiltersListCustomerRedeemablesCreatedAt.from_dict(obj["created_at"]) if obj.get("created_at") is not None else None,
            "redeemable_id": ParameterFiltersListCustomerRedeemablesRedeemableId.from_dict(obj["redeemable_id"]) if obj.get("redeemable_id") is not None else None,
            "redeemable_object": ParameterFiltersListCustomerRedeemablesRedeemableObject.from_dict(obj["redeemable_object"]) if obj.get("redeemable_object") is not None else None,
            "holder_role": ParameterFiltersListCustomerRedeemablesHolderRole.from_dict(obj["holder_role"]) if obj.get("holder_role") is not None else None,
            "campaign_id": ParameterFiltersListCustomerRedeemablesCampaignId.from_dict(obj["campaign_id"]) if obj.get("campaign_id") is not None else None,
            "campaign_type": ParameterFiltersListCustomerRedeemablesCampaignType.from_dict(obj["campaign_type"]) if obj.get("campaign_type") is not None else None,
            "voucher_type": ParameterFiltersListCustomerRedeemablesVoucherType.from_dict(obj["voucher_type"]) if obj.get("voucher_type") is not None else None
        })
        return _obj


