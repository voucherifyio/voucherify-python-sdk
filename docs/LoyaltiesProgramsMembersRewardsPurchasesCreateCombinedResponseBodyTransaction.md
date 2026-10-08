# LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBodyTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** |  | [optional] 
**card_definition_id** | **str** | Unique identifier of the card definition for that card (format &#x60;lcdef_...&#x60;). | [optional] 
**card_transaction_id** | **object** | &#x60;null&#x60; for &#x60;DRY_RUN&#x60; (SIMULATED) transactions. | [optional] 
**program_id** | **str** | Unique identifier of the loyalty program (format &#x60;lprg_...&#x60;). | [optional] 
**member_id** | **str** | Unique identifier of the program member (format &#x60;lmbr_...&#x60;). | [optional] 
**reward_id** | **str** | Unique identifier of the purchased reward (format &#x60;lrew_...&#x60;). | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'PURCHASE']
**details** | [**LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBodyTransactionDetails**](LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBodyTransactionDetails.md) |  | [optional] 
**updated_at** | **object** | For &#x60;DRY_RUN&#x60; transactions, this is always &#x60;null&#x60;. | [optional] 
**object** | **str** | Object type marker. Always &#x60;reward_transaction&#x60;. | [optional] [default to 'reward_transaction']
**id** | **str** | Unique reward transaction identifier (format &#x60;lrtx_...&#x60;). | [optional] 
**created_at** | **datetime** | Timestamp when the transaction was created (ISO 8601). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


