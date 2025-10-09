# MemberActivityDataRedemptionChannel

Defines the details of the channel through which the redemption was issued.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | Unique channel ID of the user performing the redemption. This is either a user ID from a user using the Voucherify Dashboard, an X-APP-Id of a user using the API, or the reward assignment ID for automatic reward redemption. | [optional] 
**channel_type** | **str** | The source of the channel for the redemption: &#x60;USER&#x60; - the redemption was made in the Voucherify Dashboard by a user,  &#x60;API&#x60; - redemption was made through the API, &#x60;AUTO_REDEEM&#x60; - the redemption was made automatically for a reward. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


