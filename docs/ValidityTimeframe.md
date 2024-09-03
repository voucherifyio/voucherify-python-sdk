# ValidityTimeframe

Set recurrent time periods when the earning rule is valid. For example, valid for 1 hour every other day.`start_date` **required** when including the `validity_timeframe`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | Defines the amount of time an earning rule will be active in ISO 8601 format. For example, an earning rule with a &#x60;duration&#x60; of &#x60;PT1H&#x60; will be valid for a duration of one hour. | [optional] 
**interval** | **str** | Defines the intervening time between two time points in ISO 8601 format, expressed as a duration. For example, an earning rule with an &#x60;interval&#x60; of &#x60;P2D&#x60; will be valid every other day. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


