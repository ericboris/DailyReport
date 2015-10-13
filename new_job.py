import re

#take list of jobs

#loop jobs in list
    #get job name(event)
    #get job tasks
    #create job subtotal
    #create job tax
    #create job total

'''events = [{u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-07-29T19:00:00-07:00'}, u'description': u'in out 200\nroof moss 90\ngutters 214\npw siding 110\n\n206-707-6793', u'created': u'2015-07-27T20:25:23.000Z', u'iCalUID': u'0sjg1j0q57s97i3hsleu66nni4@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=MHNqZzFqMHE1N3M5N2kzaHNsZXU2Nm5uaTQgdGhlLmVyaWMuYm9yaXNAbQ', u'sequence': 0, u'updated': u'2015-07-27T20:25:23.718Z', u'summary': u'nick d', u'start': {u'dateTime': u'2015-07-29T18:00:00-07:00'}, u'etag': u'"2876057447436000"', u'location': u'34th Ave SW, Seattle, WA, USA', u'organizer': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'creator': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'id': u'0sjg1j0q57s97i3hsleu66nni4'},
{u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-07-29T20:00:00-07:00'}, u'description': u'pw deck 100\ngutters 90', u'created': u'2015-07-27T20:24:31.000Z', u'iCalUID': u'1q3nu70dssmcjiibu8v2c4s6q8@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=MXEzbnU3MGRzc21jamlpYnU4djJjNHM2cTggdGhlLmVyaWMuYm9yaXNAbQ', u'sequence': 1, u'updated': u'2015-07-27T20:24:34.304Z', u'summary': u'Cobol Jones', u'start': {u'dateTime': u'2015-07-29T19:00:00-07:00'}, u'etag': u'"2876057348608000"', u'location': u'123 Prospect St, Seattle, WA 98109, USA', u'organizer': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'creator': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'id': u'1q3nu70dssmcjiibu8v2c4s6q8'},
{u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-07-29T21:00:00-07:00'}, u'description': u'windows in out 150\nroof moss 100\ngutters 80\npw deck 100\nnote this is a note', u'created': u'2015-07-25T21:18:28.000Z', u'iCalUID': u'pc098deg0u4p0ff80675hqq3hk@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=cGMwOThkZWcwdTRwMGZmODA2NzVocXEzaGsgdGhlLmVyaWMuYm9yaXNAbQ', u'sequence': 2, u'updated': u'2015-07-27T20:23:52.574Z', u'summary': u'John Apple', u'start': {u'dateTime': u'2015-07-29T20:00:00-07:00'}, u'etag': u'"2876057265148000"', u'location': u'4501 SW Admiral Way, Seattle, WA 98116, USA', u'organizer': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'creator': {u'self': True, u'displayName': u'Eric Boris', u'email': u'the.eric.boris@gmail.com'}, u'id': u'pc098deg0u4p0ff80675hqq3hk'}]
'''

#events = [{u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-10-08T18:00:00-07:00'}, u'description': u'Help Cass with last job of day', u'created': u'2015-10-08T16:13:53.000Z', u'iCalUID': u'k0jsqc7hlj0aoufvqa3qu6psf8@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=azBqc3FjN2hsajBhb3VmdnFhM3F1NnBzZjggdHdjbGxjYm9yaXNAbQ', u'sequence': 1, u'updated': u'2015-10-08T22:47:56.376Z', u'summary': u"Celia O'Kane", u'start': {u'dateTime': u'2015-10-08T16:00:00-07:00'}, u'etag': u'"2888688952752000"', u'location': u'8020 84th Ave SE 98040', u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'k0jsqc7hlj0aoufvqa3qu6psf8'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-10-08T19:10:00-07:00'}, u'description': u'deposit ', u'created': u'2015-07-18T15:15:30.000Z', u'iCalUID': u'i492nnvavifitkkjpbd9rav2mg@google.com', u'reminders': {u'useDefault': False}, u'htmlLink': u'https://www.google.com/calendar/event?eid=aTQ5Mm5udmF2aWZpdGtranBiZDlyYXYybWdfMjAxNTEwMDlUMDIwMDAwWiB0d2NsbGNib3Jpc0Bt', u'sequence': 0, u'updated': u'2015-09-10T21:32:35.931Z', u'summary': u'Deposit Checks', u'start': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-10-08T19:00:00-07:00'}, u'etag': u'"2883841511744000"', u'originalStartTime': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-10-08T19:00:00-07:00'}, u'recurringEventId': u'i492nnvavifitkkjpbd9rav2mg', u'organizer': {u'self': True, u'displayName': u'Eric Boris', u'email': u'twcllcboris@gmail.com'}, u'creator': {u'self': True, u'displayName': u'Eric Boris', u'email': u'twcllcboris@gmail.com'}, u'id': u'i492nnvavifitkkjpbd9rav2mg_20151009T020000Z'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-10-09T13:30:00-07:00'}, u'description': u'windows in/out $283\ngutters $185\n\n206-933-5564', u'created': u'2015-10-08T17:42:32.000Z', u'iCalUID': u'c5f4snantt0ss1cesob2jheaho@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=YzVmNHNuYW50dDBzczFjZXNvYjJqaGVhaG8gdHdjbGxjYm9yaXNAbQ', u'sequence': 2, u'updated': u'2015-10-09T21:17:55.560Z', u'summary': u'Dawn Dort', u'start': {u'dateTime': u'2015-10-09T10:00:00-07:00'}, u'etag': u'"2888850951120000"', u'location': u'4037 41st Ave SW 98116', u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'c5f4snantt0ss1cesob2jheaho'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-10-09T14:30:00-07:00'}, u'description': u'ext windows\n\n206-937-1166', u'created': u'2015-10-09T00:32:07.000Z', u'iCalUID': u'20l6opvsg3lehl7b0bunk0b2bc@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=MjBsNm9wdnNnM2xlaGw3YjBidW5rMGIyYmMgdHdjbGxjYm9yaXNAbQ', u'sequence': 3, u'updated': u'2015-10-09T21:17:58.535Z', u'summary': u'Quote Natalie Williams-Have Aiko Call On Your Way', u'start': {u'dateTime': u'2015-10-09T14:00:00-07:00'}, u'etag': u'"2888850957070000"', u'location': u'5627 47th Ave SW 98136', u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'20l6opvsg3lehl7b0bunk0b2bc'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-10-09T16:00:00-07:00'}, u'description': u'ext window $137\n\n206-937-1166\n\neric did quote', u'created': u'2015-10-09T21:18:43.000Z', u'iCalUID': u'i716dae4h4eltc237sgtd7q0fc@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=aTcxNmRhZTRoNGVsdGMyMzdzZ3RkN3EwZmMgdHdjbGxjYm9yaXNAbQ', u'sequence': 0, u'updated': u'2015-10-09T21:18:43.287Z', u'summary': u'Natalie Williams', u'start': {u'dateTime': u'2015-10-09T14:30:00-07:00'}, u'etag': u'"2888851046574000"', u'location': u'5627 47th Ave SW 98136', u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'i716dae4h4eltc237sgtd7q0fc'}]
events = [{u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T09:30:00-07:00'}, u'created': u'2015-09-28T16:19:07.000Z', u'iCalUID': u'efl91fvet9hrk9qt6vvm6r9stk@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=ZWZsOTFmdmV0OWhyazlxdDZ2dm02cjlzdGsgdHdjbGxjYm9yaXNAbQ', u'sequence': 0, u'updated': u'2015-09-28T16:19:07.620Z', u'summary': u'Alex & Eric', u'start': {u'dateTime': u'2015-09-29T09:00:00-07:00'}, u'etag': u'"2886914295240000"', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'efl91fvet9hrk9qt6vvm6r9stk'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T10:30:00-07:00'}, u'description': u'ext $152', u'created': u'2015-09-22T20:43:20.000Z', u'iCalUID': u'744h7u1ogbv62be3562479u36s@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=NzQ0aDd1MW9nYnY2MmJlMzU2MjQ3OXUzNnMgdHdjbGxjYm9yaXNAbQ', u'sequence': 0, u'updated': u'2015-09-28T16:42:51.556Z', u'summary': u'Shareen Minor', u'start': {u'dateTime': u'2015-09-29T09:30:00-07:00'}, u'etag': u'"2886917143112000"', u'location': u'4530 48th Ave SW 98116', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'744h7u1ogbv62be3562479u36s'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T12:00:00-07:00'}, u'description': u"Gutters 255\nIf 28 is too short access upper roof along ridgeline on front of house and rope over both sides", u'created': u'2015-09-23T23:57:43.000Z', u'iCalUID': u'g116rp53esfohuh6rbq7dp34uc@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=ZzExNnJwNTNlc2ZvaHVoNnJicTdkcDM0dWMgdHdjbGxjYm9yaXNAbQ', u'sequence': 0, u'updated': u'2015-09-28T16:42:58.734Z', u'summary': u'Don Moddell', u'start': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T11:00:00-07:00'}, u'etag': u'"2886917157468000"', u'location': u'1902 45th ave sw 98116', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'Matt Bay', u'email': u'mercerwindows@gmail.com'}, u'id': u'g116rp53esfohuh6rbq7dp34uc'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T12:30:00-07:00'}, u'created': u'2015-09-25T23:25:46.000Z', u'iCalUID': u'6nlsp0dhuiou2kdc5h988unqro@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=Nm5sc3AwZGh1aW91MmtkYzVoOTg4dW5xcm9fMjAxNTA5MjlUMTkwMDAwWiB0d2NsbGNib3Jpc0Bt', u'sequence': 0, u'updated': u'2015-10-02T15:43:09.581Z', u'summary': u'Eric Lunch', u'start': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T12:00:00-07:00'}, u'etag': u'"2887601179162000"', u'originalStartTime': {u'timeZone': u'America/Los_Angeles', u'dateTime': u'2015-09-29T12:00:00-07:00'}, u'recurringEventId': u'6nlsp0dhuiou2kdc5h988unqro', u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'6nlsp0dhuiou2kdc5h988unqro_20150929T190000Z'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T14:00:00-07:00'}, u'description': u'ext windows $244 ', u'created': u'2015-09-24T18:16:48.000Z', u'iCalUID': u'eces7b566q1jfugo9r311he210@google.com', u'reminders': {u'overrides': [{u'minutes': 30, u'method': u'popup'}, {u'minutes': 10, u'method': u'popup'}], u'useDefault': False}, u'htmlLink': u'https://www.google.com/calendar/event?eid=ZWNlczdiNTY2cTFqZnVnbzlyMzExaGUyMTAgdHdjbGxjYm9yaXNAbQ', u'sequence': 1, u'updated': u'2015-09-29T23:49:51.862Z', u'summary': u'Angela Gasperetti', u'start': {u'dateTime': u'2015-09-29T12:30:00-07:00'}, u'etag': u'"2887141183456000"', u'location': u'1321 42nd Ave SW 98116', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'eces7b566q1jfugo9r311he210'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T15:00:00-07:00'}, u'description': u'ext windows $125\n\nalready paid via credit card\n206-229-2446', u'created': u'2015-09-26T00:13:33.000Z', u'iCalUID': u't9mce3nem0t709g9bajpcaijks@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=dDltY2UzbmVtMHQ3MDlnOWJhanBjYWlqa3MgdHdjbGxjYm9yaXNAbQ', u'sequence': 1, u'updated': u'2015-09-29T16:12:22.684Z', u'summary': u'Kendra Yaple', u'start': {u'dateTime': u'2015-09-29T14:00:00-07:00'}, u'etag': u'"2887086285368000"', u'location': u'4932 Erskine Wy SW 98116', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u't9mce3nem0t709g9bajpcaijks'}, {u'status': u'confirmed', u'kind': u'calendar#event', u'end': {u'dateTime': u'2015-09-29T17:00:00-07:00'}, u'description': u"ext windows $338\n\nDI's can be used\n\n206-403-1317", u'created': u'2015-09-28T16:41:09.000Z', u'iCalUID': u'6t6eh4dkpg3u3e3vgb519o5mm4@google.com', u'reminders': {u'useDefault': True}, u'htmlLink': u'https://www.google.com/calendar/event?eid=NnQ2ZWg0ZGtwZzN1M2UzdmdiNTE5bzVtbTQgdHdjbGxjYm9yaXNAbQ', u'sequence': 2, u'updated': u'2015-09-29T18:35:50.401Z', u'summary': u'Terry Gibbons', u'start': {u'dateTime': u'2015-09-29T15:00:00-07:00'}, u'etag': u'"2887103500802000"', u'location': u'3701 E Garfield St 98112', u'attendees': [{u'email': u'twcllclong@gmail.com', u'responseStatus': u'needsAction'}, {u'responseStatus': u'accepted', u'organizer': True, u'email': u'twcllcboris@gmail.com', u'self': True}], u'organizer': {u'self': True, u'email': u'twcllcboris@gmail.com'}, u'creator': {u'displayName': u'The Window Cleaners LLC', u'email': u'twcllcoffice@gmail.com'}, u'id': u'6t6eh4dkpg3u3e3vgb519o5mm4'}]

def main():
    get_jobs(events)

def get_jobs(events):
    jobs = []
    for event in events:
        job_name = get_job_name(event)
        job_tasks = get_job_tasks(event)
        job_subtotal = create_job_subtotal(job_tasks)
        job_tax = create_job_tax(job_tasks)
        job_total = create_job_total(job_subtotal, job_tax)
        job = {'name': job_name,
            'tasks': job_tasks,
            'subtotal': job_subtotal,
            'tax': job_tax,
            'total': job_total}
        jobs.append(job)
    return jobs

def get_job_name(event):
    return str(event.get('summary'))

def get_job_tasks(event):
    tasks = []
    try:
        events_list = event.get('description').splitlines()
    except AttributeError:
        return tasks
    for task in events_list:
        task = str(task).lower()
        # progressively filter each line in events into tasks
        # remove empty lines
        if len(task) <= 0:
            continue
        # filtering out for keywords seems to implicitly filter telephone numbers as well
        # remove telephone numbers
        #tel_num = re.compile(".*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?", re.S) # telepone number
        #if tel_num.match(task):
        #    continue
        # remove lines not containing keywords
        task_keywords = ['window', 'windows', 'int', 'ext', 'out', 'skylight' 'note',
            'glass', 'rail', 'mirror', 'gutter', 'gutters', 'moss', 'debris', 'scrub',
    	    'pressure', 'wash', 'pw', 'setup', 'set up', 'fb', 'facebook', 'ad']
        keywords = re.compile('|'.join(task_keywords))
        if not keywords.search(task):
            continue
        # if the line is not blank and contains a keyword
        tasks.append(str(task))
    return tasks

def create_job_subtotal(tasks):
    subtotal = 0
    for task in tasks:
        try:
            price = int(re.search(r'\d+', task).group())
            subtotal += price
        except:
            pass
    return subtotal

def create_job_tax(tasks):
    tax = 0
    non_taxable_tasks = ['window', 'windows', 'skylight', 'skylights', 'note',
        'glass', 'mirror', 'mirrors', 'in/out', 'in/ext', 'int', 'ext', 'tax']
    for task in tasks:
        # remove non taxable tasks
        keywords = re.compile('|'.join(non_taxable_tasks))
        if keywords.search(task):
            continue
        try:
            price = int(re.search(r'\d+', task).group())
            tax += price
        except:
            pass
    taxRate = 0.096
    tax *= taxRate
    return round(tax, 2)

def create_job_total(subtotal, tax):
    return subtotal + tax

if __name__ == "__main__":
    main()
