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
from voucherify.models.loyalties_members_redemption_redeem_response_body_related_redemptions_redemptions_item import LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptionsRedemptionsItem
from voucherify.models.loyalties_members_redemption_redeem_response_body_related_redemptions_rollbacks_item import LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptionsRollbacksItem
from typing import Optional, Set
from typing_extensions import Self

class LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptions(BaseModel):
    """
    LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptions
    """ # noqa: E501
    rollbacks: Optional[List[LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptionsRollbacksItem]] = None
    redemptions: Optional[List[LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptionsRedemptionsItem]] = None
    __properties: ClassVar[List[str]] = ["rollbacks", "redemptions"]

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
        """Create an instance of LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rollbacks (list)
        _items = []
        if self.rollbacks:
            for _item_rollbacks in self.rollbacks:
                if _item_rollbacks:
                    _items.append(_item_rollbacks.to_dict())
            _dict['rollbacks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in redemptions (list)
        _items = []
        if self.redemptions:
            for _item_redemptions in self.redemptions:
                if _item_redemptions:
                    _items.append(_item_redemptions.to_dict())
            _dict['redemptions'] = _items
        # set to None if rollbacks (nullable) is None
        # and model_fields_set contains the field
        if self.rollbacks is None and "rollbacks" in self.model_fields_set:
            _dict['rollbacks'] = None

        # set to None if redemptions (nullable) is None
        # and model_fields_set contains the field
        if self.redemptions is None and "redemptions" in self.model_fields_set:
            _dict['redemptions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rollbacks": [LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptionsRollbacksItem.from_dict(_item) for _item in obj["rollbacks"]] if obj.get("rollbacks") is not None else None,
            "redemptions": [LoyaltiesMembersRedemptionRedeemResponseBodyRelatedRedemptionsRedemptionsItem.from_dict(_item) for _item in obj["redemptions"]] if obj.get("redemptions") is not None else None
        })
        return _obj


