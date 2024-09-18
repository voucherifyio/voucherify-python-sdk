# LoyaltiesMembersPointsExpirationListResponseBody

Response body schema for **GET** `v1/loyalties/{campaignId}/members/{memberId}/points-expiration`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about loyalty points expiration buckets in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of loyalty points expiration bucket objects. | [optional] [default to 'data']
**data** | [**List[LoyaltiesMembersPointsExpirationListResponseBodyDataItem]**](LoyaltiesMembersPointsExpirationListResponseBodyDataItem.md) | Contains array of loyalty points expiration buckets. | [optional] 
**total** | **int** | Total number of point expiration buckets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


