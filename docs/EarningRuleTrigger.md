# EarningRuleTrigger

Event that triggers the earning rule. Depending on `event`, either `custom_event` or `segment` is required and the other trigger contexts must be null/absent. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | Triggering event type. | [optional] 
**custom_event** | [**LoyaltyV2ActivityEarningRuleTriggerCustomEvent**](LoyaltyV2ActivityEarningRuleTriggerCustomEvent.md) |  | [optional] 
**segment** | [**LoyaltyV2ActivityEarningRuleTriggerSegment**](LoyaltyV2ActivityEarningRuleTriggerSegment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


