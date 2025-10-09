# CampaignsSummaryGetResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object, which is &#x60;campaign_summary&#x60;. | [optional] [default to 'campaign_summary']
**campaign** | [**CampaignBase**](CampaignBase.md) |  | [optional] 
**redemptions** | **int** | Total number of redemptions, which includes successful and failed redemptions. | [optional] 
**redemptions_succeeded** | **int** | Total number of successful redemptions. | [optional] 
**redemptions_failed** | **int** | Total number of failed redemptions. | [optional] 
**rollbacks** | **int** | Total number of rollbacks, which includes successful and failed rollbacks. | [optional] 
**rollbacks_succeeded** | **int** | Total number of successful rollbacks. | [optional] 
**rollbacks_failed** | **int** | Total number of failed rollbacks. | [optional] 
**validations** | **int** | Total number of validations, which includes successful and failed validations. | [optional] 
**validations_succeeded** | **int** | Total number of successful validations. | [optional] 
**validations_failed** | **int** | Total number of failed validations. | [optional] 
**orders_amount** | **int** | Total amount of orders related to the campaign. This amount is not reduced by &#x60;orders_rolledback_amount&#x60;. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**orders_rolledback_amount** | **int** | Total amount of orders that were rolled back and are related to the campaign. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**vouchers_created** | **int** | Total number of vouchers created within the campaign. Includes vouchers generated when the campaign was created, vouchers added manually, or vouchers generated automatically when a new customer joined the campaign. | [optional] 
**vouchers_deleted** | **int** | Total number of vouchers deleted within the campaign. Includes vouchers moved to the bin and vouchers deleted permanently. Vouchers moved to the bin and then deleted permanently are counted once. | [optional] 
**publications** | **int** | Total number of publications, which includes successful and failed publications. | [optional] 
**publications_succeeded** | **int** | Total number of successful publications. | [optional] 
**publications_failed** | **int** | Total number of failed publications. | [optional] 
**discounted_amount** | **int** | Total amount of discounts related to the campaign. This amount is not reduced by the &#x60;rolledback_discounted_amount&#x60;. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**rolledback_discounted_amount** | **int** | Total amount of discounts orders that were rolled back and are related to the campaign. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**created_vouchers_amount** | **int** | The total credit amount for all created gift cards. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**amount_added** | **int** | The total credit amount that was added. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**amount_deleted** | **int** | The total credit amount that was deleted by deleting gift cards. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**amount_redeemed** | **int** | The total credit amount that was redeemed. This amount is not reduced by the &#x60;amount_rolledback&#x60;. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**amount_rolledback** | **int** | The total credit amount that was rolled back. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**amount_subtracted** | **int** | The total credit amount that was subtracted. The value is multiplied by &#x60;100&#x60; to precisely represent 2 decimal places. For example, &#x60;$10&#x60; is represented as &#x60;1000&#x60;. | [optional] 
**created_vouchers_points** | **int** | Total number of points added to newly created loyalty cards. This also counts points added for the loyalty cards which are created by importing a CSV file to a campaign. | [optional] 
**points_deleted** | **int** | Total number of points that were deleted. | [optional] 
**points_subtracted** | **int** | Total number of points that were subtracted. | [optional] 
**points_added** | **int** | Total number of points that were added. This includes points added manually or automatically by redeeming a reward that adds loyalty points to cards in this campaign. | [optional] 
**points_rewarded** | **int** | Total number of points that were rewarded to loyalty cards through earning rules. This includes pending points that were activated. | [optional] 
**points_redeemed** | **int** | Total number of points that were redeemed for rewards. | [optional] 
**points_rolledback** | **int** | Total number of points that were rolled back for reward redemptions. | [optional] 
**points_expired** | **int** | Total number of points that have expired. | [optional] 
**points_transferred_out** | **int** | Total number of points transferred out of loyalty cards covered by the campaign. | [optional] 
**points_transferred_in** | **int** | Total number of points transferred into loyalty cards covered by the campaign. | [optional] 
**pending_points_added** | **int** | Total number of pending points that were added either as part of earning rules or added manually to an existing pending point bucket. Pending points that were activated manually or automatically or that were canceled do not affect this number. | [optional] 
**pending_points_subtracted** | **int** | Total number of pending points that were subtracted from existing pending point buckets. | [optional] 
**pending_points_activated** | **int** | Total number of pending points that were activated manually or automatically. | [optional] 
**pending_points_canceled** | **int** | Total number of pending points that were canceled. | [optional] 
**referred_customers** | **int** | Total number of all referred customers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


