from task import Task

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
		events_list = event.get('description').splitlines()
		for line in events_list:
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
