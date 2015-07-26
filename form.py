class Form:
	def __init__(self, events):
		form = self.setForm(events)

	def form(self, events):
		jobs = self.setJobs(events)
		dailyTotal = self.setDailyTotal(jobs)
		hours = self.setHours(jobs)
		form = [jobs, dailyTotal, hours]
		return form

	def setJobs(self, events):
		jobs = []
		for event in events["items"]:
			jobs.append(new Job(event))
		return jobs

	def setDailyTotal(self, jobs):
		total = 0
		for job in jobs:
			total += job.subTotal
		return total

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
