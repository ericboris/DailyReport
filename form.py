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
			tasks = ''
		    for task in job.tasks:
		    	task = str(task.title) + str(task.price) + '\n'
				tasks += task
		'''
		    subtotal = str(job.subtotal) + '\n'
		    if job.tax != 0:
				tax = str(job.tax) + '\n'
			else:
				tax = ''
		    total = str(job.total) + '\n'
			job = name + tasks + subtotal + tax + total
			form += job
		#hours = self.setHours(jobs)
		#form = [self.jobs, self.dayTotal]
		return form
		'''

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
