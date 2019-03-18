import sys
import requests
from voucherify.balance import Balance
from voucherify.campaigns import Campaigns
from voucherify.customers import Customers
from voucherify.distributions import Distributions
from voucherify.events import Events
from voucherify.exports import Exports
from voucherify.orders import Orders
from voucherify.products import Products
from voucherify.redemptions import Redemptions
from voucherify.segments import Segments
from voucherify.validation_rules import ValidationRules
from voucherify.validations import Validations
from voucherify.vouchers import Vouchers

TIMEOUT = 1000
ROOT_URL = 'https://api.voucherify.io/v1'

# TODO: also include current SDK version
class CustomClient:
	def __init__(self, application_id: str, client_secret_key: str, root_url=ROOT_URL):
		self.timeout = TIMEOUT
		self.headers = {
			'X-App-Id': application_id,
			'X-App-Token': client_secret_key,
			'X-Voucherify-Channel': 'Python-{}.{}.{}-SDK'.format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro),
			'Content-Type': 'application/json'
		}
		self.root_url = root_url

	def get(self, url='/'):
		return requests.get('{}{}'.format(self.root_url, url), headers=self.headers, timeout=self.timeout).json()

	def post(self, url='/', payload={}):
		return requests.post('{}{}'.format(self.root_url, url), headers=self.headers, timeout=self.timeout, json=payload).json()

	def put(self, url='/', payload={}):
		return requests.put('{}{}'.format(self.root_url, url), headers=self.headers, timeout=self.timeout, json=payload).json()

	def delete(self, url='/'):
		return requests.delete('{}{}'.format(self.root_url, url), headers=self.headers, timeout=self.timeout).json()

	def post_csv(self, url='/', filepath=''):
		files = {'file': (filepath, open(filepath, 'rb'))}
		return requests.post('{}{}'.format(self.root_url, url), headers=self.headers, timeout=self.timeout, files=files)


# TODO: definition for client_config
class ApiClient(CustomClient):
	def __init__(self, client_config):
		super(ApiClient, self).__init__(
			application_id=client_config['application_id'],
			client_secret_key=client_config['client_secret_key'],
			root_url=client_config['root_url']
		)				
		self.balance = Balance(self)
		self.campaigns = Campaigns(self)
		self.customers = Customers(self)
		self.distributions = Distributions(self)
		self.events = Events(self)
		self.exports = Exports(self)
		self.orders = Orders(self)
		self.products = Products(self)
		self.redemptions = Redemptions(self)
		self.segments = Segments(self)
		self.validation_rules = ValidationRules(self)
		self.validations = Validations(self, promotions_namespace=client_config['promotions_namespace'])
		self.vouchers = Vouchers(self)

	# TODO: instead of that .format() everywhere, just pass 2 url chunks and join by urllib.parse.urljoin ?

if __name__ == '__main__':
	import os
	from dotenv import load_dotenv

	load_dotenv()

	client_config = {
		'application_id': os.getenv('VOUCHERIFY_APP_ID'),
		'client_secret_key': os.getenv('VOUCHERIFY_CLIENT_SECRET_KEY'),
		'promotions_namespace': os.getenv('PROMOTIONS_NAMESPACE'),
		'root_url': ROOT_URL
	}
	client = ApiClient(client_config)
