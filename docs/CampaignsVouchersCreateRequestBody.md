# CampaignsVouchersCreateRequestBody

Request body schema for **POST** `v1/campaigns/{campaignId}/vouchers/{code}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category assigned to the campaign. Either pass this parameter OR the &#x60;category_id&#x60;. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the voucher. A set of key/value pairs that you can attach to a voucher object. It can be useful for storing additional information about the voucher in a structured format. | [optional] 
**redemption** | [**CampaignsVouchersCreateRequestBodyRedemption**](CampaignsVouchersCreateRequestBodyRedemption.md) |  | [optional] 
**additional_info** | **str** | An optional field to keep any extra textual information about the code such as a code description and details. | [optional] 
**start_date** | **datetime** | Activation timestamp defines when the voucher starts to be active in ISO 8601 format. Voucher is *inactive before* this date.  | [optional] 
**expiration_date** | **datetime** | Expiration timestamp defines when the voucher expires in ISO 8601 format.  Voucher is *inactive after* this date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


