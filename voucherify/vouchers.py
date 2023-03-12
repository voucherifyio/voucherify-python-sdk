try:
    from urllib.parse import urlencode, quote
except ImportError:
    from urllib import urlencode
    from urllib import quote
	
class Vouchers:
	def __init__(self, client):
		self.client = client
		self.url = '/vouchers'
	def get(self, code: str):
		"""
			Retrieves the voucher with the given code.
			https://docs.voucherify.io/v2018-08-01/reference#vouchers-get
		"""
		return self.client.get('{}/{}'.format(self.url, quote(code)))

	def create(self, voucher):
		"""
			Method to create single voucher. You can choose varied types of vouchers.
			https://docs.voucherify.io/v2018-08-01/reference#create-voucher
		"""
		return self.client.post('{}/{}'.format(self.url, quote(voucher['code'])), voucher)

	def update(self, voucher):
		"""
			Updates the specified voucher by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

			Updates a voucher. You can modify following fields: category, start_date, expiration_date, active, additional_info, metadata. Other fields than listed above won't be modified. Even if provided they will be silently skipped.
			https://docs.voucherify.io/v2018-08-01/reference#update-voucher
		"""
		return self.client.put('{}/{}'.format(self.url, quote(voucher['code'])), voucher)

	def delete(self, code: str, params={}):
		"""
			Permanently deletes a voucher. It cannot be undone. Also immediately removes any redemptions on the voucher.
			https://docs.voucherify.io/v2018-08-01/reference#delete-voucher
		"""
		pass

	def list_vouchers(self, params={}):
		"""
			Returns a list of your vouchers. The vouchers are returned sorted by creation date, with the most recent vouchers appearing first.
			https://docs.voucherify.io/v2018-08-01/reference#list-vouchers
		"""
		pass

	def enable(self, params={}):
		"""
			There are various times when you'll want to manage voucher accessibility.
			This can be done by two API method for managing voucher state - enable and disable. It puts voucher to state in which it is active and can be redeemed - only when it is not expired or before start date.
			https://docs.voucherify.io/v2018-08-01/reference#enable-voucher
		"""
		pass

	def disable(self, params):
		"""
			There are various times when you'll want to manage voucher accessibility.
			This can be done by two API method for managing voucher state - enable and disable. It puts voucher to state in which it is inactive and cannot be redeemed.
			https://docs.voucherify.io/v2018-08-01/reference#disable-voucher
		"""
		pass

	def import_vouchers(self, vouchers):
		"""
			Method imports vouchers to the repository.
			https://docs.voucherify.io/v2018-08-01/reference#import-vouchers-1
		"""
		pass