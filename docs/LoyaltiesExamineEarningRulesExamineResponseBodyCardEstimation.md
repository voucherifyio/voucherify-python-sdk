# LoyaltiesExamineEarningRulesExamineResponseBodyCardEstimation

Point estimation for a single card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**ExamineCardReference**](ExamineCardReference.md) |  | [optional] 
**points_estimation** | **float** | Total estimated points for the card across matching earning rules. | [optional] 
**earning_rules** | [**List[LoyaltiesExamineEarningRulesExamineResponseBodyCardEarningRuleEstimation]**](LoyaltiesExamineEarningRulesExamineResponseBodyCardEarningRuleEstimation.md) | Per-earning-rule estimations contributing to the total. | [optional] 
**object** | **str** | Object type marker. Always &#x60;card_estimation&#x60;. | [optional] [default to 'card_estimation']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


