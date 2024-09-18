# LoyaltiesMembersBalanceUpdateResponseBody

Response schema for **POST** `v1/loyalties/members/{memberId}/balance` and for **POST** `v1/loyalties/{campaignId}/members/{memberId}/balance`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | The incremental points removed or added to the current balance on the loyalty card. | [optional] 
**total** | **int** | The total of points accrued over the lifetime of the loyalty card. | [optional] 
**balance** | **int** | The balance after adding/removing points. | [optional] 
**type** | **str** | The type of voucher being modified. | [optional] 
**object** | **str** | The type of the object represented by JSON. Default is balance. | [optional] [default to 'balance']
**related_object** | [**LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject**](LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject.md) |  | [optional] 
**operation_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


