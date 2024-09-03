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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.client_redemptions_redeem_request_body_redeemables_item_gift import ClientRedemptionsRedeemRequestBodyRedeemablesItemGift
from voucherify.models.client_redemptions_redeem_request_body_redeemables_item_reward import ClientRedemptionsRedeemRequestBodyRedeemablesItemReward
from typing import Optional, Set
from typing_extensions import Self

class ClientRedemptionsRedeemRequestBodyRedeemablesItem(BaseModel):
    """
    ClientRedemptionsRedeemRequestBodyRedeemablesItem
    """ # noqa: E501
    object: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    gift: Optional[ClientRedemptionsRedeemRequestBodyRedeemablesItemGift] = None
    reward: Optional[ClientRedemptionsRedeemRequestBodyRedeemablesItemReward] = None
    __properties: ClassVar[List[str]] = ["object", "id", "gift", "reward"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['voucher', 'promotion_tier', 'promotion_stack']):
            raise ValueError("must be one of enum values ('voucher', 'promotion_tier', 'promotion_stack')")
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
        """Create an instance of ClientRedemptionsRedeemRequestBodyRedeemablesItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reward
        if self.reward:
            _dict['reward'] = self.reward.to_dict()
        # set to None if gift (nullable) is None
        # and model_fields_set contains the field
        if self.gift is None and "gift" in self.model_fields_set:
            _dict['gift'] = None

        # set to None if reward (nullable) is None
        # and model_fields_set contains the field
        if self.reward is None and "reward" in self.model_fields_set:
            _dict['reward'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClientRedemptionsRedeemRequestBodyRedeemablesItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "object": obj.get("object"),
            "id": obj.get("id"),
            "gift": ClientRedemptionsRedeemRequestBodyRedeemablesItemGift.from_dict(obj["gift"]) if obj.get("gift") is not None else None,
            "reward": ClientRedemptionsRedeemRequestBodyRedeemablesItemReward.from_dict(obj["reward"]) if obj.get("reward") is not None else None
        })
        return _obj


