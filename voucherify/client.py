import requests
import json
import re

try:
    from urllib.parse import urlencode, quote
except ImportError:
    from urllib import urlencode
    from urllib import quote

ENDPOINT_URL = 'https://api.voucherify.io/v1'


class Client(object):
    def __init__(self, application_id, client_secret_key):
        self.timeout = 30 * 1000
        self.headers = {
            'X-App-Id': application_id,
            'X-App-Token': client_secret_key,
            'X-Voucherify-Channel': 'Python-SDK',
            'Content-Type': 'application/json'
        }

    def request(self, path, method='GET', **kwargs):
        try:
            url = join_url(ENDPOINT_URL, path)

            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                timeout=self.timeout,
                **kwargs
            )
        except requests.HTTPError as e:
            response = json.loads(e.read())

        if 'json' in response.headers['content-type']:
            result = response.json()
        else:
            raise VoucherifyError('Content-Type of API response is not in a JSON format')

        if result and isinstance(result, dict) and result.get('error'):
            raise VoucherifyError(result)

        return result

    def list(self, query):
        path = '/vouchers/'

        return self.request(
            path,
            params=query
        )

    def get(self, code):
        path = join_url('/vouchers/', quote(code))

        return self.request(
            path
        )

    def create(self, voucher):
        code = voucher.get('code', '')
        path = join_url('/vouchers/', quote(code))

        return self.request(
            path,
            data=json.dumps(voucher),
            method='POST'
        )

    def enable(self, code):
        path = join_url('/vouchers/', quote(code), '/enable')

        return self.request(
            path,
            method='POST'
        )

    def disable(self, code):
        path = join_url('/vouchers/', quote(code), '/disable')

        return self.request(
            path,
            method='POST'
        )

    def redemption(self, code):
        path = join_url('/vouchers/', quote(code), '/redemption')

        return self.request(
            path
        )

    def redemptions(self, query):
        path = '/redemptions'

        return self.request(
            path,
            params=query
        )

    def redeem(self, code, tracking_id=None):
        context = {}

        if code and isinstance(code, dict) and code.get('error'):
            context = code
            code = context['voucher']
            del context['voucher']

        path = join_url('/vouchers/', quote(code), '/redemption')

        if tracking_id:
            join_url_params(path, {'tracking_id': tracking_id})

        return self.request(
            path,
            method='POST',
            data=json.dumps(context),
        )

    def rollback(self, redemption_id, reason=None):
        path = join_url('/redemptions/', redemption_id, '/rollback')

        if reason:
            join_url_params(path, {'reason': reason})

        return self.request(
            path,
            method='POST'
        )

    def publish(self, campaign_name):
        path = join_url_params('/vouchers/publish', {'campaign': campaign_name})

        return self.request(
            path,
            method='POST'
        )


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


def join_url(url, *paths):
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url


def join_url_params(url, params):
    return url + '?' + urlencode(params)
