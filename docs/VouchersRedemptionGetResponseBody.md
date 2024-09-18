# VouchersRedemptionGetResponseBody

Response body schema for **GET** `v1/vouchers/{code}/redemption`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The maximum number of times a voucher can be redeemed. | [optional] 
**redeemed_quantity** | **int** | The number of times the voucher was redeemed successfully. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about redemptions in a dictionary. | [optional] [default to 'list']
**url** | **str** | URL | [optional] 
**data_ref** | **str** | Identifies the name of the attribute that contains the array of &#x60;redemption_entries&#x60;. | [optional] [default to 'redemption_entries']
**total** | **int** | Total number of redemption objects. | [optional] 
**redemption_entries** | [**List[RedemptionEntry]**](RedemptionEntry.md) | Contains the array of successful and failed redemption objects. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


