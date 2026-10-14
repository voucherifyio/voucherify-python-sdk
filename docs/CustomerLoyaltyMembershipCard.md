# CustomerLoyaltyMembershipCard

Loyalty card balance recorded on the customer membership.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_definition_id** | **str** | Identifies the card definition. | [optional] 
**card_id** | **str** | Identifies the loyalty card. | [optional] 
**points** | **float** | Points balance on the card. | [optional] 
**pending_points** | **float** | Pending points on the card. | [optional] 
**next_activation_at** | **date** | Date when the next points become active, in &#x60;YYYY-MM-DD&#x60; format. &#x60;null&#x60; when no activation is scheduled. | [optional] 
**next_expiration_at** | **date** | Date when the next points expire, in &#x60;YYYY-MM-DD&#x60; format. &#x60;null&#x60; when no expiration is scheduled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


