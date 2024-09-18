# ClientValidationsValidateResponseBody

Response body schema for POST `/validations`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | The result of the validation. It takes all of the redeemables into account and returns a &#x60;false&#x60; if at least one redeemable is inapplicable. Returns &#x60;true&#x60; if all redeemables are applicable. | [optional] 
**redeemables** | [**List[ClientValidationsValidateResponseBodyRedeemablesItem]**](ClientValidationsValidateResponseBodyRedeemablesItem.md) |  | [optional] 
**skipped_redeemables** | [**List[ValidationsRedeemableSkipped]**](ValidationsRedeemableSkipped.md) | Lists validation results of each skipped redeemable. | [optional] 
**inapplicable_redeemables** | [**List[ValidationsRedeemableInapplicable]**](ValidationsRedeemableInapplicable.md) | Lists validation results of each inapplicable redeemable. | [optional] 
**order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 
**tracking_id** | **str** | Hashed customer source ID. | [optional] 
**session** | [**Session**](Session.md) |  | [optional] 
**stacking_rules** | [**StackingRules**](StackingRules.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


