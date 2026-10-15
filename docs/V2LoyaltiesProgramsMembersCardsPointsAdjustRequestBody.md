# V2LoyaltiesProgramsMembersCardsPointsAdjustRequestBody

Request body schema for **POST** `/v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/points`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | Number of points to adjust. Positive values add points (&#x60;ADMIN_CREDIT&#x60; transaction), negative values subtract points (&#x60;ADMIN_DEBIT&#x60; transaction), zero results in no transaction (&#x60;NO_CHANGE&#x60;). | [optional] 
**reason** | **str** | Optional reason for the adjustment, stored in the transaction details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


