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
from typing_extensions import Annotated
from voucherify.models.loyalties_members_balance_update_response_body_related_object import LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject
from typing import Optional, Set
from typing_extensions import Self

class LoyaltiesMembersBalanceUpdateResponseBody(BaseModel):
    """
    Response schema for **POST** `v1/loyalties/members/{memberId}/balance` and for **POST** `v1/loyalties/{campaignId}/members/{memberId}/balance`.
    """ # noqa: E501
    points: Optional[StrictInt] = Field(default=None, description="The incremental points removed or added to the current balance on the loyalty card.")
    total: Optional[StrictInt] = Field(default=None, description="The total of points accrued over the lifetime of the loyalty card.")
    balance: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The balance after adding/removing points.")
    type: Optional[StrictStr] = Field(default=None, description="The type of voucher being modified.")
    object: Optional[Annotated[str, Field(strict=True)]] = Field(default='balance', description="The type of the object represented by JSON. Default is balance.")
    related_object: Optional[LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject] = None
    operation_type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["points", "total", "balance", "type", "object", "related_object", "operation_type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['loyalty_card', 'gift_voucher']):
            raise ValueError("must be one of enum values ('loyalty_card', 'gift_voucher')")
        return value

    @field_validator('object')
    def object_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"balance", value):
            raise ValueError(r"must validate the regular expression /balance/")
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
        """Create an instance of LoyaltiesMembersBalanceUpdateResponseBody from a JSON string"""
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
        # set to None if points (nullable) is None
        # and model_fields_set contains the field
        if self.points is None and "points" in self.model_fields_set:
            _dict['points'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if balance (nullable) is None
        # and model_fields_set contains the field
        if self.balance is None and "balance" in self.model_fields_set:
            _dict['balance'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if related_object (nullable) is None
        # and model_fields_set contains the field
        if self.related_object is None and "related_object" in self.model_fields_set:
            _dict['related_object'] = None

        # set to None if operation_type (nullable) is None
        # and model_fields_set contains the field
        if self.operation_type is None and "operation_type" in self.model_fields_set:
            _dict['operation_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltiesMembersBalanceUpdateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "points": obj.get("points"),
            "total": obj.get("total"),
            "balance": obj.get("balance"),
            "type": obj.get("type"),
            "object": obj.get("object") if obj.get("object") is not None else 'balance',
            "related_object": LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject.from_dict(obj["related_object"]) if obj.get("related_object") is not None else None,
            "operation_type": obj.get("operation_type")
        })
        return _obj

