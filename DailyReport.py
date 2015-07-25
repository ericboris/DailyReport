# Create an email Form based on day's Calendar Events. 

import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Daily Report'


def main():
	# access Calender API for Events
	"""Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print 'Getting the upcoming 10 events'
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
	'''
    if not events:
        print 'No upcoming events found.'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print start, event['summary']
	'''
	form = Form(events)
	## print form
	# save form to clipboard or file


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials


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


class Task:
	price = find Int in description
	variety = [windows, pw, roof, tip]
	
	tax = 0

	def init (self, description):
		self.name = extractNameFromDescription()
		self.price = extractPriceFromDescription()
		self.type = setType()
		self.tax = setTax()
		
	def setTax(self, description):
		taxable = False
		if variety is not windows and not tip:
			taxable = True
		else:
			taxable = False
			
		taxRate = taxRateFromLocation()
		if taxable == True:
			taxMultiplier = taxRate
			tax = (price * taxMultiplier)
		else:
			tax = 0
			
		return tax
		
	def taxRateFromLocation():
		if location == WestSeattle:
			taxRate = 0.96
		elif location == MercerIsland:
			taxRate = 0.95
		elif location == Bellevue:
			taxRate = 0.95
		return taxRate


if __name__ == '__main__':
    main()
