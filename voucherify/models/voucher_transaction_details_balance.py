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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.voucher_transaction_details_balance_related_object import VoucherTransactionDetailsBalanceRelatedObject
from typing import Optional, Set
from typing_extensions import Self

class VoucherTransactionDetailsBalance(BaseModel):
    """
    Contains information on how the balance was affected by the transaction.
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="The type of voucher whose balance is being adjusted due to the transaction.")
    total: Optional[StrictInt] = Field(default=None, description="The number of all points or credits accumulated on the card as affected by add or subtract operations.")
    object: Optional[StrictStr] = Field(default='balance', description="The type of the object represented by the JSON.")
    points: Optional[StrictInt] = Field(default=None, description="Points added or subtracted in the transaction of a loyalty card.")
    balance: Optional[StrictInt] = Field(default=None, description="The available points or credits on the card after the transaction as affected by redemption or rollback.")
    operation_type: Optional[StrictStr] = Field(default=None, description="The type of the operation being performed. The operation type is `AUTOMATIC` if it is an automatic redemption.")
    related_object: Optional[VoucherTransactionDetailsBalanceRelatedObject] = None
    __properties: ClassVar[List[str]] = ["type", "total", "object", "points", "balance", "operation_type", "related_object"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['loyalty_card', 'gift_voucher']):
            raise ValueError("must be one of enum values ('loyalty_card', 'gift_voucher')")
        return value

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['balance']):
            raise ValueError("must be one of enum values ('balance')")
        return value

    @field_validator('operation_type')
    def operation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MANUAL', 'AUTOMATIC']):
            raise ValueError("must be one of enum values ('MANUAL', 'AUTOMATIC')")
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
        """Create an instance of VoucherTransactionDetailsBalance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of related_object
        if self.related_object:
            _dict['related_object'] = self.related_object.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if points (nullable) is None
        # and model_fields_set contains the field
        if self.points is None and "points" in self.model_fields_set:
            _dict['points'] = None

        # set to None if balance (nullable) is None
        # and model_fields_set contains the field
        if self.balance is None and "balance" in self.model_fields_set:
            _dict['balance'] = None

        # set to None if operation_type (nullable) is None
        # and model_fields_set contains the field
        if self.operation_type is None and "operation_type" in self.model_fields_set:
            _dict['operation_type'] = None

        # set to None if related_object (nullable) is None
        # and model_fields_set contains the field
        if self.related_object is None and "related_object" in self.model_fields_set:
            _dict['related_object'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VoucherTransactionDetailsBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "total": obj.get("total"),
            "object": obj.get("object") if obj.get("object") is not None else 'balance',
            "points": obj.get("points"),
            "balance": obj.get("balance"),
            "operation_type": obj.get("operation_type"),
            "related_object": VoucherTransactionDetailsBalanceRelatedObject.from_dict(obj["related_object"]) if obj.get("related_object") is not None else None
        })
        return _obj


