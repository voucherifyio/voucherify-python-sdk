# EarningRuleEffectPointsProportional

Proportional points effect - awards points using an \"every X gives Y points\" formula. Depending on `calculation_type`, one specific configuration object is required and the others must be null/absent: - `PRE_DISCOUNT_ORDER_AMOUNT`: requires `order.amount` - `POST_DISCOUNT_ORDER_AMOUNT`: requires `order.total_amount` - `ORDER_METADATA_VALUE`: requires `order.metadata` - `CUSTOMER_METADATA_VALUE`: requires `customer.metadata` - `CUSTOM_EVENT_METADATA_VALUE`: requires `custom_event.metadata` - `PRE_DISCOUNT_ORDER_ITEMS_AMOUNT`: requires `order_items.amount` - `POST_DISCOUNT_ORDER_ITEMS_AMOUNT`: requires `order_items.subtotal_amount` - `ORDER_ITEMS_QUANTITY`: requires `order_items.quantity` The trigger further restricts allowed calculation types: `customer.order.paid` allows all order/order-items types plus `CUSTOMER_METADATA_VALUE`; `customer.custom_event` allows `CUSTOMER_METADATA_VALUE` and `CUSTOM_EVENT_METADATA_VALUE`; `customer.segment.entered` allows only `CUSTOMER_METADATA_VALUE`. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculation_type** | **str** | How the proportional points are calculated. | [optional] 
**card_definition_id** | **str** | Card definition ID (&#x60;lcdef_...&#x60;) the points are awarded to. | [optional] 
**points_expiration** | [**EarningRuleEffectPointsExpiration**](EarningRuleEffectPointsExpiration.md) |  | [optional] 
**order** | [**EarningRulePointsProportionalOrder**](EarningRulePointsProportionalOrder.md) |  | [optional] 
**customer** | [**EarningRulePointsProportionalCustomer**](EarningRulePointsProportionalCustomer.md) |  | [optional] 
**custom_event** | [**EarningRulePointsProportionalCustomEvent**](EarningRulePointsProportionalCustomEvent.md) |  | [optional] 
**order_items** | [**EarningRulePointsProportionalOrderItems**](EarningRulePointsProportionalOrderItems.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


