# CardTransaction

A card transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique card transaction ID assigned by Voucherify. | [optional] 
**card_id** | **str** | ID of the card the transaction belongs to. Assigned by Voucherify. | [optional] 
**program_id** | **str** | ID of the loyalty program. Assigned by Voucherify. | [optional] 
**member_id** | **str** | ID of the member owning the card. Assigned by Voucherify. | [optional] 
**card_definition_id** | **str** | ID of the card definition of the card. Assigned by Voucherify. | [optional] 
**card_type** | **str** | Card type. | [optional] [default to 'INDIVIDUAL']
**type** | **str** | Transaction type. Options depend on the endpoint and the transaction variant. | [optional] 
**details** | **object** |  | 
**status** | **str** | Transaction processing status. Transactions are created as &#x60;PENDING&#x60; and processed asynchronously. | [optional] 
**created_at** | **datetime** | Timestamp when the transaction was created (ISO 8601). | [optional] 
**updated_at** | **datetime** | Timestamp when the transaction was last updated (ISO 8601), or &#x60;null&#x60;. | [optional] 
**object** | **str** | Object type marker, always &#x60;card_transaction&#x60;. | [optional] [default to 'card_transaction']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


