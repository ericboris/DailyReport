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
    day_total = create_day_total(jobs)
    jobs.append(day_total)
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

def create_day_total(jobs):
    total = 0
    for job in jobs:
         total += job['subtotal']
    day_total = {'total': total}
    return day_total

def create_form(jobs):
    form = ''
    for job in jobs:
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
            if len(job['tasks']) > 1:
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
