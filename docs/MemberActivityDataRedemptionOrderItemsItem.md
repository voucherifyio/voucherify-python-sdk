# MemberActivityDataRedemptionOrderItemsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the order line item. | [optional] 
**object** | **str** |  | [optional] [default to 'order_item']
**source_id** | **str** | The merchant&#39;s product/SKU ID (if it is different from the Voucherify product/SKU ID). It is useful in the integration between multiple systems. It can be an ID from an eCommerce site, a database, or a third-party service. | [optional] 
**related_object** | **str** |  | [optional] 
**product_id** | **str** | Unique identifier of the product. It is assigned by Voucherify. | [optional] 
**sku_id** | **str** | Unique identifier of the SKU. It is assigned by Voucherify. | [optional] 
**quantity** | **int** | Quantity of the particular item in the cart. and The quantity of the particular item in the cart. | [optional] 
**applied_quantity** | **int** | Quantity of items changed by the application of a new quantity items. It can be positive when an item is added or negative if an item is replaced. | [optional] 
**applied_quantity_amount** | **int** | Amount for the items changed by the application of a new quantity items. It can be positive when an item is added or negative if an item is replaced. | [optional] 
**discount_quantity** | **int** | Number of discounted items. and Number of dicounted items. | [optional] 
**applied_discount_quantity** | **int** | Number of the discounted items applied in the transaction. | [optional] 
**amount** | **int** | Total amount of the order item (price * quantity). and The total amount of the order item (price * quantity). | [optional] 
**discount_amount** | **int** | Sum of all order-item-level discounts applied to the order. | [optional] 
**applied_discount_amount** | **int** | Order-level discount amount applied in the transaction. and This field shows the order-level discount applied. | [optional] 
**price** | **int** | Unit price of an item. The value is multiplied by 100 to represent 2 decimal places. For example &#x60;10000 cents&#x60; for &#x60;$100.00&#x60;. | [optional] 
**subtotal_amount** | **int** | Final order item amount after the applied item-level discount.  If there are no item-level discounts applied, this item is equal to the &#x60;amount&#x60;.    &#x60;subtotal_amount&#x60;&#x3D;&#x60;amount&#x60;-&#x60;discount_amount&#x60; and Final order item amount after the applied item-level discount.  If there are no item-level discounts applied, this item is equal to the &#x60;amount&#x60;.    &#x60;subtotal_amount&#x60;&#x3D;&#x60;amount&#x60;-&#x60;applied_discount_amount&#x60; | [optional] 
**initial_quantity** | **int** | A positive integer in the smallest unit quantity representing the total amount of the order; this is the sum of the order items&#39; quantity. | [optional] 
**initial_amount** | **int** | A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items&#39; amounts. | [optional] 
**product** | [**MemberActivityDataRedemptionOrderItemsItemProduct**](MemberActivityDataRedemptionOrderItemsItemProduct.md) |  | [optional] 
**sku** | [**MemberActivityDataRedemptionOrderItemsItemSku**](MemberActivityDataRedemptionOrderItemsItemSku.md) |  | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to an item object. It can be useful for storing additional information about the item in a structured format. It can be used to define business validation rules or discount formulas. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


