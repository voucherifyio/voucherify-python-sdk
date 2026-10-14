# LoyaltiesProgramsMembersCardsTransactionsListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/transactions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CardTransaction]**](CardTransaction.md) | Card transactions on the current page. | [optional] 
**cursor** | **object** |  | 
**object** | **str** | Object type marker, always &#x60;list&#x60;. | [optional] [default to 'list']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


