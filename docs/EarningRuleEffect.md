# EarningRuleEffect

Effect applied when an earning is triggered. Depending on `type`, exactly one of `points`, `points_proportional` or `benefit` is required and the others must be null/absent. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Effect type. | [optional] 
**points** | [**EarningRuleEffectPoints**](EarningRuleEffectPoints.md) |  | [optional] 
**points_proportional** | [**EarningRuleEffectPointsProportional**](EarningRuleEffectPointsProportional.md) |  | [optional] 
**benefit** | [**LoyaltyV2ActivityEarningRuleEffectBenefit**](LoyaltyV2ActivityEarningRuleEffectBenefit.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


