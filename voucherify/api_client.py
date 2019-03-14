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

class ApiClient:
	def __init__(self, application_id, client_secret_key, root_url=ROOT_URL):
		self.timeout = TIMEOUT
		self.headers = {
			'X-App-Id': application_id,
			'X-App-Token': client_secret_key,
			'X-Voucherify-Channel': 'Python-SDK',
			'Content-Type': 'application/json'
		}
		self.root_url = root_url
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
		self.validations = Validations(self)
		self.vouchers = Vouchers(self)
		

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
