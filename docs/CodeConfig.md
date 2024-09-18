# CodeConfig

Contains information about the config used for the voucher code. Defines the code's pattern (prefix, postfix, length, charset, etc).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **float** | Number of characters in a generated code (excluding prefix and postfix). | [optional] 
**charset** | **str** | Characters that can appear in the code.    Examples:  - Alphanumeric: &#x60;0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&#x60;  - Alphabetic: &#x60;abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&#x60;  - Alphabetic Lowercase: &#x60;abcdefghijklmnopqrstuvwxyz&#x60;  - Alphabetic Uppercase: &#x60;ABCDEFGHIJKLMNOPQRSTUVWXYZ&#x60;  - Numbers: &#x60;0123456789&#x60;   - Custom: a custom character set | [optional] 
**prefix** | **str** | A text appended before the code. | [optional] 
**postfix** | **str** | A text appended after the code. | [optional] 
**pattern** | **str** | A pattern for codes where hashes (#) will be replaced with random characters. Overrides &#x60;length&#x60;. | [optional] 
**initial_count** | **int** | Internal value, does not change anything if provided. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


