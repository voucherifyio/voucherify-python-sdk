# LoyaltiesMembersPendingPointsBalanceResponseBody

Response body schema for **POST** `/loyalties/members/{memberId}/pending-points/{pendingPointsId}/balance`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | The number of pending points added to or subtracted from the loyalty card. | [optional] 
**total** | **int** | Total number of pending points currently on a loyalty card. | [optional] 
**object** | **str** | The type of the object represented by JSON. Default is &#x60;balance&#x60;. | [optional] [default to 'balance']
**related_object** | [**LoyaltiesMembersPendingPointsBalanceResponseBodyRelatedObject**](LoyaltiesMembersPendingPointsBalanceResponseBodyRelatedObject.md) |  | [optional] 
**operation_type** | **str** | The type of the operation being performed. | [optional] [default to 'MANUAL']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


