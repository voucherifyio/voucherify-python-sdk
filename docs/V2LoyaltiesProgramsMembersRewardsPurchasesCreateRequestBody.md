# V2LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody

Request body schema for **POST** `/v2/loyalties/programs/{programId}/members/{memberId}/rewards/purchases`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward_id** | **str** | Unique identifier of the reward to purchase (format &#x60;lrew_...&#x60;). | [optional] 
**mode** | **str** | Purchase mode. &#x60;TRANSACTION&#x60; creates a &#x60;PENDING&#x60; reward transaction processed asynchronously (HTTP &#x60;202&#x60;). &#x60;DRY_RUN&#x60; only simulates the purchase and returns the calculation result (HTTP &#x60;200&#x60;); no transaction is created. Defaults to &#x60;TRANSACTION&#x60; when omitted. | [optional] [default to 'TRANSACTION']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


