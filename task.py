'''
Parses a Task object out of a description string
'''

import re

class Task:
	def __init__ (self, description):
		self.title = self.get_title(description)
		self.price = self.get_price(description)
		self.taxable = self.is_taxable()

	def get_title(self, description):
		title = ''.join(i for i in description if not i.isdigit()).strip()
		return str(title)

	def get_price(self, description):
		#for keyword in keywords:
		#	if keyword in description:
		try:
			price = int(re.search(r'\d+', description).group())
		except AttributeError:
			#if price == '':
			return 0
		#		break
		# needs a more elegant way to check if task is actually a note
		#if price == '':
		#	return 0
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

	keywords = ['window', 'in ext', 'ext', 'out', 'in out', 'skylight' 'note',
		'glass', 'rail', 'mirror', 'gutter', 'roof', 'moss', 'debris', 'scrub',
		'pressure', 'wash', 'pw', 'setup', 'set up', 'fb', 'facebook', 'ad']
