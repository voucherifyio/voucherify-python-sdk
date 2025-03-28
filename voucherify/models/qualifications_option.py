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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from voucherify.models.qualifications_option_filters import QualificationsOptionFilters
from typing import Optional, Set
from typing_extensions import Self

class QualificationsOption(BaseModel):
    """
    Configure parameters returned in the response.
    """ # noqa: E501
    limit: Optional[Annotated[int, Field(le=50, strict=True)]] = Field(default=None, description="The maximum number of redeemables to be returned in the API request. The actual number of returned redeemables will be determined by the API. The default value is set to 5")
    starting_after: Optional[datetime] = Field(default=None, description="Cursor used for paging.")
    filters: Optional[QualificationsOptionFilters] = None
    expand: Optional[List[StrictStr]] = Field(default=None, description="The expand array lets you configure the parameters included in the response. Depending on the strings included in the array, the response will contain different details.   | **Expand Option** | **Response Body** | |:---|:---| | [`\"redeemable\"`] | Returns the redeemables':<br>- metadata<br>- redeemable name,<br>- campaign name,<br>- campaign ID| | [`\"category\"`] | - Returns an expanded `categories` object, showing details about the category. | | [`\"validation_rules\"`] | - Returns an expanded `validation_rules` object, showing details about the validation rules. |")
    sorting_rule: Optional[StrictStr] = Field(default=None, description="Is used to determine the order in which data is displayed in the result array.    - `DEFAULT` - Sorting descending by `created_at`   - `BEST_DEAL` - Sorting descending by `total_applied_discount_amount`   - `LEAST_DEAL` - Sorting ascending by `total_applied_discount_amount`")
    __properties: ClassVar[List[str]] = ["limit", "starting_after", "filters", "expand", "sorting_rule"]

    @field_validator('expand')
    def expand_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['redeemable', 'category', 'validation_rules']):
                raise ValueError("each list item must be one of ('redeemable', 'category', 'validation_rules')")
        return value

    @field_validator('sorting_rule')
    def sorting_rule_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BEST_DEAL', 'LEAST_DEAL', 'DEFAULT']):
            raise ValueError("must be one of enum values ('BEST_DEAL', 'LEAST_DEAL', 'DEFAULT')")
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
        """Create an instance of QualificationsOption from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if starting_after (nullable) is None
        # and model_fields_set contains the field
        if self.starting_after is None and "starting_after" in self.model_fields_set:
            _dict['starting_after'] = None

        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if expand (nullable) is None
        # and model_fields_set contains the field
        if self.expand is None and "expand" in self.model_fields_set:
            _dict['expand'] = None

        # set to None if sorting_rule (nullable) is None
        # and model_fields_set contains the field
        if self.sorting_rule is None and "sorting_rule" in self.model_fields_set:
            _dict['sorting_rule'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QualificationsOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limit": obj.get("limit"),
            "starting_after": obj.get("starting_after"),
            "filters": QualificationsOptionFilters.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "expand": obj.get("expand"),
            "sorting_rule": obj.get("sorting_rule")
        })
        return _obj


