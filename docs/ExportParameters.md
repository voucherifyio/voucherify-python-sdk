# ExportParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** |  | [optional] 
**fields** | **List[str]** | Array of strings containing the data in the export. These fields define the headers in the CSV file. and Array of strings containing the data in the export. These fields define the headers in the CSV file. The &#x60;metadata&#x60; field expands into one CSV column per metadata property. You can also pass specific properties as &#x60;metadata.&lt;property_name&gt;&#x60;. | [optional] 
**filters** | **object** | Allowed additional properties must start with \&quot;metadata.\&quot; or \&quot;redemption.\&quot; and Allowed additional properties must start with \&quot;metadata.\&quot; and Allowed additional properties must start with \&quot;metadata.\&quot; or \&quot;address.\&quot; or \&quot;summary.\&quot; or \&quot;loyalty.\&quot; or \&quot;loyalty_tier.\&quot; or \&quot;loyalty_points.\&quot; or \&quot;system_metadata.\&quot; and Allowed additional properties must start with \&quot;metadata.\&quot; or \&quot;attributes.\&quot; | [optional] 
**campaign_id** | **str** | Unique identifier of the campaign. It is assigned by Voucherify. The campaign ID defines the campaign for which the voucher export will be triggered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


