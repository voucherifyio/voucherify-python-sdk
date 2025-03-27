# LoyaltyPendingPointsDetailsEvent

Details about the event that created pending points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique event identifier, assigned by Voucherify. | [optional] 
**type** | **str** | Type of the event that triggered the creation of pending points. | [optional] [default to 'customer.order.paid']
**group_id** | **str** | Unique identifier of the request that triggered the event, assigned by Voucherify. | [optional] 
**entity_id** | **str** | Unique identifier of the entity that triggered the event, assigned by Voucherify. For pending points, it is the &#x60;customer_id&#x60; of the customer who paid for the order. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the event occurred. The value is shown in the ISO 8601 format. | [optional] 
**category** | **str** | Type of the event. | [optional] 
**event_source** | [**EventSource**](EventSource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


