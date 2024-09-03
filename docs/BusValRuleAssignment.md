# BusValRuleAssignment

Assignments of business validation rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for a assignment | [optional] 
**rule_id** | **str** | The unique identifier for a rule | [optional] 
**related_object_id** | **str** | The unique identifier for a related object | [optional] 
**related_object_type** | **str** | The type of related object | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the object was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the object was last updated in ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'validation_rules_assignment']
**validation_status** | **str** | The validation status of the assignment | [optional] 
**validation_omitted_rules** | **List[str]** | The list of omitted rules | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


