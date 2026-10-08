# MembershipCard

A membership's loyalty card - the member's assignment to the card (`member_role`, `created_at`) combined with the card details in the `card` object and the member's tier progress on this card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_role** | **str** | Role of the member on this card. Currently, loyalty program members can have only the &#x60;OWNER&#x60; role. | [optional] 
**created_at** | **datetime** | Timestamp when the card was assigned to the member (ISO 8601). | [optional] 
**card** | **object** |  | [optional] 
**object** | **str** | Object type marker, always &#x60;member_card&#x60;. | [optional] [default to 'member_card']
**tier_progress** | [**MemberTierProgress**](MemberTierProgress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


