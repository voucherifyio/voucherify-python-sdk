# V2LoyaltiesProgramsMembersCardsPendingPointsCancelResponseBody

Response body schema for **POST** `/v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/pending-points/{bucketId}/cancel`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**CardTransaction**](CardTransaction.md) |  | 
**status** | **str** | Result status. The API endpoint returns &#x60;TRANSACTION_CREATED&#x60;. | [optional] [default to 'TRANSACTION_CREATED']
**message** | **str** | Human-readable result message - \&quot;Points cancellation transaction created\&quot;. | [optional] [default to 'Points cancellation transaction created']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


