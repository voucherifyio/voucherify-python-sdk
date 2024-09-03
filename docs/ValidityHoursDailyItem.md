# ValidityHoursDailyItem

Defines the reccuring period(s) when the resource will be active.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | Defines the starting hour of validity in the HH:mm format. The resource is *inactive before* this time. | [optional] 
**days_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the resource is valid.  - &#x60;0&#x60; Sunday - &#x60;1&#x60; Monday - &#x60;2&#x60; Tuesday - &#x60;3&#x60;  Wednesday - &#x60;4&#x60; Thursday - &#x60;5&#x60; Friday - &#x60;6&#x60; Saturday | [optional] 
**expiration_time** | **str** | Defines the ending hour of validity in the HH:mm format. The resource is *inactive after* this time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


