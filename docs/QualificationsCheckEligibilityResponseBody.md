# QualificationsCheckEligibilityResponseBody

Response body schema for **POST** `v1/qualifications`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeemables** | [**QualificationsRedeemables**](QualificationsRedeemables.md) |  | [optional] 
**tracking_id** | **str** | This identifier is generated during voucher qualification based on your internal id (e.g., email, database ID). This is a hashed customer source ID. | [optional] 
**order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 
**stacking_rules** | [**StackingRules**](StackingRules.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


