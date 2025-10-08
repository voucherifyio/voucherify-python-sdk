# MemberActivityDataRedemptionOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**status** | **str** | The order status. | [optional] 
**customer_id** | **str** | Unique customer identifier of the customer making the purchase. The ID is assigned by Voucherify. | [optional] 
**referrer_id** | **str** |  | [optional] 
**amount** | **int** | A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items&#39; amounts. and This is the sum of the order items&#39; amounts. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). | [optional] 
**discount_amount** | **int** | Sum of all order-level discounts applied to the order. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). | [optional] 
**applied_discount_amount** | **int** | This field shows the order-level discount applied. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). | [optional] 
**items_discount_amount** | **int** | Sum of all product-specific discounts applied to the order.  It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). and Sum of all product-specific discounts applied to the order. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). | [optional] 
**items_applied_discount_amount** | **int** | Sum of all product-specific discounts applied in a particular request. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00).   &#x60;sum(items, i &#x3D;&gt; i.applied_discount_amount)&#x60; | [optional] 
**total_discount_amount** | **int** | Sum of all order-level AND all product-specific discounts applied to the order. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). | [optional] 
**total_applied_discount_amount** | **int** | Sum of all order-level AND all product-specific discounts applied in a particular request. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). &#x60;total_applied_discount_amount&#x60; &#x3D; &#x60;applied_discount_amount&#x60; + &#x60;items_applied_discount_amount&#x60; and Sum of all order-level AND all product-specific discounts applied in a particular request. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00).   &#x60;total_applied_discount_amount&#x60; &#x3D; &#x60;applied_discount_amount&#x60; + &#x60;items_applied_discount_amount&#x60; | [optional] 
**total_amount** | **int** | Order amount after undoing all the discounts through the rollback redemption. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). | [optional] 
**items** | [**List[MemberActivityDataRedemptionOrderItemsItem]**](MemberActivityDataRedemptionOrderItemsItem.md) | Array of items applied to the order. It can include up to 500 items. | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to an order. It can be useful for storing additional information about the order in a structured format. It can be used to define business validation rules or discount formulas. | [optional] 
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'order']
**initial_amount** | **int** | This is the sum of the order items&#39; amounts before any discount or other effect (e.g. add missing units) is applied. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the order was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the order was last updated in ISO 8601 format. | [optional] 
**customer** | [**MemberActivityDataRedemptionOrderCustomer**](MemberActivityDataRedemptionOrderCustomer.md) |  | [optional] 
**referrer** | [**MemberActivityDataRedemptionOrderReferrer**](MemberActivityDataRedemptionOrderReferrer.md) |  | [optional] 
**redemptions** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


