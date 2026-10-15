# V2LoyaltiesProgramsMembershipsGetResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/memberships/{customerId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**Member**](Member.md) |  | [optional] 
**program** | [**ProgramSimple**](ProgramSimple.md) |  | [optional] 
**object** | **str** | Object type marker, always &#x60;membership&#x60;. | [optional] [default to 'membership']
**cards** | [**List[MembershipCard]**](MembershipCard.md) | Member&#39;s loyalty cards, one per card definition assigned to the program. &#x60;tier_progress&#x60; is present when that card definition has a tier structure and the member has a tier on the card. Otherwise it is omitted. &#x60;card.code&#x60; can be &#x60;null&#x60; right after member creation, while code generation is still running. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


