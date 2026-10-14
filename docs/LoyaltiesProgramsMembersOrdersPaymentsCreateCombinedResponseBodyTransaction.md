# LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBodyTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **str** | Unique identifier of the loyalty program (format &#x60;lprg_...&#x60;). | [optional] 
**member_id** | **str** | Unique identifier of the program member (format &#x60;lmbr_...&#x60;). | [optional] 
**card_id** | **str** | Unique identifier of the loyalty card the points were spent from (format &#x60;lcrd_...&#x60;). | [optional] 
**card_definition_id** | **str** | Identifies the card definition (format &#x60;lcdef_...&#x60;). | [optional] 
**card_transaction_id** | **object** | &#x60;null&#x60; for &#x60;DRY_RUN&#x60; (&#x60;SIMULATED&#x60;) transactions. | [optional] 
**order_id** | **str** | Identifies the paid order (format &#x60;ord_...&#x60;). | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** | Defines the transaction type. Always &#x60;PAY_WITH_POINTS&#x60;. | [optional] [default to 'PAY_WITH_POINTS']
**details** | [**LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBodyTransactionDetails**](LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBodyTransactionDetails.md) |  | [optional] 
**updated_at** | **object** | Timestamp when the transaction was last updated (ISO 8601), or &#x60;null&#x60; for &#x60;DRY_RUN&#x60; (&#x60;SIMULATED&#x60;) transactions. | [optional] 
**object** | **str** | Object type marker. Always &#x60;order_transaction&#x60;. | [optional] [default to 'order_transaction']
**created_at** | **datetime** | Timestamp when the transaction was created (ISO 8601). | [optional] 
**id** | **str** | Identifies the order transaction (&#x60;lotx_...&#x60;). Absent on dry-run (&#x60;SIMULATED&#x60;) create responses, which are never persisted. Always present in list responses. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


