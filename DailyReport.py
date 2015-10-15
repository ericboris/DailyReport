#!/usr/local/bin/python

import calendarEvent
import os
import pyperclip
import re
#import new_job

# Create an email Form based on day's Calendar Events.

def main():
    events = calendarEvent.get_days_events()
    jobs = get_jobs(events)
    form = create_form(jobs)
    print form
    pyperclip.copy(form)

def get_jobs(events):
    jobs = []
    for event in events:
        job = {}
        job['name'] = job_name(event)
        job['tasks'] = job_tasks(event)
        job['subtotal'] = job_subtotal(job['tasks'])
        job['tax'] = job_tax(job['tasks'])
        job['total'] = job_total(job['subtotal'], job['tax'])
        jobs.append(job)
    jobs.append(day_total(jobs))
    return jobs

def job_name(event):
    return str(event.get('summary'))

def job_tasks(event):
    tasks = []
    try:
        events_list = event.get('description').splitlines()
    except AttributeError:
        return tasks
    task_keywords = ['window', 'windows', 'int', 'ext', 'out', 'skylight' 'note',
        'glass', 'rail', 'mirror', 'gutter', 'gutters', 'moss', 'debris', 'scrub',
	    'pressure', 'wash', 'pw', 'setup', 'set up', 'fb', 'facebook', 'ad', 'quote']
    keywords = re.compile('|'.join(task_keywords))
    for task in events_list:
        if len(task) <= 0 or not keywords.search(str(task).lower()):
            continue
        tasks.append(str(task))
    return tasks

def job_subtotal(tasks):
    subtotal = 0
    ignore_keywords = ['quote', 'quotes']
    keywords = re.compile('|'.join(ignore_keywords))
    for task in tasks:
        try:
            if keywords.search(str(task).lower()):
                continue
            price = int(re.search(r'\d+', task).group())
            subtotal += price
        except:
            pass
    return subtotal

def job_tax(tasks):
    tax = 0
    non_taxable_tasks = ['window', 'windows', 'skylight', 'skylights', 'note',
        'glass', 'mirror', 'mirrors', 'in/out', 'in/ext', 'int', 'ext', 'tax',
        'quote', 'quotes']
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

def job_total(subtotal, tax):
    return subtotal + tax

def day_total(jobs):
    total = 0
    for job in jobs:
         total += job['subtotal']
    day_total = {'total': total}
    return day_total

def create_form(jobs):
    form = ''
    for job in jobs:
        '''
        try:
            for key in job:

                form += '%s %s\n' % (key, job[str(key)])
            form += '\n'
        except KeyError:
            pass
        '''
        try:
            form += job['name']
            form += '\n'
        except KeyError:
            pass
        try:
            if len(job['tasks']) >= 0:
                for task in job['tasks']:
                    form += task
                    form += '\n'
        except KeyError:
            pass
        try:
            if len(job['tasks']) > 1 and job['subtotal'] != 0:
                form += 'subtotal %s' % job['subtotal']
                form += '\n'
        except KeyError:
            pass
        try:
            if job['tax'] > 0:
                form += 'tax %s ' % job['tax']
                form += '\n'
        except KeyError:
            pass
        try:
            if job['total'] > 0:
                form += 'total %s' % job['total']
                form += '\n'
            form += '\n'
        except KeyError:
            pass
    return form

if __name__ == '__main__':
    main()
