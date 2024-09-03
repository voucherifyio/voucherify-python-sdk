# RewardsListResponseBody

Response body schema for **GET** `v1/rewards`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of transaction objects. | [optional] [default to 'data']
**data** | [**List[Reward]**](Reward.md) | A dictionary that contains an array of rewards. Each entry in the array is a separate transaction object. | [optional] 
**total** | **int** | Returns how many rewards in the project meet the limits defined by the query parameter definitions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


