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
    #events = [{u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T09:30:00-07:00'}, u'created': u'2015-09-28T16:19:07.000Z', u'iCalUID': u'efl91fvet9hrk9qt6vvm6r9stk@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=ZWZsOTFmdmV0OWhyazlxdDZ2dm02cjlzdGsgdHdjbGxjYm9yaXNAbQ', u'sequence': 0, u'updated': u'2015-09-28T16:19:07.620Z', u'summary': u'Alex & Eric', u'start': {u'dateTime': u'2015-09-29T09:00:00-07:00'}, u'etag': u'"2886914295240000"', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'efl91fvet9hrk9qt6vvm6r9stk'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T10:30:00-07:00'}, u'description': u'ext $152', u'created': u'2015-09-22T20:43:20.000Z', u'iCalUID': u'744h7u1ogbv62be3562479u36s@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=NzQ0aDd1MW9nYnY2MmJlMzU2MjQ3OXUzNnMgdHdjbGxjYm9yaXNAbQ', u'sequence': 0, u'updated': u'2015-09-28T16:42:51.556Z', u'summary': u'Shareen Minor', u'start': {u'dateTime': u'2015-09-29T09:30:00-07:00'}, u'etag': u'"2886917143112000"', u'location': u'4530 48th Ave SW 98116', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'744h7u1ogbv62be3562479u36s'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T12:00:00-07:00'}, u'description': u"Gutters 255\nIf 28' is too short access upper roof along ridgeline on front of house and rope over both sides", u'created': u'2015-09-23T23:57:43.000Z', u'iCalUID': u'g116rp53esfohuh6rbq7dp34uc@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=ZzExNnJwNTNlc2ZvaHVoNnJicTdkcDM0dWMgdHdjbGxjYm9yaXNAbQ', u'sequence': 0, u'updated': u'2015-09-28T16:42:58.734Z', u'summary': u'Don Moddell', u'start': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T11:00:00-07:00'}, u'etag': u'"2886917157468000"', u'location': u'1902 45th ave sw 98116', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'Matt Bay', u'email': u'mercerwindows@gmail.com'}, u'id': u'g116rp53esfohuh6rbq7dp34uc'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T12:30:00-07:00'}, u'created': u'2015-09-25T23:25:46.000Z', u'iCalUID': u'6nlsp0dhuiou2kdc5h988unqro@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=Nm5sc3AwZGh1aW91MmtkYzVoOTg4dW5xcm9fMjAxNTA5MjlUMTkwMDAwWiB0d2NsbGNib3Jpc0Bt', u'sequence': 0, u'updated': u'2015-10-02T15:43:09.581Z', u'summary': u'Eric Lunch', u'start': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T12:00:00-07:00'}, u'etag': u'"2887601179162000"', u'originalStartTime': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T12:00:00-07:00'}, u'recurringEventId': u'6nlsp0dhuiou2kdc5h988unqro', u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'6nlsp0dhuiou2kdc5h988unqro_20150929T190000Z'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T14:00:00-07:00'}, u'description': u'ext windows $244 ', u'created': u'2015-09-24T18:16:48.000Z', u'iCalUID': u'eces7b566q1jfugo9r311he210@google.com', u'reminders': {u'overrides': [{u'minutes': 30, u'method': u'popup'}, {u'minutes': 10, u'method': u'popup'}], u'useDefault': False}, u'htmlLink': u'https://www.google.com/calendar/event?eid=ZWNlczdiNTY2cTFqZnVnbzlyMzExaGUyMTAgdHdjbGxjYm9yaXNAbQ', u'sequence': 1, u'updated': u'2015-09-29T23:49:51.862Z', u'summary': u'Angela Gasperetti', u'start': {u'dateTime': u'2015-09-29T12:30:00-07:00'}, u'etag': u'"2887141183456000"', u'location': u'1321 42nd Ave SW 98116', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'eces7b566q1jfugo9r311he210'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T15:00:00-07:00'}, u'description': u'ext windows $125\n\nalready paid via credit card\n206-229-2446', u'created': u'2015-09-26T00:13:33.000Z', u'iCalUID': u't9mce3nem0t709g9bajpcaijks@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=dDltY2UzbmVtMHQ3MDlnOWJhanBjYWlqa3MgdHdjbGxjYm9yaXNAbQ', u'sequence': 1, u'updated': u'2015-09-29T16:12:22.684Z', u'summary': u'Kendra Yaple', u'start': {u'dateTime': u'2015-09-29T14:00:00-07:00'}, u'etag': u'"2887086285368000"', u'location': u'4932 Erskine Wy SW 98116', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u't9mce3nem0t709g9bajpcaijks'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T17:00:00-07:00'}, u'description': u"ext windows $338\n\nDI's can be used\n\n206-403-1317", u'created': u'2015-09-28T16:41:09.000Z', u'iCalUID': u'6t6eh4dkpg3u3e3vgb519o5mm4@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=NnQ2ZWg0ZGtwZzN1M2UzdmdiNTE5bzVtbTQgdHdjbGxjYm9yaXNAbQ', u'sequence': 2, u'updated': u'2015-09-29T18:35:50.401Z', u'summary': u'Terry Gibbons', u'start': {u'dateTime': u'2015-09-29T15:00:00-07:00'}, u'etag': u'"2887103500802000"', u'location': u'3701 E Garfield St 98112', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'6t6eh4dkpg3u3e3vgb519o5mm4'}]
    #return events
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    today = datetime.datetime.today()# - datetime.timedelta(days=0)
    dayStart = today.replace(hour=00, minute=00, second=01).isoformat() + 'Z'
    dayEnd = today.replace(hour=23, minute=59, second=59).isoformat() + 'Z'
    eventsResult = service.events().list(
        calendarId='primary', timeMin=dayStart, singleEvents=True,
        orderBy='startTime', timeMax=dayEnd).execute()
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
    #print eventList
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

def get_work_day():
    return dayStart

if __name__ == '__main__':
    main()
