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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from voucherify.models.management_project_api_usage_notifications import ManagementProjectApiUsageNotifications
from voucherify.models.management_project_default_code_config import ManagementProjectDefaultCodeConfig
from voucherify.models.management_project_limits import ManagementProjectLimits
from voucherify.models.management_project_webhooks_callout_notifications import ManagementProjectWebhooksCalloutNotifications
from typing import Optional, Set
from typing_extensions import Self

class ManagementProject(BaseModel):
    """
    ManagementProject
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the project.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the project.")
    description: Optional[StrictStr] = Field(default=None, description="A user-defined description of the project, e.g. its purpose, scope, region.")
    timezone: Optional[StrictStr] = Field(default=None, description="The time zone in which the project is established. It can be in the GMT format or in accordance with IANA time zone database.")
    currency: Optional[StrictStr] = Field(default=None, description="The currency used in the project. It is equal to a 3-letter ISO 4217 code.")
    dial_code: Optional[StrictStr] = Field(default=None, description="The country dial code for the project. It is equal to an ITU country code.")
    webhook_version: Optional[StrictStr] = Field(default='v2024-01-01', description="The webhook version used in the project.")
    client_trusted_domains: Optional[List[StrictStr]] = Field(default=None, description="An array of URL addresses that allow client requests.")
    client_redeem_enabled: Optional[StrictBool] = Field(default=None, description="Enables client-side redemption.")
    client_publish_enabled: Optional[StrictBool] = Field(default=None, description="Enables client-side publication.")
    client_list_vouchers_enabled: Optional[StrictBool] = Field(default=None, description="Enables client-side listing of vouchers.")
    client_create_customer_enabled: Optional[StrictBool] = Field(default=None, description="Enables client-side creation of customers.")
    client_loyalty_events_enabled: Optional[StrictBool] = Field(default=None, description="Enables client-side events for loyalty and referral programs.")
    client_set_voucher_expiration_date_enabled: Optional[StrictBool] = Field(default=None, description="Enables client-side setting of voucher expiration date.")
    api_usage_notifications: Optional[ManagementProjectApiUsageNotifications] = None
    webhooks_callout_notifications: Optional[ManagementProjectWebhooksCalloutNotifications] = None
    cluster_id: Optional[StrictStr] = Field(default=None, description="The identifier of the cluster where the project will be created.")
    case_sensitive_codes: Optional[StrictBool] = Field(default=None, description="Determines if the vouchers in the project will be: - case sensitive - if `true`, `C0dE-cfV` is **not** equal to `c0de-cfv`), - case insensitive - if `false`, `C0dE-cfV` is equal to `c0de-cfv`.")
    api_version: Optional[StrictStr] = Field(default='v2018-08-01', description="The API version used in the project. Currently, the default and only value is `v2018-08-01`.")
    is_sandbox: Optional[StrictBool] = Field(default=None, description="Determines if the project is a sandbox project.")
    webhook_token: Optional[StrictStr] = Field(default=None, description="Webhook token used for authentication.")
    default_code_config: Optional[ManagementProjectDefaultCodeConfig] = None
    limits: Optional[ManagementProjectLimits] = None
    __properties: ClassVar[List[str]] = ["id", "name", "description", "timezone", "currency", "dial_code", "webhook_version", "client_trusted_domains", "client_redeem_enabled", "client_publish_enabled", "client_list_vouchers_enabled", "client_create_customer_enabled", "client_loyalty_events_enabled", "client_set_voucher_expiration_date_enabled", "api_usage_notifications", "webhooks_callout_notifications", "cluster_id", "case_sensitive_codes", "api_version", "is_sandbox", "webhook_token", "default_code_config", "limits"]

    @field_validator('webhook_version')
    def webhook_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['v2024-01-01']):
            raise ValueError("must be one of enum values ('v2024-01-01')")
        return value

    @field_validator('api_version')
    def api_version_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['v2018-08-01']):
            raise ValueError("must be one of enum values ('v2018-08-01')")
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
        """Create an instance of ManagementProject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of api_usage_notifications
        if self.api_usage_notifications:
            _dict['api_usage_notifications'] = self.api_usage_notifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of webhooks_callout_notifications
        if self.webhooks_callout_notifications:
            _dict['webhooks_callout_notifications'] = self.webhooks_callout_notifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_code_config
        if self.default_code_config:
            _dict['default_code_config'] = self.default_code_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict['limits'] = self.limits.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if timezone (nullable) is None
        # and model_fields_set contains the field
        if self.timezone is None and "timezone" in self.model_fields_set:
            _dict['timezone'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if dial_code (nullable) is None
        # and model_fields_set contains the field
        if self.dial_code is None and "dial_code" in self.model_fields_set:
            _dict['dial_code'] = None

        # set to None if webhook_version (nullable) is None
        # and model_fields_set contains the field
        if self.webhook_version is None and "webhook_version" in self.model_fields_set:
            _dict['webhook_version'] = None

        # set to None if client_trusted_domains (nullable) is None
        # and model_fields_set contains the field
        if self.client_trusted_domains is None and "client_trusted_domains" in self.model_fields_set:
            _dict['client_trusted_domains'] = None

        # set to None if client_redeem_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.client_redeem_enabled is None and "client_redeem_enabled" in self.model_fields_set:
            _dict['client_redeem_enabled'] = None

        # set to None if client_publish_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.client_publish_enabled is None and "client_publish_enabled" in self.model_fields_set:
            _dict['client_publish_enabled'] = None

        # set to None if client_list_vouchers_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.client_list_vouchers_enabled is None and "client_list_vouchers_enabled" in self.model_fields_set:
            _dict['client_list_vouchers_enabled'] = None

        # set to None if client_create_customer_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.client_create_customer_enabled is None and "client_create_customer_enabled" in self.model_fields_set:
            _dict['client_create_customer_enabled'] = None

        # set to None if client_loyalty_events_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.client_loyalty_events_enabled is None and "client_loyalty_events_enabled" in self.model_fields_set:
            _dict['client_loyalty_events_enabled'] = None

        # set to None if client_set_voucher_expiration_date_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.client_set_voucher_expiration_date_enabled is None and "client_set_voucher_expiration_date_enabled" in self.model_fields_set:
            _dict['client_set_voucher_expiration_date_enabled'] = None

        # set to None if api_usage_notifications (nullable) is None
        # and model_fields_set contains the field
        if self.api_usage_notifications is None and "api_usage_notifications" in self.model_fields_set:
            _dict['api_usage_notifications'] = None

        # set to None if webhooks_callout_notifications (nullable) is None
        # and model_fields_set contains the field
        if self.webhooks_callout_notifications is None and "webhooks_callout_notifications" in self.model_fields_set:
            _dict['webhooks_callout_notifications'] = None

        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict['cluster_id'] = None

        # set to None if case_sensitive_codes (nullable) is None
        # and model_fields_set contains the field
        if self.case_sensitive_codes is None and "case_sensitive_codes" in self.model_fields_set:
            _dict['case_sensitive_codes'] = None

        # set to None if api_version (nullable) is None
        # and model_fields_set contains the field
        if self.api_version is None and "api_version" in self.model_fields_set:
            _dict['api_version'] = None

        # set to None if is_sandbox (nullable) is None
        # and model_fields_set contains the field
        if self.is_sandbox is None and "is_sandbox" in self.model_fields_set:
            _dict['is_sandbox'] = None

        # set to None if webhook_token (nullable) is None
        # and model_fields_set contains the field
        if self.webhook_token is None and "webhook_token" in self.model_fields_set:
            _dict['webhook_token'] = None

        # set to None if default_code_config (nullable) is None
        # and model_fields_set contains the field
        if self.default_code_config is None and "default_code_config" in self.model_fields_set:
            _dict['default_code_config'] = None

        # set to None if limits (nullable) is None
        # and model_fields_set contains the field
        if self.limits is None and "limits" in self.model_fields_set:
            _dict['limits'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManagementProject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "timezone": obj.get("timezone"),
            "currency": obj.get("currency"),
            "dial_code": obj.get("dial_code"),
            "webhook_version": obj.get("webhook_version") if obj.get("webhook_version") is not None else 'v2024-01-01',
            "client_trusted_domains": obj.get("client_trusted_domains"),
            "client_redeem_enabled": obj.get("client_redeem_enabled"),
            "client_publish_enabled": obj.get("client_publish_enabled"),
            "client_list_vouchers_enabled": obj.get("client_list_vouchers_enabled"),
            "client_create_customer_enabled": obj.get("client_create_customer_enabled"),
            "client_loyalty_events_enabled": obj.get("client_loyalty_events_enabled"),
            "client_set_voucher_expiration_date_enabled": obj.get("client_set_voucher_expiration_date_enabled"),
            "api_usage_notifications": ManagementProjectApiUsageNotifications.from_dict(obj["api_usage_notifications"]) if obj.get("api_usage_notifications") is not None else None,
            "webhooks_callout_notifications": ManagementProjectWebhooksCalloutNotifications.from_dict(obj["webhooks_callout_notifications"]) if obj.get("webhooks_callout_notifications") is not None else None,
            "cluster_id": obj.get("cluster_id"),
            "case_sensitive_codes": obj.get("case_sensitive_codes"),
            "api_version": obj.get("api_version") if obj.get("api_version") is not None else 'v2018-08-01',
            "is_sandbox": obj.get("is_sandbox"),
            "webhook_token": obj.get("webhook_token"),
            "default_code_config": ManagementProjectDefaultCodeConfig.from_dict(obj["default_code_config"]) if obj.get("default_code_config") is not None else None,
            "limits": ManagementProjectLimits.from_dict(obj["limits"]) if obj.get("limits") is not None else None
        })
        return _obj


