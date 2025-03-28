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
from voucherify.models.usage_notifications import UsageNotifications
from typing import Optional, Set
from typing_extensions import Self

class ManagementProjectsUpdateRequestBodyApiUsageNotifications(BaseModel):
    """
    Determines the notification settings.
    """ # noqa: E501
    messages: Optional[UsageNotifications] = None
    api_calls: Optional[UsageNotifications] = None
    bulk_api_calls: Optional[UsageNotifications] = None
    webhook_calls: Optional[UsageNotifications] = None
    cycle_calls: Optional[UsageNotifications] = None
    __properties: ClassVar[List[str]] = ["messages", "api_calls", "bulk_api_calls", "webhook_calls", "cycle_calls"]

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
        """Create an instance of ManagementProjectsUpdateRequestBodyApiUsageNotifications from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of messages
        if self.messages:
            _dict['messages'] = self.messages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api_calls
        if self.api_calls:
            _dict['api_calls'] = self.api_calls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_api_calls
        if self.bulk_api_calls:
            _dict['bulk_api_calls'] = self.bulk_api_calls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhook_calls
        if self.webhook_calls:
            _dict['webhook_calls'] = self.webhook_calls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cycle_calls
        if self.cycle_calls:
            _dict['cycle_calls'] = self.cycle_calls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagementProjectsUpdateRequestBodyApiUsageNotifications from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "messages": UsageNotifications.from_dict(obj["messages"]) if obj.get("messages") is not None else None,
            "api_calls": UsageNotifications.from_dict(obj["api_calls"]) if obj.get("api_calls") is not None else None,
            "bulk_api_calls": UsageNotifications.from_dict(obj["bulk_api_calls"]) if obj.get("bulk_api_calls") is not None else None,
            "webhook_calls": UsageNotifications.from_dict(obj["webhook_calls"]) if obj.get("webhook_calls") is not None else None,
            "cycle_calls": UsageNotifications.from_dict(obj["cycle_calls"]) if obj.get("cycle_calls") is not None else None
        })
        return _obj


