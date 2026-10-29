# LoyaltiesExamineEarningRulesExamineRequestBodyCustomerCustomEvent

Context for examining `customer.custom_event` earning rules. With `type` = `ALL`, `all` is required and `specific` must be `null`/absent. With `SPECIFIC`, `specific` is required and `all` must be null/absent. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Whether to examine all custom events or one specific event. | [optional] 
**all** | [**LoyaltiesExamineEarningRulesExamineRequestBodyCustomerCustomEventAll**](LoyaltiesExamineEarningRulesExamineRequestBodyCustomerCustomEventAll.md) |  | [optional] 
**specific** | [**LoyaltiesExamineEarningRulesExamineRequestBodyCustomerCustomEventSpecific**](LoyaltiesExamineEarningRulesExamineRequestBodyCustomerCustomEventSpecific.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


