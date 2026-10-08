# MemberTierProgress

Member's tier progress on a card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **object** |  | 
**tier_structure** | **object** |  | 
**deferred** | [**List[MemberTierProgressDeferred]**](MemberTierProgressDeferred.md) | Upcoming tier assignments scheduled to start later, when the tier structure defers tier changes. The member will be assigned to the deferred tier at the start date. | [optional] 
**risks** | [**List[MemberTierProgressRisk]**](MemberTierProgressRisk.md) | Upcoming risks of losing or downgrading the current tier. | [optional] 
**opportunities** | [**List[MemberTierProgressOpportunity]**](MemberTierProgressOpportunity.md) | Opportunities to reach higher tiers. Deferred tiers are not included in this list. | [optional] 
**object** | **str** | Object type marker, always &#x60;member_tier_progress&#x60;. | [optional] [default to 'member_tier_progress']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


