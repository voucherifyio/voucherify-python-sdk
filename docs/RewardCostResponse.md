# RewardCostResponse

A reward cost. `rules` is omitted when the cost has no rule definitions; `spending` is `null` when no spending is defined. `tier_rules` is always present and defaults to `NO_REQUIREMENTS`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique cost identifier, prefixed with &#x60;lrcst_&#x60;. | [optional] 
**name** | **str** | Display name of the cost. Omitted when not set. &#x60;null&#x60; when cleared. | [optional] 
**rules** | **object** | Rules group. Contains a &#x60;logic&#x60; formula string plus numbered rule definition properties (positive-integer keys). | [optional] 
**spending** | [**List[LoyaltyV2ActivityRewardCostSpendingResponse]**](LoyaltyV2ActivityRewardCostSpendingResponse.md) | Points spending definitions, or &#x60;null&#x60; when none are defined. | [optional] 
**tier_rules** | [**RewardCostTierRulesResponse**](RewardCostTierRulesResponse.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


