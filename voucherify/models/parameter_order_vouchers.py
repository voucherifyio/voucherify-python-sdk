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
import json
from enum import Enum
from typing_extensions import Self


class ParameterOrderVouchers(str, Enum):
    """
    ParameterOrderVouchers
    """

    """
    allowed enum values
    """
    CREATED_AT = 'created_at'
    MINUS_CREATED_AT = '-created_at'
    UPDATED_AT = 'updated_at'
    MINUS_UPDATED_AT = '-updated_at'
    CODE = 'code'
    MINUS_CODE = '-code'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ParameterOrderVouchers from a JSON string"""
        return cls(json.loads(json_str))


