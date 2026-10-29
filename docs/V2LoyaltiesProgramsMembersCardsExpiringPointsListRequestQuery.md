# V2LoyaltiesProgramsMembersCardsExpiringPointsListRequestQuery

Request query schema for **GET** `/v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/expiring-points`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**junction** | **str** | Joins the field filters. Allowed values are &#x60;AND&#x60; and &#x60;OR&#x60;. Defaults to &#x60;AND&#x60;. | [optional] 
**card_definition_id** | [**CardDefinitionIdFilterConditions**](CardDefinitionIdFilterConditions.md) |  | [optional] 
**expiration_date** | [**DateFilter**](DateFilter.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


