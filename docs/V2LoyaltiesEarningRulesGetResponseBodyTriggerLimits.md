# V2LoyaltiesEarningRulesGetResponseBodyTriggerLimits

Cooldown and frequency limits. Always present. `cooldown` and `frequency` are always objects. `frequency.limits` is always an array and is empty when `frequency.type` is `NO_LIMIT`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | [**EarningRuleTriggerLimitsCooldown**](EarningRuleTriggerLimitsCooldown.md) |  | [optional] 
**frequency** | [**EarningRuleTriggerLimitsFrequency**](EarningRuleTriggerLimitsFrequency.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


