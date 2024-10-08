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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.campaigns_vouchers_create_in_bulk_request_body_redemption import CampaignsVouchersCreateInBulkRequestBodyRedemption
from voucherify.models.code_config import CodeConfig
from typing import Optional, Set
from typing_extensions import Self

class CampaignsVouchersCreateInBulkRequestBody(BaseModel):
    """
    Request body schema for **POST** `v1/campaigns/{campaignId}/vouchers`.
    """ # noqa: E501
    code: Optional[StrictStr] = Field(default=None, description="Unique voucher code.")
    code_config: Optional[CodeConfig] = None
    category: Optional[StrictStr] = Field(default=None, description="The category assigned to the campaign. Either pass this parameter OR the `category_id`.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the voucher. A set of key/value pairs that you can attach to a voucher object. It can be useful for storing additional information about the voucher in a structured format.")
    redemption: Optional[CampaignsVouchersCreateInBulkRequestBodyRedemption] = None
    additional_info: Optional[StrictStr] = Field(default=None, description="An optional field to keep any extra textual information about the code such as a code description and details.")
    start_date: Optional[datetime] = Field(default=None, description="Activation timestamp defines when the voucher starts to be active in ISO 8601 format. Voucher is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(default=None, description="Expiration timestamp defines when the voucher expires in ISO 8601 format.  Voucher is *inactive after* this date.")
    __properties: ClassVar[List[str]] = ["code", "code_config", "category", "metadata", "redemption", "additional_info", "start_date", "expiration_date"]

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
        """Create an instance of CampaignsVouchersCreateInBulkRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of code_config
        if self.code_config:
            _dict['code_config'] = self.code_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and "code" in self.model_fields_set:
            _dict['code'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if redemption (nullable) is None
        # and model_fields_set contains the field
        if self.redemption is None and "redemption" in self.model_fields_set:
            _dict['redemption'] = None

        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additional_info'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['start_date'] = None

        # set to None if expiration_date (nullable) is None
        # and model_fields_set contains the field
        if self.expiration_date is None and "expiration_date" in self.model_fields_set:
            _dict['expiration_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CampaignsVouchersCreateInBulkRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "code_config": CodeConfig.from_dict(obj["code_config"]) if obj.get("code_config") is not None else None,
            "category": obj.get("category"),
            "metadata": obj.get("metadata"),
            "redemption": CampaignsVouchersCreateInBulkRequestBodyRedemption.from_dict(obj["redemption"]) if obj.get("redemption") is not None else None,
            "additional_info": obj.get("additional_info"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date")
        })
        return _obj


