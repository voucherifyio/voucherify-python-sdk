# RedeemableHolder

Single customer's redeemable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the redeemable holder. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the redeemable was assigned. The value is shown in the ISO 8601 format. | [optional] 
**redeemable_id** | **str** | Identifier of the redeemable item. | [optional] 
**redeemable_object** | **str** | Type of the redeemable. | [optional] 
**customer_id** | **str** | Unique identifier of the customer. | [optional] 
**holder_role** | **str** | Role of the holder. | [optional] 
**campaign_id** | **str** | Unique identifier of the campaign as assigned by Voucherify. | [optional] 
**campaign_type** | **str** | Defines the type of the campaign. | [optional] [default to 'REFERRAL_PROGRAM']
**voucher_type** | **str** | Defines the type of the voucher. | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to a redeemable holder. The metadata object stores all custom attributes assigned to the &#x60;redeemable_holder&#x60; object. | [optional] 
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'redeemable_holder']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


