# V2LoyaltiesProgramsMembersBenefitsTransactionsListRequestQuery

Request query schema for **GET** `/v2/loyalties/programs/{programId}/members/{memberId}/benefits/transactions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**junction** | **str** | Defines the logical junction between field filters. Allowed values: &#x60;AND&#x60;, &#x60;OR&#x60;. Defaults to &#x60;AND&#x60;. | [optional] 
**benefit_id** | [**LoyaltiesProgramsMembersBenefitsTransactionsListRequestQueryBenefitId**](LoyaltiesProgramsMembersBenefitsTransactionsListRequestQueryBenefitId.md) |  | [optional] 
**created_at** | [**TransactionFilterDateConditions**](TransactionFilterDateConditions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


