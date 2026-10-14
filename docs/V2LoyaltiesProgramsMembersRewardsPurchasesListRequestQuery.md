# V2LoyaltiesProgramsMembersRewardsPurchasesListRequestQuery

Request query schema for **GET** `/v2/loyalties/programs/{programId}/members/{memberId}/rewards/purchases`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**junction** | **str** | Logical junction between the field filters. Defaults to AND behavior. | [optional] 
**id** | [**LoyaltiesProgramsMembersRewardsPurchasesListRequestQueryId**](LoyaltiesProgramsMembersRewardsPurchasesListRequestQueryId.md) |  | [optional] 
**reward_id** | [**LoyaltiesProgramsMembersRewardsPurchasesListRequestQueryRewardId**](LoyaltiesProgramsMembersRewardsPurchasesListRequestQueryRewardId.md) |  | [optional] 
**card_definition_id** | [**LoyaltiesProgramsMembersRewardsPurchasesListRequestQueryCardDefinitionId**](LoyaltiesProgramsMembersRewardsPurchasesListRequestQueryCardDefinitionId.md) |  | [optional] 
**created_at** | [**TransactionFilterDateConditions**](TransactionFilterDateConditions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


