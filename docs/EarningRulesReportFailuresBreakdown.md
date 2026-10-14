# EarningRulesReportFailuresBreakdown

Counts failed trigger-limit checks by reason. `COOLDOWN` and `FREQUENCY` are the only keys. Either key may be absent. A present key is `0` when that reason has no failures. The object is empty when no failure counts are stored yet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cooldown** | **float** | Counts failures caused by the cooldown limit. | [optional] 
**frequency** | **float** | Counts failures caused by the frequency limit. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


