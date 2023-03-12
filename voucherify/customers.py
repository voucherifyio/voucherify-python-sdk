try:
    from urllib.parse import urlencode, quote
except ImportError:
    from urllib import urlencode
    from urllib import quote

class Customers:
	def __init__(self, client):
		self.client = client
		self.url = '/customers'

	def get(self, customer_id):
		"""
			https://docs.voucherify.io/reference#read-customer
		"""
		return self.client.get('{}/{}'.format(self.url, quote(customer_id)))

	def create(self, customer):
		"""
			https://docs.voucherify.io/reference#create-customer
		"""
		return self.client.post(self.url, customer)

	def update(self, customer):
		"""
			https://docs.voucherify.io/reference#update-customer
		"""
		# hasattr(x, "__getitem__")
		if isinstance(customer, dict):
			encoding_key = customer.get('id') or customer.get('source_id')
		else:
			encoding_key = customer.id or customer.source_id
		del customer['id']
		return self.client.put('{}/{}'.format(self.url, quote(encoding_key)), customer)

	def delete(self, customer_id):
		"""
			https://docs.voucherify.io/reference#delete-customer
		"""
		return self.client.delete('{}/{}/permanent-deletion'.format(self.url, quote(customer_id)))

	def permanent_delete(self, customer_id):
		"""
			The organization user can remove consumer data permanently from the Voucherify system by using this API method.
			It d​eletes all customer data and connected resources. It makes customer profile forgotten by Voucherify.
			https://docs.voucherify.io/reference#delete-customer-permanently
		"""
		return self.client.delete('{}/{}'.format(self.url, quote(customer_id)))

	def list_customers(self, params):
		"""
			Returns a list of your vouchers. The vouchers are returned sorted by creation date, with the most recent vouchers appearing first.
			https://docs.voucherify.io/v2018-08-01/reference#list-vouchers
		"""
		return self.client.get(self.url, params)		
