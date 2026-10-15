# CardLifetimeBucketPendingPoints

Lifetime counters of pending points. The available pending balance is max(`total` - `activated` - `canceled`, 0).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Total pending points ever added. | [optional] [default to 0]
**activated** | **float** | Total pending points activated into regular points. | [optional] [default to 0]
**canceled** | **float** | Total pending points canceled. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


