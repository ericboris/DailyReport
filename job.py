from task import Task
import re

class Job:
	def __init__ (self, event):
		self.name = self.get_name(event)
		self.tasks = self.get_tasks(event)
		self.subtotal = self.get_subtotal()
		self.tax = self.get_tax()
		self.total = self.get_total()
		#self.start = self.setStartTime(event)
		#self.end = self.setEndTime(event)
		# self.date = self.setDate

	def get_name(self, event):
		name = str(event.get('summary'))
		return name

	def get_tasks(self, event):
		tasks = []
		try:
			events_list = event.get('description').splitlines()
		except AttributeError:
			return ''
		for line in events_list:
			tel_num = re.compile(".*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?", re.S) # telepone number
			keywords = ['window', 'in ext', 'ext', 'out', 'in out', 'skylight' 'note',
				'glass', 'rail', 'mirror', 'gutter', 'roof', 'moss', 'debris', 'scrub',
				'pressure', 'wash', 'pw', 'setup', 'set up', 'fb', 'facebook', 'ad', 'windows']
			if len(line) <= 0 or tel_num.match(line):
				continue
			task = Task(line)
			tasks.append(task)
		return tasks

	def get_subtotal(self):
		subtotal = 0
		for task in self.tasks:
			subtotal += task.price
		return subtotal

	def get_tax(self):
		taxableTasks = 0
		for task in self.tasks:
			if task.taxable:
				taxableTasks += task.price
				#location = event.get("location")
		taxRate = 0.096
		tax = round(taxableTasks * taxRate, 2)
		return tax

	def get_total(self):
		total = self.subtotal + self.tax
		return total
