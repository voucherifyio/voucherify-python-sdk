# MemberCreate

Fields for creating one loyalty program member. No additional properties are allowed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_identification** | **object** |  | 
**status** | **str** | Sets the initial member status. Allowed values are &#x60;ACTIVE&#x60; and &#x60;INACTIVE&#x60;. Defaults to &#x60;ACTIVE&#x60; when omitted or &#x60;null&#x60;. | [optional] 
**metadata** | **object** | Stores custom metadata on the member. Validated against the metadata schema for the &#x60;vl_member&#x60; related object when one is configured. Defaults to an empty object when omitted or &#x60;null&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


