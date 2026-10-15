# LoyaltiesExamineRewardsExamineResponseBodyCardRewardEstimation

Reward availability estimation for a card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward** | [**LoyaltiesExamineRewardsExamineResponseBodyRewardReference**](LoyaltiesExamineRewardsExamineResponseBodyRewardReference.md) |  | 
**status** | **str** | Whether the reward can currently be obtained with this card. | [optional] 
**cost** | [**LoyaltiesExamineRewardsExamineResponseBodyRewardCost**](LoyaltiesExamineRewardsExamineResponseBodyRewardCost.md) |  | 
**unavailability_reasons** | [**List[LoyaltiesExamineRewardsExamineResponseBodyRewardUnavailabilityReason]**](LoyaltiesExamineRewardsExamineResponseBodyRewardUnavailabilityReason.md) | Reasons the reward is unavailable. Absent when the reward is available. | [optional] 
**object** | **str** | Object type marker. Always &#x60;reward_estimation&#x60;. | [optional] [default to 'reward_estimation']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


