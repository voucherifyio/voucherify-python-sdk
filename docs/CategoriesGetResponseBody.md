# CategoriesGetResponseBody

Response body schema for **GET** `v1/categories/{categoryId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique category ID assigned by Voucherify. | [optional] 
**name** | **str** | Category name. | [optional] 
**hierarchy** | **int** | Category hierarchy. Categories with lower hierarchy are processed before categories with higher hierarchy value. | [optional] 
**object** | **str** | The type of the object represented by the JSON. This object stores information about the category. | [optional] [default to 'category']
**created_at** | **datetime** | Timestamp representing the date and time when the category was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the category was updated. The value is shown in the ISO 8601 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


