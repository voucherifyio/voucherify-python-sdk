# LoyaltiesMembersPendingPointsActivateResponseBody

Response body schema for **POST** `/loyalties/members/{memberId}/pending-points/{pendingPointsId}/activate`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | The number of pending points added to the loyalty card. | [optional] 
**total** | **int** | Total number of points incurred over the lifespan of the loyalty card, minus the expired points. | [optional] 
**balance** | **int** | The current number of loyalty points after the pendint points have been added. | [optional] 
**type** | **str** | The type of the voucher being modified. For pending points, it is always &#x60;loyalty_card&#x60;. | [optional] [default to 'loyalty_card']
**object** | **str** | The type of the object represented by JSON. Default is &#x60;balance&#x60;. | [optional] [default to 'balance']
**related_object** | [**LoyaltiesMembersPendingPointsActivateResponseBodyRelatedObject**](LoyaltiesMembersPendingPointsActivateResponseBodyRelatedObject.md) |  | [optional] 
**operation_type** | **str** | The type of the operation being performed. | [optional] [default to 'MANUAL']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


