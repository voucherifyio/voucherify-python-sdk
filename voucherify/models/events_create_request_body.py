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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from voucherify.models.customer import Customer
from voucherify.models.events_create_request_body_loyalty import EventsCreateRequestBodyLoyalty
from voucherify.models.events_create_request_body_referral import EventsCreateRequestBodyReferral
from typing import Optional, Set
from typing_extensions import Self

class EventsCreateRequestBody(BaseModel):
    """
    Request body schema for **POST** `v1/events`.
    """ # noqa: E501
    event: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=300)]] = Field(default=None, description="Event name. This is the same name that you used to define a custom event in the **Dashboard** > **Project Settings** > **Event Schema**.")
    customer: Customer
    referral: Optional[EventsCreateRequestBodyReferral] = None
    loyalty: Optional[EventsCreateRequestBodyLoyalty] = None
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="The metadata object stores all custom attributes assigned to the event. A set of key/value pairs that you can attach to an event object. It can be useful for storing additional information about the event in a structured format. Event metadata schema is defined in the **Dashboard** > **Project Settings** > **Event Schema** > **Edit particular event** > **Metadata property definition**.")
    __properties: ClassVar[List[str]] = ["event", "customer", "referral", "loyalty", "metadata"]

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
        """Create an instance of EventsCreateRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of referral
        if self.referral:
            _dict['referral'] = self.referral.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty
        if self.loyalty:
            _dict['loyalty'] = self.loyalty.to_dict()
        # set to None if event (nullable) is None
        # and model_fields_set contains the field
        if self.event is None and "event" in self.model_fields_set:
            _dict['event'] = None

        # set to None if referral (nullable) is None
        # and model_fields_set contains the field
        if self.referral is None and "referral" in self.model_fields_set:
            _dict['referral'] = None

        # set to None if loyalty (nullable) is None
        # and model_fields_set contains the field
        if self.loyalty is None and "loyalty" in self.model_fields_set:
            _dict['loyalty'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventsCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event": obj.get("event"),
            "customer": Customer.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "referral": EventsCreateRequestBodyReferral.from_dict(obj["referral"]) if obj.get("referral") is not None else None,
            "loyalty": EventsCreateRequestBodyLoyalty.from_dict(obj["loyalty"]) if obj.get("loyalty") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


