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


def get_days_events():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    #now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    #print now
    today = datetime.datetime.today()
    thisMorning = today.replace(hour=00, minute=00, second=01).isoformat() + 'Z'
    thisEvening = today.replace(hour=23, minute=59, second=59).isoformat() + 'Z'
    eventsResult = service.events().list(
        calendarId='primary', timeMin=thisMorning, singleEvents=True,
        orderBy='startTime', timeMax=thisEvening).execute()
    events = eventsResult.get('items', [])

    if not events:
        print 'No upcoming events found.'
    eventList = []
    for event in events:
        eventList.append(event)

    # Present for testing
    #eventList = [{u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-07-29T19:00:00-07:00'}, u'description': u'in out 200\nroof moss 90\ngutters 214\npw siding 110', u'created': u'2015-07-27T20:25:23.000Z', u'iCalUID': u'0sjg1j0q57s97i3hsleu66nni4@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=MHNqZzFqMHE1N3M5N2kzaHNsZXU2Nm5uaTQgdGhlLmVyaWMuYm9yaXNAbQ', u'sequence': 0, u'updated': u'2015-07-27T20:25:23.718Z', u'summary': u'nick d', u'start': {u'dateTime': u'2015-07-29T18:00:00-07:00'}, u'etag': u'"2876057447436000"', u'location': u'34th Ave SW, Seattle, WA, USA', u'organizer': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'creator': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'id': u'0sjg1j0q57s97i3hsleu66nni4'},
    #{u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-07-29T20:00:00-07:00'}, u'description': u'pw deck 100\ngutters 90', u'created': u'2015-07-27T20:24:31.000Z', u'iCalUID': u'1q3nu70dssmcjiibu8v2c4s6q8@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=MXEzbnU3MGRzc21jamlpYnU4djJjNHM2cTggdGhlLmVyaWMuYm9yaXNAbQ', u'sequence': 1, u'updated': u'2015-07-27T20:24:34.304Z', u'summary': u'Cobol Jones', u'start': {u'dateTime': u'2015-07-29T19:00:00-07:00'}, u'etag': u'"2876057348608000"', u'location': u'123 Prospect St, Seattle, WA 98109, USA', u'organizer': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'creator': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'id': u'1q3nu70dssmcjiibu8v2c4s6q8'},
    #{u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-07-29T21:00:00-07:00'}, u'description': u'windows in out 150\nroof moss 100\ngutters 80\npw deck 100\nnote this is a note', u'created': u'2015-07-25T21:18:28.000Z', u'iCalUID': u'pc098deg0u4p0ff80675hqq3hk@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=cGMwOThkZWcwdTRwMGZmODA2NzVocXEzaGsgdGhlLmVyaWMuYm9yaXNAbQ', u'sequence': 2, u'updated': u'2015-07-27T20:23:52.574Z', u'summary': u'John Apple', u'start': {u'dateTime': u'2015-07-29T20:00:00-07:00'}, u'etag': u'"2876057265148000"', u'location': u'4501 SW Admiral Way, Seattle, WA 98116, USA', u'organizer': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'creator': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'id': u'pc098deg0u4p0ff80675hqq3hk'}]

    return eventList

def get_credentials():
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
        else:
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials


if __name__ == '__main__':
    main()
