# ValidationsRedeemableSkipped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Indicates whether the redeemable can be applied or not applied based on the validation rules. | [optional] [default to 'SKIPPED']
**id** | **str** | Redeemable ID, i.e. the voucher code. | [optional] 
**object** | **str** | Redeemable&#39;s object type. | [optional] 
**result** | [**ValidationsRedeemableSkippedResult**](ValidationsRedeemableSkippedResult.md) |  | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes in the form of key/value pairs assigned to the redeemable. | [optional] 
**categories** | [**List[CategoryWithStackingRulesType]**](CategoryWithStackingRulesType.md) |  | [optional] 
**campaign_name** | **str** | Campaign name. Displayed only if the &#x60;options.expand&#x60; is passed with a &#x60;redeemable&#x60; value in the validation request body. | [optional] 
**campaign_id** | **str** | Unique campaign ID assigned by Voucherify. Displayed only if the &#x60;options.expand&#x60; is passed with a &#x60;redeemable&#x60; value in the validation request body. | [optional] 
**name** | **str** | Name of the promotion tier. Displayed only if the &#x60;options.expand&#x60; is passed with a &#x60;redeemable&#x60; value in the validation request body. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


