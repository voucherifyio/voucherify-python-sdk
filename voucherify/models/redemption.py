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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.order_calculated import OrderCalculated
from voucherify.models.promotion_tier import PromotionTier
from voucherify.models.redemption_channel import RedemptionChannel
from voucherify.models.redemption_gift import RedemptionGift
from voucherify.models.redemption_loyalty_card import RedemptionLoyaltyCard
from voucherify.models.redemption_related_redemptions import RedemptionRelatedRedemptions
from voucherify.models.redemption_reward_result import RedemptionRewardResult
from voucherify.models.redemption_voucher import RedemptionVoucher
from voucherify.models.simple_customer import SimpleCustomer
from typing import Optional, Set
from typing_extensions import Self

class Redemption(BaseModel):
    """
    This is an object representing a redemption for **POST** `v1/redemptions` and **POST** `/client/v1/redemptions`.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique redemption ID.")
    object: Optional[StrictStr] = Field(default='redemption', description="The type of the object represented by the JSON")
    var_date: Optional[datetime] = Field(default=None, description="Timestamp representing the date and time when the object was created. The value is shown in the ISO 8601 format.", alias="date")
    customer_id: Optional[StrictStr] = Field(default=None, description="Unique customer ID of the redeeming customer.")
    tracking_id: Optional[StrictStr] = Field(default=None, description="Hashed customer source ID.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the redemption.")
    amount: Optional[StrictInt] = Field(default=None, description="For gift cards, this is a positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the number of redeemed credits. For loyalty cards, this is the number of loyalty points used in the transaction.")
    redemption: Optional[StrictStr] = Field(default=None, description="Unique redemption ID of the parent redemption.")
    result: Optional[StrictStr] = Field(default=None, description="Redemption result.")
    status: Optional[StrictStr] = Field(default=None, description="Redemption status.")
    related_redemptions: Optional[RedemptionRelatedRedemptions] = None
    failure_code: Optional[StrictStr] = Field(default=None, description="If the result is `FAILURE`, this parameter will provide a generic reason as to why the redemption failed.")
    failure_message: Optional[StrictStr] = Field(default=None, description="If the result is `FAILURE`, this parameter will provide a more expanded reason as to why the redemption failed.")
    order: Optional[OrderCalculated] = None
    channel: Optional[RedemptionChannel] = None
    customer: Optional[SimpleCustomer] = None
    related_object_type: Optional[StrictStr] = Field(default=None, description="Defines the related object.")
    related_object_id: Optional[StrictStr] = Field(default=None, description="Unique related object ID assigned by Voucherify, i.e. v_lfZi4rcEGe0sN9gmnj40bzwK2FH6QUno for a voucher.")
    promotion_tier: Optional[PromotionTier] = None
    reward: Optional[RedemptionRewardResult] = None
    gift: Optional[RedemptionGift] = None
    loyalty_card: Optional[RedemptionLoyaltyCard] = None
    voucher: Optional[RedemptionVoucher] = None
    __properties: ClassVar[List[str]] = ["id", "object", "date", "customer_id", "tracking_id", "metadata", "amount", "redemption", "result", "status", "related_redemptions", "failure_code", "failure_message", "order", "channel", "customer", "related_object_type", "related_object_id", "promotion_tier", "reward", "gift", "loyalty_card", "voucher"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['redemption']):
            raise ValueError("must be one of enum values ('redemption')")
        return value

    @field_validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SUCCESS', 'FAILURE']):
            raise ValueError("must be one of enum values ('SUCCESS', 'FAILURE')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SUCCEEDED', 'FAILED', 'ROLLED_BACK']):
            raise ValueError("must be one of enum values ('SUCCEEDED', 'FAILED', 'ROLLED_BACK')")
        return value

    @field_validator('related_object_type')
    def related_object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['voucher', 'promotion_tier', 'redemption']):
            raise ValueError("must be one of enum values ('voucher', 'promotion_tier', 'redemption')")
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
        """Create an instance of Redemption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of related_redemptions
        if self.related_redemptions:
            _dict['related_redemptions'] = self.related_redemptions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of channel
        if self.channel:
            _dict['channel'] = self.channel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotion_tier
        if self.promotion_tier:
            _dict['promotion_tier'] = self.promotion_tier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reward
        if self.reward:
            _dict['reward'] = self.reward.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_card
        if self.loyalty_card:
            _dict['loyalty_card'] = self.loyalty_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if object (nullable) is None
        # and model_fields_set contains the field
        if self.object is None and "object" in self.model_fields_set:
            _dict['object'] = None

        # set to None if var_date (nullable) is None
        # and model_fields_set contains the field
        if self.var_date is None and "var_date" in self.model_fields_set:
            _dict['date'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customer_id'] = None

        # set to None if tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_id is None and "tracking_id" in self.model_fields_set:
            _dict['tracking_id'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if amount (nullable) is None
        # and model_fields_set contains the field
        if self.amount is None and "amount" in self.model_fields_set:
            _dict['amount'] = None

        # set to None if redemption (nullable) is None
        # and model_fields_set contains the field
        if self.redemption is None and "redemption" in self.model_fields_set:
            _dict['redemption'] = None

        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict['result'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if related_redemptions (nullable) is None
        # and model_fields_set contains the field
        if self.related_redemptions is None and "related_redemptions" in self.model_fields_set:
            _dict['related_redemptions'] = None

        # set to None if failure_code (nullable) is None
        # and model_fields_set contains the field
        if self.failure_code is None and "failure_code" in self.model_fields_set:
            _dict['failure_code'] = None

        # set to None if failure_message (nullable) is None
        # and model_fields_set contains the field
        if self.failure_message is None and "failure_message" in self.model_fields_set:
            _dict['failure_message'] = None

        # set to None if channel (nullable) is None
        # and model_fields_set contains the field
        if self.channel is None and "channel" in self.model_fields_set:
            _dict['channel'] = None

        # set to None if related_object_type (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_type is None and "related_object_type" in self.model_fields_set:
            _dict['related_object_type'] = None

        # set to None if related_object_id (nullable) is None
        # and model_fields_set contains the field
        if self.related_object_id is None and "related_object_id" in self.model_fields_set:
            _dict['related_object_id'] = None

        # set to None if gift (nullable) is None
        # and model_fields_set contains the field
        if self.gift is None and "gift" in self.model_fields_set:
            _dict['gift'] = None

        # set to None if loyalty_card (nullable) is None
        # and model_fields_set contains the field
        if self.loyalty_card is None and "loyalty_card" in self.model_fields_set:
            _dict['loyalty_card'] = None

        # set to None if voucher (nullable) is None
        # and model_fields_set contains the field
        if self.voucher is None and "voucher" in self.model_fields_set:
            _dict['voucher'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Redemption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "object": obj.get("object") if obj.get("object") is not None else 'redemption',
            "date": obj.get("date"),
            "customer_id": obj.get("customer_id"),
            "tracking_id": obj.get("tracking_id"),
            "metadata": obj.get("metadata"),
            "amount": obj.get("amount"),
            "redemption": obj.get("redemption"),
            "result": obj.get("result"),
            "status": obj.get("status"),
            "related_redemptions": RedemptionRelatedRedemptions.from_dict(obj["related_redemptions"]) if obj.get("related_redemptions") is not None else None,
            "failure_code": obj.get("failure_code"),
            "failure_message": obj.get("failure_message"),
            "order": OrderCalculated.from_dict(obj["order"]) if obj.get("order") is not None else None,
            "channel": RedemptionChannel.from_dict(obj["channel"]) if obj.get("channel") is not None else None,
            "customer": SimpleCustomer.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "related_object_type": obj.get("related_object_type"),
            "related_object_id": obj.get("related_object_id"),
            "promotion_tier": PromotionTier.from_dict(obj["promotion_tier"]) if obj.get("promotion_tier") is not None else None,
            "reward": RedemptionRewardResult.from_dict(obj["reward"]) if obj.get("reward") is not None else None,
            "gift": RedemptionGift.from_dict(obj["gift"]) if obj.get("gift") is not None else None,
            "loyalty_card": RedemptionLoyaltyCard.from_dict(obj["loyalty_card"]) if obj.get("loyalty_card") is not None else None,
            "voucher": RedemptionVoucher.from_dict(obj["voucher"]) if obj.get("voucher") is not None else None
        })
        return _obj


