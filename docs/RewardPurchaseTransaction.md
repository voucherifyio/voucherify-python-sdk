# RewardPurchaseTransaction

A reward transaction. Represents a reward purchase or a reward refund.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique reward transaction identifier (format &#x60;lrtx_...&#x60;). Absent for &#x60;DRY_RUN&#x60; (SIMULATED) transactions, which are never persisted. | [optional] 
**card_id** | **str** | Unique identifier of the loyalty card the points were spent from (format &#x60;lcrd_...&#x60;). | [optional] 
**card_definition_id** | **str** | Unique identifier of the card definition for that card (format &#x60;lcdef_...&#x60;). &#x60;null&#x60; when none is stored. | [optional] 
**card_transaction_id** | **str** | Unique identifier of the underlying card transaction (format &#x60;lctx_...&#x60;). &#x60;null&#x60; for &#x60;DRY_RUN&#x60; (SIMULATED) transactions. | [optional] 
**program_id** | **str** | Unique identifier of the loyalty program (format &#x60;lprg_...&#x60;). | [optional] 
**member_id** | **str** | Unique identifier of the program member (format &#x60;lmbr_...&#x60;). | [optional] 
**reward_id** | **str** | Unique identifier of the purchased reward (format &#x60;lrew_...&#x60;). | [optional] 
**status** | **str** | Transaction status:  - &#x60;PENDING&#x60;: Created and awaiting processing.  - &#x60;PROCESSING&#x60;: Being processed.  - &#x60;APPROVED&#x60;: Completed successfully.  - &#x60;REJECTED&#x60;: Rejected (see &#x60;details.rejection&#x60;).  - &#x60;SIMULATED&#x60;: Dry-run result that is not persisted.  - &#x60;REFUNDED&#x60;: Purchase has been refunded. | [optional] 
**type** | **str** | Transaction type. | [optional] 
**details** | **object** |  | [optional] 
**created_at** | **datetime** | Timestamp when the transaction was created (ISO 8601). | [optional] 
**updated_at** | **datetime** | Timestamp when the transaction was last updated (ISO 8601), or &#x60;null&#x60;. | [optional] 
**object** | **str** | Object type marker. Always &#x60;reward_transaction&#x60;. | [optional] [default to 'reward_transaction']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


