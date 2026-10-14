# LoyaltiesExamineRewardsExamineResponseBody

Response body schema for **POST** `/v2/loyalties/examine/rewards`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**ExamineCustomerReference**](ExamineCustomerReference.md) |  | 
**rewards** | [**List[LoyaltiesExamineRewardsExamineResponseBodyRewardDetail]**](LoyaltiesExamineRewardsExamineResponseBodyRewardDetail.md) | Lists rewards that resolved a points cost and appear on a returned card. Omits a reward when it is inactive, out of stock, has no matching cost, or the member has no card for that cost. | [optional] 
**memberships** | [**List[LoyaltiesExamineRewardsExamineResponseBodyMembership]**](LoyaltiesExamineRewardsExamineResponseBodyMembership.md) | Lists one entry for each active membership whose program has reward assignments. &#x60;cards&#x60; can be empty when none of those rewards resolve onto a card. | [optional] 
**object** | **str** | Object type marker. Always &#x60;rewards_examine_result&#x60;. | [optional] [default to 'rewards_examine_result']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


