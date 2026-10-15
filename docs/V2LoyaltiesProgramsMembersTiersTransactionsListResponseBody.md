# V2LoyaltiesProgramsMembersTiersTransactionsListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/members/{memberId}/tiers/transactions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TierTransaction]**](TierTransaction.md) | List of tier transactions. | [optional] 
**cursor** | [**ListCursor**](ListCursor.md) |  | [optional] 
**object** | **str** | Object type marker. Always &#x60;list&#x60;. | [optional] [default to 'list']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


