# LoyaltiesExamineEarningRulesExamineRequestBody

Request body schema for **POST** `/v2/loyalties/examine/earning-rules`.  When `trigger.type` is `SPECIFIC`, the context object matching the specific event is required and the other context objects must not be present: `customer.order.paid` > `customer_order_paid`, `customer.segment.entered` > `customer_segment_entered`, `customer.custom_event` > `customer_custom_event`. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger** | [**LoyaltiesExamineEarningRulesExamineRequestBodyTrigger**](LoyaltiesExamineEarningRulesExamineRequestBodyTrigger.md) |  | 
**customer_identification** | [**ExamineCustomerIdentification**](ExamineCustomerIdentification.md) |  | 
**customer_order_paid** | [**LoyaltiesExamineEarningRulesExamineRequestBodyCustomerOrderPaid**](LoyaltiesExamineEarningRulesExamineRequestBodyCustomerOrderPaid.md) |  | [optional] 
**customer_segment_entered** | [**LoyaltiesExamineEarningRulesExamineRequestBodyCustomerSegmentEntered**](LoyaltiesExamineEarningRulesExamineRequestBodyCustomerSegmentEntered.md) |  | [optional] 
**customer_custom_event** | [**LoyaltiesExamineEarningRulesExamineRequestBodyCustomerCustomEvent**](LoyaltiesExamineEarningRulesExamineRequestBodyCustomerCustomEvent.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


