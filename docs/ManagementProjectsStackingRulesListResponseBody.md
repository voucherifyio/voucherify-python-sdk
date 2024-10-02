# ManagementProjectsStackingRulesListResponseBody

Response body schema for **GET** `/management/v1/projects/{projectId}/stacking-rules`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about the stacking rules in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of stacking rule objects. | [optional] [default to 'data']
**data** | [**List[ManagementProjectsStackingRules]**](ManagementProjectsStackingRules.md) | Array of only one stacking rule object. | [optional] 
**total** | **int** | The total number of stacking rule objects. It is always 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


