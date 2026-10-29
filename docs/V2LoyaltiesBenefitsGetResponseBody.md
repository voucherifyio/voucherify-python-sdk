# V2LoyaltiesBenefitsGetResponseBody

Response body schema for **GET** `/v2/loyalties/benefits/{benefitId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique benefit ID, prefixed with &#x60;lben_&#x60;. | [optional] 
**name** | **str** | Benefit name, unique within the project. | [optional] 
**type** | **str** | Benefit type. | [optional] 
**status** | **str** | Current benefit status. &#x60;DELETED&#x60; appears only in the response of the delete endpoint and in activity snapshots. | [optional] 
**stock** | [**V2LoyaltiesBenefitsGetResponseBodyStock**](V2LoyaltiesBenefitsGetResponseBodyStock.md) |  | [optional] 
**points** | [**V2LoyaltiesBenefitsGetResponseBodyPoints**](V2LoyaltiesBenefitsGetResponseBodyPoints.md) |  | [optional] 
**points_proportional** | [**V2LoyaltiesBenefitsGetResponseBodyPointsProportional**](V2LoyaltiesBenefitsGetResponseBodyPointsProportional.md) |  | [optional] 
**material** | **object** |  | [optional] 
**digital** | **object** |  | [optional] 
**created_at** | **datetime** | Timestamp of when the benefit was created, in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp of the last update, in ISO 8601 format. &#x60;null&#x60; when the benefit was never updated. | [optional] 
**object** | **str** | Type of the object. Always &#x60;benefit&#x60;. | [optional] [default to 'benefit']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


