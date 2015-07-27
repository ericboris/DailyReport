'''
Parses a Task object out of a description string
'''

class Task:
	def __init__ (self, description):
		self.title = self.get_title(description)
		self.price = self.get_price(description)
		self.taxable = self.is_taxable()

	def get_title(self, description):
		title = ''.join(i for i in description if not i.isdigit()).strip()
		return str(title)

	def get_price(self, description):
		price = ''.join(i for i in description if not i.isalpha()).strip()
		# needs a more elegant way to check if task is actually a note
		if price == '':
			return 0
		return int(price)

	def is_taxable(self):
		non_taxable_tasks = ['window', 'windows', 'skylight', 'skylights', 'note',
			'glass', 'mirror', 'mirrors', 'in/out', 'in/ext', 'in out', 'in ext']
		if any(task in self.title for task in non_taxable_tasks):
			# task is not taxable
			return False
		else:
			# task is taxable
			return True
