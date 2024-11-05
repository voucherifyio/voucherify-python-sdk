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
**campaign_name** | **str** | Campaign name | [optional] 
**campaign_id** | **str** | Unique campaign ID assigned by Voucherify. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


