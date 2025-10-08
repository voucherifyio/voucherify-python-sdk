# SimplePromotionTier

This is an object representing a simple promotion tier. Promotion tiers are always assigned to a campaign and cannot be used standalone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique promotion tier ID. | [optional] 
**name** | **str** | Name of the promotion tier. | [optional] 
**banner** | **str** | Text to be displayed to your customers on your website. | [optional] 
**campaign** | [**SimplePromotionTierCampaign**](SimplePromotionTierCampaign.md) |  | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to a promotion tier. The metadata object stores all custom attributes assigned to the promotion tier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


