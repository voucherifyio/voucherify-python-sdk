# RedemptionsListResponseBody

Response body schema for **GET** `v1/redemptions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about redemptions in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of redemption objects. | [optional] [default to 'redemptions']
**redemptions** | [**List[RedemptionsListResponseBodyRedemptionsItem]**](RedemptionsListResponseBodyRedemptionsItem.md) |  | [optional] 
**total** | **int** | Total number of redemptions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


