# LoyaltiesExamineRewardsExamineResponseBodyMembership

Reward opportunities for one program membership.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**ExamineMemberReference**](ExamineMemberReference.md) |  | 
**program** | [**ExamineProgramReference**](ExamineProgramReference.md) |  | 
**cards** | [**List[LoyaltiesExamineRewardsExamineResponseBodyCardEstimation]**](LoyaltiesExamineRewardsExamineResponseBodyCardEstimation.md) | Lists cards that have at least one reward with a resolved points cost. Can be empty. | [optional] 
**object** | **str** | Object type marker. Always &#x60;member_rewards_opportunity&#x60;. | [optional] [default to 'member_rewards_opportunity']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


