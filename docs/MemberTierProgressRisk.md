# MemberTierProgressRisk

A risk of losing or downgrading the current tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Risk type - &#x60;TIER_DOWNGRADE&#x60; when the member would fall to a lower tier, &#x60;TIER_LEFT&#x60; when the member would leave the tier structure entirely. | [optional] 
**var_date** | **datetime** | Date when the risk materializes (ISO 8601), or &#x60;null&#x60;. | [optional] 
**tier** | [**MemberTierProgressTier**](MemberTierProgressTier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


