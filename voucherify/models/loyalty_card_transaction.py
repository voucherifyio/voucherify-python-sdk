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
from voucherify.models.loyalty_card_transaction_details import LoyaltyCardTransactionDetails
from voucherify.models.loyalty_card_transactions_type import LoyaltyCardTransactionsType
from typing import Optional, Set
from typing_extensions import Self

class LoyaltyCardTransaction(BaseModel):
    """
    LoyaltyCardTransaction
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique transaction ID.")
    source_id: Optional[StrictStr] = Field(default=None, description="The merchant's transaction ID if it is different from the Voucherify transaction ID. It is really useful in case of an integration between multiple systems. It can be a transaction ID from a CRM system, database or 3rd-party service. In case of a redemption, this value is null.")
    voucher_id: Optional[StrictStr] = Field(default=None, description="Unique voucher ID.")
    campaign_id: Optional[StrictStr] = Field(default=None, description="Unqiue campaign ID of the voucher's parent campaign if it is part of campaign that generates bulk codes.")
    source: Optional[StrictStr] = Field(default=None, description="The channel through which the transaction took place, whether through the API or the the Dashboard. In case of a redemption, this value is null.")
    reason: Optional[StrictStr] = Field(default=None, description="Reason why the transaction occurred. In case of a redemption, this value is null.")
    related_transaction_id: Optional[StrictStr] = Field(default=None, description="The related transaction ID on the receiving card.")
    created_at: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the transaction was created. The value is shown in the ISO 8601 format.")
    details: Optional[LoyaltyCardTransactionDetails] = None
    type: Optional[LoyaltyCardTransactionsType] = None
    __properties: ClassVar[List[str]] = ["id", "source_id", "voucher_id", "campaign_id", "source", "reason", "related_transaction_id", "created_at", "details", "type"]

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
        """Create an instance of LoyaltyCardTransaction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['details'] = self.details.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['source_id'] = None

        # set to None if voucher_id (nullable) is None
        # and model_fields_set contains the field
        if self.voucher_id is None and "voucher_id" in self.model_fields_set:
            _dict['voucher_id'] = None

        # set to None if campaign_id (nullable) is None
        # and model_fields_set contains the field
        if self.campaign_id is None and "campaign_id" in self.model_fields_set:
            _dict['campaign_id'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        # set to None if related_transaction_id (nullable) is None
        # and model_fields_set contains the field
        if self.related_transaction_id is None and "related_transaction_id" in self.model_fields_set:
            _dict['related_transaction_id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltyCardTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "voucher_id": obj.get("voucher_id"),
            "campaign_id": obj.get("campaign_id"),
            "source": obj.get("source"),
            "reason": obj.get("reason"),
            "related_transaction_id": obj.get("related_transaction_id"),
            "created_at": obj.get("created_at"),
            "details": LoyaltyCardTransactionDetails.from_dict(obj["details"]) if obj.get("details") is not None else None,
            "type": obj.get("type")
        })
        return _obj


