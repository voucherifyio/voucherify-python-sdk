# voucherify.LV2ProgramsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_create_program_members**](LV2ProgramsApi.md#batch_create_program_members) | **POST** /v2/loyalties/programs/{programId}/members/batch | Batch create program members
[**create_member_order_payment**](LV2ProgramsApi.md#create_member_order_payment) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/orders/payments | Pay for order with points
[**create_program_member**](LV2ProgramsApi.md#create_program_member) | **POST** /v2/loyalties/programs/{programId}/members | Create program member
[**get_program_member**](LV2ProgramsApi.md#get_program_member) | **GET** /v2/loyalties/programs/{programId}/members/{memberId} | Get program member
[**get_program_membership**](LV2ProgramsApi.md#get_program_membership) | **GET** /v2/loyalties/programs/{programId}/memberships/{customerId} | Get program membership
[**list_card_transactions**](LV2ProgramsApi.md#list_card_transactions) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/transactions | List card transactions
[**list_member_order_payments**](LV2ProgramsApi.md#list_member_order_payments) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/orders/payments | List member order payments
[**list_member_reward_purchases**](LV2ProgramsApi.md#list_member_reward_purchases) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/rewards/purchases | List member reward purchases
[**purchase_member_reward**](LV2ProgramsApi.md#purchase_member_reward) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/rewards/purchases | Purchase reward with points


# **batch_create_program_members**
> LoyaltiesProgramsMembersCreateInBulkResponseBody batch_create_program_members(program_id, member_create=member_create)

Batch create program members

Schedules creation of program members from a JSON array and returns 202 with async_action_id. The program must exist, be ACTIVE, and be inside its validity window. The body isnt checked before that response. Entries are processed in batches of 100. The raw body must be at most 10 MB. Each entry uses the same fields as [Create program member](/api-reference/programs/create-program-member). A failed entry is skipped. Its report row sets created to false and explains the failure in error. Skipped cases include an invalid customer_identification, an unknown customer, an invalid status, a duplicate customer in the batch (Duplicate customer ID), a customer who is already a member (Member already exists), metadata that doesnt match the vl_member schema, and entries past the loyalty members plan limit. Successful entries enroll the customer and create a loyalty card for each card definition on the program. Report columns are identification_type, customer_id, customer_source_id, program_id, member_id, created, and error. An empty array or a null entry fails the async action with invalid_request_payload. A body that isnt a JSON array fails it with top_level_object_should_be_an_array. Use [Get async action](/api-reference/async-actions/get-async-action) to read the status and the report. You can also open the result from Audit log, [Background tasks](/analyze/audit-logs#background-tasks).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_create_in_bulk_response_body import LoyaltiesProgramsMembersCreateInBulkResponseBody
from voucherify.models.member_create import MemberCreate
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Unique loyalty program ID (format lprg_[a-f0-9]+).
    member_create = [{"customer_identification":{"type":"customer_id","customer_id":"cust_X07elh40iNWLujRmDNmBufxd"}},{"customer_identification":{"type":"customer_source_id","customer_source_id":"crm-1001"},"status":"ACTIVE"}] # List[MemberCreate] |  (optional)

    try:
        # Batch create program members
        api_response = api_instance.batch_create_program_members(program_id, member_create=member_create)
        print("The response of LV2ProgramsApi->batch_create_program_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->batch_create_program_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Unique loyalty program ID (format lprg_[a-f0-9]+). | 
 **member_create** | [**List[MemberCreate]**](MemberCreate.md)|  | [optional] 

### Return type

[**LoyaltiesProgramsMembersCreateInBulkResponseBody**](LoyaltiesProgramsMembersCreateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The batch is scheduled. Use &#x60;async_action_id&#x60; to follow processing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_member_order_payment**
> LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBody create_member_order_payment(program_id, member_id, loyalties_programs_members_orders_payments_create_request_body=loyalties_programs_members_orders_payments_create_request_body)

Pay for order with points

Pays for an order with points from the members card. The amount and points come from the card definitions pay-with-points exchange ratio, limited by the order total, the card balance, card spending caps, and the optional payment_limit. The binding cap is returned as details.spending_cap. The program and member must be ACTIVE, and the program must be inside its validity window. The card must belong to the member. The card definition must have pay-with-points enabled and an exchange-ratio formula. The order must already exist, identified by id or source_id. Modes: - TRANSACTION (default): creates a PENDING order transaction and a PENDING card transaction. Returns 202. The same order can be paid again; each call creates a new transaction. - DRY_RUN: simulates the payment and doesnt create a transaction. Returns 200 with status SIMULATED.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_orders_payments_create_combined_response_body import LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBody
from voucherify.models.loyalties_programs_members_orders_payments_create_request_body import LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program (lprg_ followed by hexadecimal characters).
    member_id = 'member_id_example' # str | Identifies the program member (lmbr_[a-f0-9]+).
    loyalties_programs_members_orders_payments_create_request_body = {"payment_limit":{"type":"CARD_BALANCE"},"mode":"TRANSACTION","card_id":"lcrd_128f962dbd8c4ba5e1","order":{"id":"ord_12b4cdf5f30c158825"}} # LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody |  (optional)

    try:
        # Pay for order with points
        api_response = api_instance.create_member_order_payment(program_id, member_id, loyalties_programs_members_orders_payments_create_request_body=loyalties_programs_members_orders_payments_create_request_body)
        print("The response of LV2ProgramsApi->create_member_order_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->create_member_order_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program (lprg_ followed by hexadecimal characters). | 
 **member_id** | **str**| Identifies the program member (lmbr_[a-f0-9]+). | 
 **loyalties_programs_members_orders_payments_create_request_body** | [**LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody**](LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody.md)|  | [optional] 

### Return type

[**LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBody**](LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Dry run result (mode &#x60;DRY_RUN&#x60;). No transaction was created; the returned transaction has status &#x60;SIMULATED&#x60; and no &#x60;id&#x60;. and Payment accepted (mode &#x60;TRANSACTION&#x60;). A &#x60;PENDING&#x60; order transaction was created and will be processed asynchronously. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_program_member**
> LoyaltiesProgramsMembersCreateResponseBody create_program_member(program_id, loyalties_programs_members_create_request_body=loyalties_programs_members_create_request_body)

Create program member

Enrolls an existing customer as a member of the loyalty program and creates a loyalty card for each card definition assigned to the program. Card code generation is asynchronous, so code can be null right after creation. The program must be ACTIVE and inside its validity window, and the customer must already exist. A customer can be a member of a program only once. Identify the customer with customer_identification. status defaults to ACTIVE.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_create_request_body import LoyaltiesProgramsMembersCreateRequestBody
from voucherify.models.loyalties_programs_members_create_response_body import LoyaltiesProgramsMembersCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Unique loyalty program ID (format lprg_[a-f0-9]+).
    loyalties_programs_members_create_request_body = {"customer_identification":{"type":"customer_id","customer_id":"cust_X07elh40iNWLujRmDNmBufxd"}} # LoyaltiesProgramsMembersCreateRequestBody |  (optional)

    try:
        # Create program member
        api_response = api_instance.create_program_member(program_id, loyalties_programs_members_create_request_body=loyalties_programs_members_create_request_body)
        print("The response of LV2ProgramsApi->create_program_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->create_program_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Unique loyalty program ID (format lprg_[a-f0-9]+). | 
 **loyalties_programs_members_create_request_body** | [**LoyaltiesProgramsMembersCreateRequestBody**](LoyaltiesProgramsMembersCreateRequestBody.md)|  | [optional] 

### Return type

[**LoyaltiesProgramsMembersCreateResponseBody**](LoyaltiesProgramsMembersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The created member with its automatically created cards. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_program_member**
> MemberWithCards get_program_member(program_id, member_id)

Get program member

 <Info> <Badge color gray>Documentation in progress</Badge> This documentation is in progress. The parameters, fields, request and response bodies, and other data may be subject to change. If you need more information or you want to share feedback, contact [Voucherify support](https://www.voucherify.io/contact-support) or your Technical Account Manager. </Info> Returns one member of the program together with that members loyalty cards. Each card includes balance, lifetime_bucket, next_expiration, and next_activation. tier_progress is not included. Use [Get program membership](/api-reference/programs/get-program-membership) when you need tier progress. card.code can be null shortly after member creation, while code generation is still running. Returns 404 when the program doesnt exist, or when the member doesnt exist in that program. The program is checked first.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.member_with_cards import MemberWithCards
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Unique loyalty program ID (format lprg_[a-f0-9]+).
    member_id = 'member_id_example' # str | Program member ID (format lmbr_[a-f0-9]+).

    try:
        # Get program member
        api_response = api_instance.get_program_member(program_id, member_id)
        print("The response of LV2ProgramsApi->get_program_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->get_program_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Unique loyalty program ID (format lprg_[a-f0-9]+). | 
 **member_id** | **str**| Program member ID (format lmbr_[a-f0-9]+). | 

### Return type

[**MemberWithCards**](MemberWithCards.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The member with its cards. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_program_membership**
> LoyaltiesProgramsMembershipsGetResponseBody get_program_membership(program_id, customer_id, identification_type=identification_type)

Get program membership

Returns the membership for one customer in the program: the member, the program, and the members loyalty cards. A card includes tier_progress when its card definition has a tier structure and the member has a tier on that card. Otherwise tier_progress is omitted. identification_type chooses how customerId is read. It defaults to customer_id.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_memberships_get_response_body import LoyaltiesProgramsMembershipsGetResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Unique loyalty program ID (format lprg_[a-f0-9]+).
    customer_id = 'customer_id_example' # str | Unique identifier of the customer or member, interpreted according to identification_type: a Voucherify customer ID (cust_...), a customer source_id, or a loyalty member ID (lmbr_...).
    identification_type = customer_id # str | Chooses how customerId is read. customer_id is the Voucherify customer ID and the default. customer_source_id is the customers source_id. member_id is the loyalty member ID. (optional) (default to customer_id)

    try:
        # Get program membership
        api_response = api_instance.get_program_membership(program_id, customer_id, identification_type=identification_type)
        print("The response of LV2ProgramsApi->get_program_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->get_program_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Unique loyalty program ID (format lprg_[a-f0-9]+). | 
 **customer_id** | **str**| Unique identifier of the customer or member, interpreted according to identification_type: a Voucherify customer ID (cust_...), a customer source_id, or a loyalty member ID (lmbr_...). | 
 **identification_type** | **str**| Chooses how customerId is read. customer_id is the Voucherify customer ID and the default. customer_source_id is the customers source_id. member_id is the loyalty member ID. | [optional] [default to customer_id]

### Return type

[**LoyaltiesProgramsMembershipsGetResponseBody**](LoyaltiesProgramsMembershipsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The membership in the program. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_card_transactions**
> LoyaltiesProgramsMembersCardsTransactionsListResponseBody list_card_transactions(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)

List card transactions

Returns a cursor-paginated list of transactions on the members card. Filter by id, card_definition_id, and created_at. Order by id (default -id, newest first). Returns 404 when the program, member, or card doesnt exist. The program is checked first, then the member, then the card. A member of another program, or a card that isnt assigned to this member, is not found.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_cards_transactions_list_request_query import LoyaltiesProgramsMembersCardsTransactionsListRequestQuery
from voucherify.models.loyalties_programs_members_cards_transactions_list_response_body import LoyaltiesProgramsMembersCardsTransactionsListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Unique loyalty program ID (format lprg_[a-f0-9]+).
    member_id = 'member_id_example' # str | Program member ID (format lmbr_[a-f0-9]+).
    card_id = 'card_id_example' # str | Loyalty card ID (format lcrd_[a-f0-9]+).
    limit = 10 # int | Maximum number of transactions to return. Must be between 1 and 100. Defaults to 10 when not provided. (optional) (default to 10)
    order = voucherify.ListCardTransactionsOrderParameter() # ListCardTransactionsOrderParameter | Orders results by transaction id. -id is newest first and the default. id is oldest first. An array that orders by id and -id together is rejected. (optional)
    cursor = 'cursor_example' # str | Pagination cursor returned in the cursor.next field of a previous response. Must match the pattern ^lcrsctx_[a-f0-9]+$. (optional)
    filters = voucherify.LoyaltiesProgramsMembersCardsTransactionsListRequestQuery() # LoyaltiesProgramsMembersCardsTransactionsListRequestQuery | Field-specific filter conditions, passed as a deep object, e.g. filters[id][conditions][$is] lctx_0f5d0a8878caa3ee5c. (optional)

    try:
        # List card transactions
        api_response = api_instance.list_card_transactions(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_card_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_card_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Unique loyalty program ID (format lprg_[a-f0-9]+). | 
 **member_id** | **str**| Program member ID (format lmbr_[a-f0-9]+). | 
 **card_id** | **str**| Loyalty card ID (format lcrd_[a-f0-9]+). | 
 **limit** | **int**| Maximum number of transactions to return. Must be between 1 and 100. Defaults to 10 when not provided. | [optional] [default to 10]
 **order** | [**ListCardTransactionsOrderParameter**](.md)| Orders results by transaction id. -id is newest first and the default. id is oldest first. An array that orders by id and -id together is rejected. | [optional] 
 **cursor** | **str**| Pagination cursor returned in the cursor.next field of a previous response. Must match the pattern ^lcrsctx_[a-f0-9]+$. | [optional] 
 **filters** | [**LoyaltiesProgramsMembersCardsTransactionsListRequestQuery**](.md)| Field-specific filter conditions, passed as a deep object, e.g. filters[id][conditions][$is] lctx_0f5d0a8878caa3ee5c. | [optional] 

### Return type

[**LoyaltiesProgramsMembersCardsTransactionsListResponseBody**](LoyaltiesProgramsMembersCardsTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Cursor-paginated list of card transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_order_payments**
> LoyaltiesProgramsMembersOrdersPaymentsListResponseBody list_member_order_payments(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)

List member order payments

Lists stored PAY_WITH_POINTS order transactions for the program member, with cursor pagination. Filter by id, card_definition_id, and created_at. Order by id (default -id, newest first). Dry-run (SIMULATED) results arent stored and dont appear. Returns 404 when the program or the member doesnt exist. The program is checked first.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_orders_payments_list_request_query import LoyaltiesProgramsMembersOrdersPaymentsListRequestQuery
from voucherify.models.loyalties_programs_members_orders_payments_list_response_body import LoyaltiesProgramsMembersOrdersPaymentsListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program (lprg_ followed by hexadecimal characters).
    member_id = 'member_id_example' # str | Identifies the program member (lmbr_[a-f0-9]+).
    limit = 10 # int | Maximum number of items to return. An integer between 1 and 100; numeric strings are also accepted. Defaults to 10. (optional) (default to 10)
    order = voucherify.ListCardTransactionsOrderParameter() # ListCardTransactionsOrderParameter | Orders results by transaction id. -id is newest first and the default. id is oldest first. An array that orders by id and -id together is rejected. (optional)
    cursor = 'cursor_example' # str | Pagination cursor returned in the cursor.next field of a previous response (format: lcrsotx_ followed by hexadecimal characters). (optional)
    filters = voucherify.LoyaltiesProgramsMembersOrdersPaymentsListRequestQuery() # LoyaltiesProgramsMembersOrdersPaymentsListRequestQuery | Filters results by field, e.g. filters[id][conditions][$is] lotx_.... Each field accepts a conditions object with condition operators. (optional)

    try:
        # List member order payments
        api_response = api_instance.list_member_order_payments(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_member_order_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_member_order_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program (lprg_ followed by hexadecimal characters). | 
 **member_id** | **str**| Identifies the program member (lmbr_[a-f0-9]+). | 
 **limit** | **int**| Maximum number of items to return. An integer between 1 and 100; numeric strings are also accepted. Defaults to 10. | [optional] [default to 10]
 **order** | [**ListCardTransactionsOrderParameter**](.md)| Orders results by transaction id. -id is newest first and the default. id is oldest first. An array that orders by id and -id together is rejected. | [optional] 
 **cursor** | **str**| Pagination cursor returned in the cursor.next field of a previous response (format: lcrsotx_ followed by hexadecimal characters). | [optional] 
 **filters** | [**LoyaltiesProgramsMembersOrdersPaymentsListRequestQuery**](.md)| Filters results by field, e.g. filters[id][conditions][$is] lotx_.... Each field accepts a conditions object with condition operators. | [optional] 

### Return type

[**LoyaltiesProgramsMembersOrdersPaymentsListResponseBody**](LoyaltiesProgramsMembersOrdersPaymentsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a paginated list of persisted order payment transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_reward_purchases**
> LoyaltiesProgramsMembersRewardsPurchasesListResponseBody list_member_reward_purchases(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)

List member reward purchases

Lists stored PURCHASE reward transactions for the program member, with cursor pagination. Filter by id, reward_id, card_definition_id, and created_at. Order by id (default -id, newest first). Purchases rejected before a transaction is stored dont appear. A purchase accepted with 202 that later fails is stored as REJECTED with details.rejection. Returns 404 when the program or the member doesnt exist. The program is checked first.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_rewards_purchases_list_request_query import LoyaltiesProgramsMembersRewardsPurchasesListRequestQuery
from voucherify.models.loyalties_programs_members_rewards_purchases_list_response_body import LoyaltiesProgramsMembersRewardsPurchasesListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Unique loyalty program identifier (format: lprg_ followed by hexadecimal characters).
    member_id = 'member_id_example' # str | Program member ID (format lmbr_[a-f0-9]+).
    limit = 10 # int | Maximum number of items to return. An integer between 1 and 100; numeric strings are also accepted. Defaults to 10. (optional) (default to 10)
    order = voucherify.ListCardTransactionsOrderParameter() # ListCardTransactionsOrderParameter | Orders results by transaction id. -id is newest first and the default. id is oldest first. An array that orders by id and -id together is rejected. (optional)
    cursor = 'cursor_example' # str | Pagination cursor returned in the cursor.next field of a previous response (format: lcrstrx_ followed by hexadecimal characters). (optional)
    filters = voucherify.LoyaltiesProgramsMembersRewardsPurchasesListRequestQuery() # LoyaltiesProgramsMembersRewardsPurchasesListRequestQuery | Field filters, e.g. filters[reward_id][conditions][$is] lrew_.... Each field accepts a conditions object with condition operators. (optional)

    try:
        # List member reward purchases
        api_response = api_instance.list_member_reward_purchases(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_member_reward_purchases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_member_reward_purchases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Unique loyalty program identifier (format: lprg_ followed by hexadecimal characters). | 
 **member_id** | **str**| Program member ID (format lmbr_[a-f0-9]+). | 
 **limit** | **int**| Maximum number of items to return. An integer between 1 and 100; numeric strings are also accepted. Defaults to 10. | [optional] [default to 10]
 **order** | [**ListCardTransactionsOrderParameter**](.md)| Orders results by transaction id. -id is newest first and the default. id is oldest first. An array that orders by id and -id together is rejected. | [optional] 
 **cursor** | **str**| Pagination cursor returned in the cursor.next field of a previous response (format: lcrstrx_ followed by hexadecimal characters). | [optional] 
 **filters** | [**LoyaltiesProgramsMembersRewardsPurchasesListRequestQuery**](.md)| Field filters, e.g. filters[reward_id][conditions][$is] lrew_.... Each field accepts a conditions object with condition operators. | [optional] 

### Return type

[**LoyaltiesProgramsMembersRewardsPurchasesListResponseBody**](LoyaltiesProgramsMembersRewardsPurchasesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Paginated list of reward purchase transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_member_reward**
> LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBody purchase_member_reward(program_id, member_id, loyalties_programs_members_rewards_purchases_create_request_body=loyalties_programs_members_rewards_purchases_create_request_body)

Purchase reward with points

Purchases a reward for the program member by spending points from the members card. The card comes from the matching reward costs card definition. The program, reward, and member must be ACTIVE. The program and reward must be inside their validity windows. The reward must be assigned to the program with stock available, a cost must match the customer, and the purchase must stay inside frequency, cooldown, balance, and spending limits. Modes: - TRANSACTION (default): creates a PENDING reward transaction and a PENDING card transaction. Returns 202. - DRY_RUN: simulates the purchase and doesnt create a transaction. Returns 200 with status SIMULATED.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_rewards_purchases_create_combined_response_body import LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBody
from voucherify.models.loyalties_programs_members_rewards_purchases_create_request_body import LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Unique loyalty program identifier (format: lprg_ followed by hexadecimal characters).
    member_id = 'member_id_example' # str | Program member ID (format lmbr_[a-f0-9]+).
    loyalties_programs_members_rewards_purchases_create_request_body = voucherify.LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody() # LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody |  (optional)

    try:
        # Purchase reward with points
        api_response = api_instance.purchase_member_reward(program_id, member_id, loyalties_programs_members_rewards_purchases_create_request_body=loyalties_programs_members_rewards_purchases_create_request_body)
        print("The response of LV2ProgramsApi->purchase_member_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->purchase_member_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Unique loyalty program identifier (format: lprg_ followed by hexadecimal characters). | 
 **member_id** | **str**| Program member ID (format lmbr_[a-f0-9]+). | 
 **loyalties_programs_members_rewards_purchases_create_request_body** | [**LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody**](LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody.md)|  | [optional] 

### Return type

[**LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBody**](LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Dry run result (mode &#x60;DRY_RUN&#x60;). No transaction was created; the returned transaction has status &#x60;SIMULATED&#x60; and no &#x60;id&#x60;. and Purchase accepted (mode &#x60;TRANSACTION&#x60;). A &#x60;PENDING&#x60; reward transaction was created and will be processed asynchronously. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

