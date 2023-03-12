try:
    from urllib.parse import urlencode, quote
except ImportError:
    from urllib import urlencode
    from urllib import quote

class Campaigns:
	def __init__(self, client):
		self.client = client
		self.url = '/campaigns'
	def create(self, campaign):
		"""
			Method to create a batch of vouchers aggregated in one campaign. You can choose varied types of vouchers and define unique codes pattern.
			https://docs.voucherify.io/reference#create-campaign
		"""
		return self.client.post(self.url, campaign)


	def update(self, name_or_id, campaign):
		"""
			Updates the specified campaign by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

			You can modify following fields: start_date, expiration_date, metadata, description, type. Other fields than listed above won't be modified.
			Even if provided they will be silently skipped. This method will update vouchers aggregated in the campaign. It will affect all vouchers which are not published or redeemed yet.
			https://docs.voucherify.io/reference#update-campaign
		"""
		return self.client.put('{}/{}'.format(self.url, quote(name_or_id)), campaign)

	def get(self, name):
		"""
			https://docs.voucherify.io/reference#get-campaign
		"""
		return self.client.get('{}/{}'.format(self.url, quote(name)))

	def delete(self, name):
		"""
			Permanently deletes a campaign and all related vouchers. It cannot be undone. Also immediately removes any redemptions on the voucher.
			https://docs.voucherify.io/reference#delete-campaign
		"""
		return self.client.delete('{}/{}'.format(self.url, quote(name)))

	def add_voucher(self, name, properties):
		"""
			This method gives a possibility to push new vouchers to existing campaign. Voucher definition will be inherited from this one kept in campaign profile.
			However you are able to overwrite few properties inherited from campaign: metadata, additional_info, redemption.quantity, category.
			https://docs.voucherify.io/reference#add-voucher-to-campaign
		"""
		return self.client.post('{}/{}/vouchers'.format(self.url, quote(name)), properties)

	def import_voucher(self, name, vouchers):
		"""
			Imports vouchers to an existing campaign.
			https://docs.voucherify.io/reference#import-vouchers
		"""
		return self.client.post('{}/{}/import'.format(self.url, quote(name)), vouchers)

	def list_campaigns(self, params):
		"""
			Returns a list of your campaigns. The campaigns are returned sorted by creation date, with the most recent campaigns appearing first.
			https://docs.voucherify.io/reference#list-campaigns
		"""
		return self.client.get(self.url, params)

	def add_voucher_by_code(self, name, code, properties):
		"""
			This method gives a possibility to push new vouchers to existing campaign. Voucher definition will be inherited from this one kept in campaign profile.
			However you are able to overwrite few properties inherited from campaign: metadata, additional_info, redemption.quantity, category.
			https://docs.voucherify.io/reference#add-voucher-to-campaign
		"""
		return self.client.post('{}/{}/vouchers/{}'.format(self.url, quote(name), quote(code)), properties)

	def import_voucher_csv(self, name, filepath):
		"""
			Imports vouchers to an existing campaign.
			https://docs.voucherify.io/reference#import-vouchers-by-csv
		"""
		return self.client.post_csv('{}/{}/importCSV'.format(self.url, quote(name)), filepath)