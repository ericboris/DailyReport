class Job:
	def __init__ (self, event):
		self.name = self.setName(event)
		self.tasks = self.setTasks(event)
		self.subTotal = self.setSubtotal(event)
		self.tax = self.setTax(event)
		self.start = self.setStartTime(event)
		self.end = self.setEndTime(event)
		# self.date = self.setDate

	def setName(self, event):
		name = event.get("id")
		return name

	def setTasks(self, event):
		tasks = []
		keywords = ['in/out skylight glass rail screen pw scrub gutter roof debris moss']
		for line in event.get("description"):
			if line has keyword and has price:
				tasks.append(task(line))
		return tasks

	def setSubtotal(self, event):
		subTotal = 0
		for task in tasks[]:
			if task is not tip && task is not taxable:
					subTotal += task.price

	def setTaxOwed(self, event):
		tax = 0
		if task is taxable:
		tax += task.price
		location = event.get("location")
		if location is not WS:
			locationMultiplier = 0.95
		else:  location is MI or BE
		locationMultiplier = 0.96
		tax *= locationMultiplier
		self.taxOwed = tax

	def setStartTime(self, event):
		startTime = event.get("start")
		return startTime

	def setEndTime(self, event):
		endTime = event.get("end")
		return endTime

	def setDate(self, event):
		date = event.date
		return date
