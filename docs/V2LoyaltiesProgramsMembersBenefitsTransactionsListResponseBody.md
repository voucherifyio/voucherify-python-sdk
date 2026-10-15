# V2LoyaltiesProgramsMembersBenefitsTransactionsListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/members/{memberId}/benefits/transactions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BenefitTransaction]**](BenefitTransaction.md) | List of benefit transactions. | [optional] 
**cursor** | [**V2LoyaltiesProgramsMembersBenefitsTransactionsListResponseBodyCursor**](V2LoyaltiesProgramsMembersBenefitsTransactionsListResponseBodyCursor.md) |  | [optional] 
**object** | **str** | Object type marker. Always &#x60;list&#x60;. | [optional] [default to 'list']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


