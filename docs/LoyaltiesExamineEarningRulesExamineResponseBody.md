# LoyaltiesExamineEarningRulesExamineResponseBody

Response body schema for **POST** `/v2/loyalties/examine/earning-rules`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | Examined trigger event (e.g. &#x60;customer.order.paid&#x60;, &#x60;customer.segment.entered&#x60;, &#x60;customer.custom_event&#x60;). &#x60;null&#x60; when &#x60;trigger.type&#x60; is &#x60;ALL&#x60;. | [optional] 
**customer** | [**ExamineCustomerReference**](ExamineCustomerReference.md) |  | [optional] 
**earning_rules** | [**List[LoyaltiesExamineEarningRulesExamineResponseBodyEarningRuleDetail]**](LoyaltiesExamineEarningRulesExamineResponseBodyEarningRuleDetail.md) | Lists earning rules that produced a points or benefit estimation, deduplicated across memberships. | [optional] 
**memberships** | [**List[LoyaltiesExamineEarningRulesExamineResponseBodyMembership]**](LoyaltiesExamineEarningRulesExamineResponseBodyMembership.md) | Lists one entry for each active membership whose program has earning rules for the examined trigger. Includes a card only when its estimated points are greater than 0, and a benefit only when an earning rule can grant it. Both arrays can be empty. | [optional] 
**object** | **str** | Object type marker. Always &#x60;earnings_examine_result&#x60;. | [optional] [default to 'earnings_examine_result']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


