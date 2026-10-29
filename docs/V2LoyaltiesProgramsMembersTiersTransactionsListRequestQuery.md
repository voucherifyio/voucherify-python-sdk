# V2LoyaltiesProgramsMembersTiersTransactionsListRequestQuery

Request query schema for **GET** `/v2/loyalties/programs/{programId}/members/{memberId}/tiers/transactions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**junction** | **str** | Joins the field filters. Allowed values are &#x60;AND&#x60; and &#x60;OR&#x60;. Defaults to &#x60;AND&#x60;. | [optional] 
**card_id** | [**LoyaltiesProgramsMembersTiersTransactionsListRequestQueryCardId**](LoyaltiesProgramsMembersTiersTransactionsListRequestQueryCardId.md) |  | [optional] 
**card_definition_id** | [**LoyaltiesProgramsMembersTiersTransactionsListRequestQueryCardDefinitionId**](LoyaltiesProgramsMembersTiersTransactionsListRequestQueryCardDefinitionId.md) |  | [optional] 
**created_at** | [**TransactionFilterDateConditions**](TransactionFilterDateConditions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


