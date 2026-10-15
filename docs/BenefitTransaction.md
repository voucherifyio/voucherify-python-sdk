# BenefitTransaction

A benefit transaction. Represents a benefit fulfillment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **str** | Unique identifier of the loyalty program (format &#x60;lprg_...&#x60;). | [optional] 
**member_id** | **str** | Unique identifier of the program member (format &#x60;lmbr_...&#x60;). | [optional] 
**created_at** | **datetime** | Timestamp when the transaction was created (ISO 8601). | [optional] 
**updated_at** | **datetime** | Timestamp when the transaction was last updated (ISO 8601), or &#x60;null&#x60;. | [optional] 
**id** | **str** | Unique benefit transaction identifier (format &#x60;lbtx_...&#x60;). | [optional] 
**benefit_id** | **str** | Unique identifier of the fulfilled benefit (format &#x60;lben_...&#x60;). | [optional] 
**earning_rule_id** | **str** | Unique identifier of the earning rule that triggered the fulfillment (format &#x60;lern_...&#x60;). | [optional] 
**type** | **str** | Transaction type. Always &#x60;FULFILLMENT&#x60;. | [optional] [default to 'FULFILLMENT']
**details** | [**BenefitTransactionDetails**](BenefitTransactionDetails.md) |  | [optional] 
**status** | **str** | Transaction status. &#x60;PENDING&#x60; - created, awaiting processing; &#x60;APPROVED&#x60; - completed successfully; &#x60;REJECTED&#x60; - rejected (see &#x60;details.rejection&#x60;). | [optional] 
**object** | **str** | Object type marker. Always &#x60;benefit_transaction&#x60;. | [optional] [default to 'benefit_transaction']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


