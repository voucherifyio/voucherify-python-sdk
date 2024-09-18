# PromotionsTiersListResponseBody

Response body schema for **GET** `v1/promotions/{campaignId}/tiers` and **GET** `v1/promotions/tiers`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about promotion tiers in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of promotion tier objects. | [optional] [default to 'tiers']
**tiers** | [**List[PromotionTier]**](PromotionTier.md) | Contains array of promotion tier objects. | [optional] 
**total** | **int** | Total number of promotion tiers. | [optional] 
**has_more** | **bool** | As query results are always limited (by the limit parameter), the &#x60;has_more&#x60; flag indicates if there are more records for given filter parameters. This lets you know if you can run another request to get more records returned in the results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


