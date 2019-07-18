import requests
import json

try:
    from urllib.parse import urlencode, quote
except ImportError:
    from urllib import urlencode
    from urllib import quote

ENDPOINT_URL = 'https://api.voucherify.io'
TIMEOUT = 30 * 1000


class VoucherifyRequest(object):
    def __init__(self, application_id, client_secret_key, api_endpoint=None):
        self.timeout = TIMEOUT
        self.url = (api_endpoint if api_endpoint else ENDPOINT_URL) + "/v1"
        self.headers = {
            'X-App-Id': application_id,
            'X-App-Token': client_secret_key,
            'X-Voucherify-Channel': 'Python-SDK',
            'Content-Type': 'application/json'
        }

    def request(self, path, method='GET', **kwargs):
        try:
            url = self.url + path

            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                timeout=self.timeout,
                **kwargs
            )
        except requests.HTTPError as e:
            response = json.loads(e.read())
        except requests.ConnectionError as e:
            raise VoucherifyError(e)

        if response.headers.get('content-type') and 'json' in response.headers['content-type']:
            result = response.json()
        else:
            result = response.text

        if isinstance(result, dict) and result.get('error'):
            raise VoucherifyError(result)

        return result


class Vouchers(VoucherifyRequest):
    def __init__(self, *args, **kwargs):
        super(Vouchers, self).__init__(*args, **kwargs)

    def list(self, query):
        path = '/vouchers/'

        return self.request(
            path,
            params=query
        )

    def get(self, code):
        path = '/vouchers/' + quote(code)

        return self.request(
            path
        )

    def create(self, voucher):
        code = voucher.get('code', '')
        path = '/vouchers/' + quote(code)

        return self.request(
            path,
            data=json.dumps(voucher),
            method='POST'
        )

    def update(self, voucher_update):
        path = '/vouchers/' + quote(voucher_update.get("code"))

        return self.request(
            path,
            data=json.dumps(voucher_update),
            method='PUT'
        )

    def enable(self, code):
        path = '/vouchers/' + quote(code) + '/enable'

        return self.request(
            path,
            method='POST'
        )

    def disable(self, code):
        path = '/vouchers/' + quote(code) + '/disable'

        return self.request(
            path,
            method='POST'
        )


class Redemptions(VoucherifyRequest):
    def __init__(self, *args, **kwargs):
        super(Redemptions, self).__init__(*args, **kwargs)

    def redeem(self, code, tracking_id=None):
        context = {}

        if code and isinstance(code, dict):
            context = code
            code = context['voucher']
            del context['voucher']

        path = '/vouchers/' + quote(code) + '/redemption'

        if tracking_id:
            path = path + '?' + urlencode({'tracking_id': tracking_id})

        return self.request(
            path,
            method='POST',
            data=json.dumps(context),
        )

    def getForVoucher(self, code):
        path = '/vouchers/' + quote(code) + '/redemption'

        return self.request(
            path
        )

    def list(self, query):
        path = '/redemptions'

        return self.request(
            path,
            params=query
        )

    def rollback(self, redemption_id, reason=None):
        path = '/redemptions/' + redemption_id + '/rollback'

        if reason:
            path = path + '?' + urlencode({'reason': reason})

        return self.request(
            path,
            method='POST'
        )


class Distributions(VoucherifyRequest):
    def __init__(self, *args, **kwargs):
        super(Distributions, self).__init__(*args, **kwargs)

    def publish(self, params):
        path = '/vouchers/publish'

        return self.request(
            path,
            method='POST',
            data=json.dumps(params)
        )


class Customers(VoucherifyRequest):
    def __init__(self, *args, **kwargs):
        super(Customers, self).__init__(*args, **kwargs)

    def create(self, customer):
        path = '/customers/'

        return self.request(
            path,
            data=json.dumps(customer),
            method='POST'
        )

    def get(self, customer_id):
        path = '/customers/' + quote(customer_id)

        return self.request(
            path
        )

    def update(self, customer):
        path = '/customers/' + quote(customer.get('id'))

        return self.request(
            path,
            data=json.dumps(customer),
            method='PUT'
        )

    def delete(self, customer_id):
        path = '/customers/' + quote(customer_id)

        return self.request(
            path,
            method='DELETE'
        )


class Client(VoucherifyRequest):
    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self.customers = Customers(*args, **kwargs)
        self.vouchers = Vouchers(*args, **kwargs)
        self.redemptions = Redemptions(*args, **kwargs)
        self.distributions = Distributions(*args, **kwargs)


class VoucherifyError(Exception):
    def __init__(self, result):
        self.result = result
        self.code = None
        self.message = None

        try:
            self.type = result['error_code']
            self.message = result['error_msg']
        except:
            self.type = ''
            self.message = result

        Exception.__init__(self, self.message)


__all__ = ['Client']
