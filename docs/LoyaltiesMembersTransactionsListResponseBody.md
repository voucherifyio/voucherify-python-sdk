# LoyaltiesMembersTransactionsListResponseBody

Response body schema for **GET** `v1/loyalties/{campaignId}/members/{memberId}/transactions` and `/loyalties/members/{memberId}/transactions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of transaction objects. | [optional] [default to 'data']
**data** | [**List[LoyaltyCardTransaction]**](LoyaltyCardTransaction.md) | A dictionary that contains an array of transactions. Each entry in the array is a separate transaction object. | [optional] 
**has_more** | **bool** | As query results are always limited (by the limit parameter), the &#x60;has_more&#x60; flag indicates if there are more records for given filter parameters. This lets you know if you can run another request to get more records returned in the results. | [optional] 
**more_starting_after** | **str** | Returns an ID that can be used to return another page of results. Use the transaction ID in the &#x60;starting_after_id&#x60; query parameter to display another page of the results starting after the transaction with that ID. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

