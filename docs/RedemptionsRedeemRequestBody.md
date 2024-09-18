# RedemptionsRedeemRequestBody

Response body schema for **POST** `v1/redemptions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**RedemptionsRedeemRequestBodyOptions**](RedemptionsRedeemRequestBodyOptions.md) |  | [optional] 
**redeemables** | [**List[RedemptionsRedeemRequestBodyRedeemablesItem]**](RedemptionsRedeemRequestBodyRedeemablesItem.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**session** | [**Session**](Session.md) |  | [optional] 
**tracking_id** | **str** | Is correspondent to Customer&#39;s source_id | [optional] 
**metadata** | **object** | A set of key/value pairs that you can attach to a redemption object. It can be useful for storing additional information about the redemption in a structured format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


