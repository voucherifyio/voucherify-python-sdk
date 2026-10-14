# V2LoyaltiesProgramsMembersListRequestQuery

Request query schema for **GET** `/v2/loyalties/programs/{programId}/members`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**junction** | **str** | How multiple field filters are combined. Defaults to &#x60;AND&#x60;. | [optional] 
**id** | [**LoyaltiesProgramsMembersListRequestQueryId**](LoyaltiesProgramsMembersListRequestQueryId.md) |  | [optional] 
**status** | [**LoyaltiesProgramsMembersListRequestQueryStatus**](LoyaltiesProgramsMembersListRequestQueryStatus.md) |  | [optional] 
**customer_id** | [**LoyaltiesProgramsMembersListRequestQueryCustomerId**](LoyaltiesProgramsMembersListRequestQueryCustomerId.md) |  | [optional] 
**created_at** | [**DateFilter**](DateFilter.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


