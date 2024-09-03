# LoyaltiesListMembersResponseBody

Response body schema for **GET** `v1/loyalties/{campaignId}/members`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about members in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of voucher objects. | [optional] [default to 'vouchers']
**vouchers** | [**List[LoyaltyMember]**](LoyaltyMember.md) | Contains array of voucher objects representing loyalty cards, in other words, loyalty program members. | [optional] 
**total** | **int** | Total number of voucher objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


