# RedemptionsRollbacksCreateResponseBody

Response body schema for POST `/redemptions/{parentRedemptionID}/rollbacks`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rollbacks** | [**List[RedemptionRollback]**](RedemptionRollback.md) | Contains the rollback redemption objects of the particular incentives. | [optional] 
**parent_rollback** | [**RedemptionRollback**](RedemptionRollback.md) |  | [optional] 
**order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


