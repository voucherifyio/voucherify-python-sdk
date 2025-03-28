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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AccessSettingsAssign(BaseModel):
    """
    Assigns the campaign to an area or a store. Provide the area and/or store IDs in the respective arrays. If a campaign changes assignments between areas or stores, unassign it from the area. For example, if a campaign is assigned to Area-01, but it must be now assigned to Store-01 within this area, you have to unassign the campaign from Area-01 and assign to Store-01 only.  If you want to assign the campaign to stores only, you do not have to send the area ID.
    """ # noqa: E501
    areas_ids: Optional[List[StrictStr]] = Field(default=None, description="List all area IDs to which the campaign will be assigned.")
    area_stores_ids: Optional[List[StrictStr]] = Field(default=None, description="List all store IDs to which the campaign will be assigned.")
    area_all_stores_ids: Optional[List[StrictStr]] = Field(default=None, description="List all area IDs where the campaign is assigned to all stores in the area. This assignment is not equal to the assignment to all `area_stores_ids` listed separately.")
    __properties: ClassVar[List[str]] = ["areas_ids", "area_stores_ids", "area_all_stores_ids"]

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
        """Create an instance of AccessSettingsAssign from a JSON string"""
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
        # set to None if areas_ids (nullable) is None
        # and model_fields_set contains the field
        if self.areas_ids is None and "areas_ids" in self.model_fields_set:
            _dict['areas_ids'] = None

        # set to None if area_stores_ids (nullable) is None
        # and model_fields_set contains the field
        if self.area_stores_ids is None and "area_stores_ids" in self.model_fields_set:
            _dict['area_stores_ids'] = None

        # set to None if area_all_stores_ids (nullable) is None
        # and model_fields_set contains the field
        if self.area_all_stores_ids is None and "area_all_stores_ids" in self.model_fields_set:
            _dict['area_all_stores_ids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AccessSettingsAssign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "areas_ids": obj.get("areas_ids"),
            "area_stores_ids": obj.get("area_stores_ids"),
            "area_all_stores_ids": obj.get("area_all_stores_ids")
        })
        return _obj


