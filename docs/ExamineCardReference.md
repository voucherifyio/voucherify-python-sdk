# ExamineCardReference

Card reference in examine results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique card ID (&#x60;lcrd_...&#x60;). | [optional] 
**card_definition_id** | **str** | Unique card definition ID (&#x60;lcdef_...&#x60;). | [optional] 
**card_type** | **str** | Card type. Currently only &#x60;INDIVIDUAL&#x60; exists. | [optional] [default to 'INDIVIDUAL']
**code** | **str** | Card code. May be &#x60;null&#x60; right after member creation because card codes are generated asynchronously. | [optional] 
**object** | **str** | Object type marker. Always &#x60;card&#x60;. | [optional] [default to 'card']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


