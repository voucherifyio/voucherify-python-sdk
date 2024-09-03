# RedemptionRewardResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**assignment_id** | **str** | Unique reward assignment ID assigned by Voucherify. | [optional] 
**voucher** | [**Voucher**](Voucher.md) |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**sku** | [**Sku**](Sku.md) |  | [optional] 
**loyalty_tier_id** | **str** | Unique loyalty tier ID assigned by Voucherify. | [optional] 
**id** | **str** | Unique reward ID. | [optional] 
**name** | **str** | Name of the reward. | [optional] 
**object** | **str** | The type of the object represented by the JSON | [optional] [default to 'reward']
**created_at** | **datetime** | Timestamp representing the date and time when the redemption was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp in ISO 8601 format indicating when the reward was updated. | [optional] 
**parameters** | [**RedemptionRewardResultParameters**](RedemptionRewardResultParameters.md) |  | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to a reward. The metadata object stores all custom attributes assigned to the reward. | [optional] 
**type** | **str** | Reward type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


