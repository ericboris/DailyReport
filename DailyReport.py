from calendarEvent import get_days_events
from form import Form
import os
import pyperclip

# Create an email Form based on day's Calendar Events.

def main():
    events = get_days_events()
    f = Form(events)
    # copy f.form to clipboard
    print f.form
    pyperclip.copy(f.form)

if __name__ == '__main__':
    main()
