# LocationsGetResponseBody

Response schema for listing locations using **GET** `/v1/locations/{locationId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique location ID, assigned by the Voucherify API. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about a &#x60;location&#x60;. | [optional] [default to 'location']
**name** | **str** | Location name. | [optional] 
**shape** | [**LocationsGetResponseBodyShape**](LocationsGetResponseBodyShape.md) |  | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the location was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the location was updated. The value is shown in the ISO 8601 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


