# ClientRedemptionsRedeemResponseBody

Response body schema for **POST** `v1/redemptions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redemptions** | [**List[Redemption]**](Redemption.md) |  | [optional] 
**parent_redemption** | [**Redemption**](Redemption.md) |  | [optional] 
**order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 
**inapplicable_redeemables** | [**List[ValidationsRedeemableInapplicable]**](ValidationsRedeemableInapplicable.md) | Lists validation results of each inapplicable redeemable. | [optional] 
**skipped_redeemables** | [**List[ValidationsRedeemableSkipped]**](ValidationsRedeemableSkipped.md) | Lists validation results of each redeemable. If a redeemable can be applied, the API returns &#x60;\&quot;status\&quot;: \&quot;APPLICABLE\&quot;&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


