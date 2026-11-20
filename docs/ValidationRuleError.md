# ValidationRuleError

Defines the custom error returned when validation or redemption fails this rule. Use legacy `message`, `mode: MESSAGES` with per-language `messages`, or `mode: LIBRARY` with a library `key`. `MESSAGES` and `LIBRARY` are mutually exclusive. At validation or redemption time the API resolves this object to a single `{ message }` using `options.language`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Legacy single-language error message. Used when &#x60;mode&#x60; is omitted. In &#x60;MESSAGES&#x60; mode, used when neither the requested language nor the default language has a translation. | [optional] 
**mode** | **str** | Selects how the custom error is defined. &#x60;MESSAGES&#x60; stores per-language text in &#x60;messages&#x60;. &#x60;LIBRARY&#x60; references an Error Message Library entry in &#x60;library&#x60;. Omit &#x60;mode&#x60; to use the legacy &#x60;message&#x60; field only. | [optional] 
**messages** | **object** | Per-language custom messages keyed by language code (&#x60;en&#x60;, &#x60;pl&#x60;, &#x60;en-US&#x60;). Required when &#x60;mode&#x60; is &#x60;MESSAGES&#x60;. Must be omitted or &#x60;null&#x60; when &#x60;mode&#x60; is &#x60;LIBRARY&#x60;. | [optional] 
**library** | [**ValidationRuleErrorLibrary**](ValidationRuleErrorLibrary.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


