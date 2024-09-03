# PromotionsStacksCreateResponseBody

Response body schema for **POST** `v1/promotions/{campaignId}/stacks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Promotion stack name. | [optional] 
**tiers** | [**PromotionsStacksCreateResponseBodyTiers**](PromotionsStacksCreateResponseBodyTiers.md) |  | [optional] 
**id** | **str** | Unique promotion stack ID. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the promotion stack was created. The value is shown in the ISO 8601 format. | [optional] 
**campaign_id** | **str** | Promotion stack&#39;s parent campaign&#39;s unique ID. | [optional] 
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'promotion_stack']
**category_id** | **str** | Promotion stack category ID. | [optional] 
**categories** | [**List[PromotionStackBase]**](PromotionStackBase.md) | Details about the category assigned to the promotion stack. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


