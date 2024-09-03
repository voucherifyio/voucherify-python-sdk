# LoyaltiesMembersRewardsListResponseBody

Response body schema for **GET** `v1/loyalties/members/{memberId}/rewards`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of loyalty reward objects. | [optional] [default to 'data']
**data** | [**List[LoyaltiesMembersRewardsListResponseBodyDataItem]**](LoyaltiesMembersRewardsListResponseBodyDataItem.md) | Contains array of loyalty reward objects. | [optional] 
**total** | **int** | Total number of loyalty reward objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


