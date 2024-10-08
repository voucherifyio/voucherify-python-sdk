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
from typing import Optional, Set
from typing_extensions import Self

class FiltersCondition(BaseModel):
    """
    FiltersCondition
    """ # noqa: E501
    var_in: Optional[Any] = Field(default=None, alias="$in")
    not_in: Optional[Any] = Field(default=None, alias="$not_in")
    var_is: Optional[Any] = Field(default=None, alias="$is")
    is_days_ago: Optional[Any] = Field(default=None, alias="$is_days_ago")
    is_days_in_future: Optional[Any] = Field(default=None, alias="$is_days_in_future")
    is_not: Optional[Any] = Field(default=None, alias="$is_not")
    has_value: Optional[Any] = Field(default=None, alias="$has_value")
    is_unknown: Optional[Any] = Field(default=None, alias="$is_unknown")
    contains: Optional[Any] = Field(default=None, alias="$contains")
    not_contain: Optional[Any] = Field(default=None, alias="$not_contain")
    starts_with: Optional[Any] = Field(default=None, alias="$starts_with")
    ends_with: Optional[Any] = Field(default=None, alias="$ends_with")
    more_than: Optional[Any] = Field(default=None, alias="$more_than")
    less_than: Optional[Any] = Field(default=None, alias="$less_than")
    more_than_ago: Optional[Any] = Field(default=None, alias="$more_than_ago")
    less_than_ago: Optional[Any] = Field(default=None, alias="$less_than_ago")
    more_than_future: Optional[Any] = Field(default=None, alias="$more_than_future")
    less_than_future: Optional[Any] = Field(default=None, alias="$less_than_future")
    more_than_equal: Optional[Any] = Field(default=None, alias="$more_than_equal")
    less_than_equal: Optional[Any] = Field(default=None, alias="$less_than_equal")
    after: Optional[Any] = Field(default=None, alias="$after")
    before: Optional[Any] = Field(default=None, alias="$before")
    count: Optional[Any] = Field(default=None, alias="$count")
    count_less: Optional[Any] = Field(default=None, alias="$count_less")
    count_more: Optional[Any] = Field(default=None, alias="$count_more")
    __properties: ClassVar[List[str]] = ["$in", "$not_in", "$is", "$is_days_ago", "$is_days_in_future", "$is_not", "$has_value", "$is_unknown", "$contains", "$not_contain", "$starts_with", "$ends_with", "$more_than", "$less_than", "$more_than_ago", "$less_than_ago", "$more_than_future", "$less_than_future", "$more_than_equal", "$less_than_equal", "$after", "$before", "$count", "$count_less", "$count_more"]

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
        """Create an instance of FiltersCondition from a JSON string"""
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
        # set to None if var_in (nullable) is None
        # and model_fields_set contains the field
        if self.var_in is None and "var_in" in self.model_fields_set:
            _dict['$in'] = None

        # set to None if not_in (nullable) is None
        # and model_fields_set contains the field
        if self.not_in is None and "not_in" in self.model_fields_set:
            _dict['$not_in'] = None

        # set to None if var_is (nullable) is None
        # and model_fields_set contains the field
        if self.var_is is None and "var_is" in self.model_fields_set:
            _dict['$is'] = None

        # set to None if is_days_ago (nullable) is None
        # and model_fields_set contains the field
        if self.is_days_ago is None and "is_days_ago" in self.model_fields_set:
            _dict['$is_days_ago'] = None

        # set to None if is_days_in_future (nullable) is None
        # and model_fields_set contains the field
        if self.is_days_in_future is None and "is_days_in_future" in self.model_fields_set:
            _dict['$is_days_in_future'] = None

        # set to None if is_not (nullable) is None
        # and model_fields_set contains the field
        if self.is_not is None and "is_not" in self.model_fields_set:
            _dict['$is_not'] = None

        # set to None if has_value (nullable) is None
        # and model_fields_set contains the field
        if self.has_value is None and "has_value" in self.model_fields_set:
            _dict['$has_value'] = None

        # set to None if is_unknown (nullable) is None
        # and model_fields_set contains the field
        if self.is_unknown is None and "is_unknown" in self.model_fields_set:
            _dict['$is_unknown'] = None

        # set to None if contains (nullable) is None
        # and model_fields_set contains the field
        if self.contains is None and "contains" in self.model_fields_set:
            _dict['$contains'] = None

        # set to None if not_contain (nullable) is None
        # and model_fields_set contains the field
        if self.not_contain is None and "not_contain" in self.model_fields_set:
            _dict['$not_contain'] = None

        # set to None if starts_with (nullable) is None
        # and model_fields_set contains the field
        if self.starts_with is None and "starts_with" in self.model_fields_set:
            _dict['$starts_with'] = None

        # set to None if ends_with (nullable) is None
        # and model_fields_set contains the field
        if self.ends_with is None and "ends_with" in self.model_fields_set:
            _dict['$ends_with'] = None

        # set to None if more_than (nullable) is None
        # and model_fields_set contains the field
        if self.more_than is None and "more_than" in self.model_fields_set:
            _dict['$more_than'] = None

        # set to None if less_than (nullable) is None
        # and model_fields_set contains the field
        if self.less_than is None and "less_than" in self.model_fields_set:
            _dict['$less_than'] = None

        # set to None if more_than_ago (nullable) is None
        # and model_fields_set contains the field
        if self.more_than_ago is None and "more_than_ago" in self.model_fields_set:
            _dict['$more_than_ago'] = None

        # set to None if less_than_ago (nullable) is None
        # and model_fields_set contains the field
        if self.less_than_ago is None and "less_than_ago" in self.model_fields_set:
            _dict['$less_than_ago'] = None

        # set to None if more_than_future (nullable) is None
        # and model_fields_set contains the field
        if self.more_than_future is None and "more_than_future" in self.model_fields_set:
            _dict['$more_than_future'] = None

        # set to None if less_than_future (nullable) is None
        # and model_fields_set contains the field
        if self.less_than_future is None and "less_than_future" in self.model_fields_set:
            _dict['$less_than_future'] = None

        # set to None if more_than_equal (nullable) is None
        # and model_fields_set contains the field
        if self.more_than_equal is None and "more_than_equal" in self.model_fields_set:
            _dict['$more_than_equal'] = None

        # set to None if less_than_equal (nullable) is None
        # and model_fields_set contains the field
        if self.less_than_equal is None and "less_than_equal" in self.model_fields_set:
            _dict['$less_than_equal'] = None

        # set to None if after (nullable) is None
        # and model_fields_set contains the field
        if self.after is None and "after" in self.model_fields_set:
            _dict['$after'] = None

        # set to None if before (nullable) is None
        # and model_fields_set contains the field
        if self.before is None and "before" in self.model_fields_set:
            _dict['$before'] = None

        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['$count'] = None

        # set to None if count_less (nullable) is None
        # and model_fields_set contains the field
        if self.count_less is None and "count_less" in self.model_fields_set:
            _dict['$count_less'] = None

        # set to None if count_more (nullable) is None
        # and model_fields_set contains the field
        if self.count_more is None and "count_more" in self.model_fields_set:
            _dict['$count_more'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FiltersCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$in": obj.get("$in"),
            "$not_in": obj.get("$not_in"),
            "$is": obj.get("$is"),
            "$is_days_ago": obj.get("$is_days_ago"),
            "$is_days_in_future": obj.get("$is_days_in_future"),
            "$is_not": obj.get("$is_not"),
            "$has_value": obj.get("$has_value"),
            "$is_unknown": obj.get("$is_unknown"),
            "$contains": obj.get("$contains"),
            "$not_contain": obj.get("$not_contain"),
            "$starts_with": obj.get("$starts_with"),
            "$ends_with": obj.get("$ends_with"),
            "$more_than": obj.get("$more_than"),
            "$less_than": obj.get("$less_than"),
            "$more_than_ago": obj.get("$more_than_ago"),
            "$less_than_ago": obj.get("$less_than_ago"),
            "$more_than_future": obj.get("$more_than_future"),
            "$less_than_future": obj.get("$less_than_future"),
            "$more_than_equal": obj.get("$more_than_equal"),
            "$less_than_equal": obj.get("$less_than_equal"),
            "$after": obj.get("$after"),
            "$before": obj.get("$before"),
            "$count": obj.get("$count"),
            "$count_less": obj.get("$count_less"),
            "$count_more": obj.get("$count_more")
        })
        return _obj


