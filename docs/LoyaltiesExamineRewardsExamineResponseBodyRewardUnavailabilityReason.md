# LoyaltiesExamineRewardsExamineResponseBodyRewardUnavailabilityReason

Reason a reward is unavailable.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Identifies why the reward is unavailable.  - &#x60;insufficient_balance&#x60;: The source card balance is lower than the required points cost.  - &#x60;no_target_card&#x60;: The member does not have the loyalty card that would receive the points from a \&quot;points on a loyalty card\&quot; reward. | [optional] 
**details** | **object** |  | 
**object** | **str** | Object type marker. Always &#x60;reward_unavailability_reason&#x60;. | [optional] [default to 'reward_unavailability_reason']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


