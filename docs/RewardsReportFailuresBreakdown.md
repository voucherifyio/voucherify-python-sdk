# RewardsReportFailuresBreakdown

Counts failed reward purchase attempts by reason. A reason is present only when it was recorded. Empty when no failures were recorded. Keys can also be a card-transaction rejection reason or a publication error key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | **float** | Counts failures caused by the cooldown limit. | [optional] 
**frequency** | **float** | Counts failures caused by the frequency limit. | [optional] 
**out_of_stock** | **float** | Counts failures caused by missing stock. | [optional] 
**reward_not_found** | **float** | Counts failures caused by a missing reward. | [optional] 
**reward_not_active** | **float** | Counts failures caused by an inactive reward. | [optional] 
**program_not_found** | **float** | Counts failures caused by a missing program. | [optional] 
**member_not_found** | **float** | Counts failures caused by a missing member. | [optional] 
**member_not_active** | **float** | Counts failures caused by an inactive member. | [optional] 
**publication_failed** | **float** | Counts failures caused by a failed voucher publication. | [optional] 
**target_card_not_found** | **float** | Counts failures caused by a missing target card. | [optional] 
**points_purchase_failed** | **float** | Counts failures caused by a failed points purchase. | [optional] 
**unexpected_error** | **float** | Counts failures caused by an unexpected error. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


