from job import Job

class Form:
	def __init__(self, events):
		self.jobs = self.get_jobs(events)
		self.dayTotal = self.get_day_total()
		self.form = self.get_form()

	def get_form(self):
		form = ''
		for job in self.jobs:
			name = str(job.name)

			tasksLocal = []
			for t in job.tasks:
				tasksLocal.append(t.title + ' ' + str(t.price))
			tasks = '\n'.join(tasksLocal)

			subtotal = 'subtotal ' + str(job.subtotal)

			if job.tax != 0:
				tax = 'tax ' + str(job.tax)
			else:
				tax = ''

			total = 'total ' + str(job.total)

			job = [name, tasks, subtotal, tax, total]
			job = '\n'.join(job) + '\n'*2
			form += job

		form += 'total w/o tax ' + str(self.dayTotal)
		form += '\n'*2
		form += 'hours '
		form += '\n'*2

		return form

	def get_jobs(self, events):
		jobs = []
		for event in events:
		    j = Job(event)
		    jobs.append(j)
		return jobs

	def get_day_total(self):
		dayTotal = 0
		for job in self.jobs:
			dayTotal += job.subtotal
		return dayTotal
'''
	def setHours(self, jobs):
		dayStartTime = setDayStartTime()
		dayEndTime = setDayEndTime()
		hours = [dayStartTime, dayEndTime]
		return hours

	def setDayStartHours(self, jobs):
		dayStartTime = None
		for job in jobs
			if dayStartTime == None:
				dayStartTime = job.start
			elif job.start < dayStartTime:
				dayStartTime = job.start
			else:
				pass

	def setDayEndHours(self):
		dayEndTime = None
		for job in jobs:
			if dayEndTime == None:
				dayEndTime = job.end
			elif job.end > dayEndTime:
				dayEndTime = job.end
			else:
				pass

	def copyToClipboard(self):
		#pyperClip self.form to clipboard

	def saveFormToFile(self):
		#os.newFile self.form to new file
'''
