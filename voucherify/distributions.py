class Distributions:
	def __init__(self, client, exports_namespace):
		self.client = client
		self.url = '/distributions'
		self.exports_namespace = exports_namespace