# RedemptionsRollbacksCreateRequestBody

Request body schema for **POST** `v1/redemptions/{parentRedemptionId}/rollbacks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason for the rollback. | [optional] 
**tracking_id** | **str** | Customer&#39;s &#x60;source_id&#x60;. | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**order** | [**Order**](Order.md) |  | [optional] 
**metadata** | **object** | A set of key/value pairs that you can send in the request body to update **redemption** metadata. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


