# EarningRuleTierRules

Tier requirements for an earning. With `NO_REQUIREMENTS`, `any_of` must be null/absent. With `ANY_OF`, `any_of` is required (at least one entry) and the member must be in any of the listed tiers to earn. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Tier requirement type. | [optional] 
**any_of** | [**List[LoyaltyV2ActivityEarningRuleTierRulesAnyOfEntry]**](LoyaltyV2ActivityEarningRuleTierRulesAnyOfEntry.md) | Tier structure/tier combinations, any of which satisfies the requirement. Can be &#x60;null&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


