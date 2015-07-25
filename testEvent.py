event = {
    "nextPageToken": "A String", # Token used to access the next page of this result. Omitted if no further results are available, in which case nextSyncToken is provided.
    "kind": "calendar#events", # Type of the collection ("calendar#events").
    "defaultReminders": [ # The default reminders on the calendar for the authenticated user. These reminders apply to all events on this calendar that do not explicitly override them (i.e. do not have reminders.useDefault set to True).
      {
        "minutes": 42, # Number of minutes before the start of the event when the reminder should trigger.
        "method": "A String", # The method used by this reminder. Possible values are:
            # - "email" - Reminders are sent via email.
            # - "sms" - Reminders are sent via SMS.
            # - "popup" - Reminders are sent via a UI popup.
      },
    ],
    "description": "A String", # Description of the calendar. Read-only.
    "items": [ # List of events on the calendar.
      {
          "attachments": [ # File attachments for the event. Currently only Google Drive attachments are supported.
              # In order to modify attachments the supportsAttachments request parameter should be set to True.
              # There can be at most 25 attachments per event,
            {
              "mimeType": "A String", # Internet media type (MIME type) of the attachment.
              "fileUrl": "A String", # URL link to the attachment.
                  # For adding Google Drive file attachments use the same format as in alternateLink property of the Files resource in the Drive API.
              "iconLink": "A String", # URL link to the attachment's icon. Read-only.
              "fileId": "A String", # ID of the attached file. Read-only.
                  # E.g. for Google Drive files this is the ID of the corresponding Files resource entry in the Drive API.
              "title": "A String", # Attachment title.
            },
          ],
          "creator": { # The creator of the event. Read-only.
            "self": False, # Whether the creator corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.
            "displayName": "A String", # The creator's name, if available.
            "email": "A String", # The creator's email address, if available.
            "id": "A String", # The creator's Profile ID, if available.
          },
          "originalStartTime": { # For an instance of a recurring event, this is the time at which this event would start according to the recurrence data in the recurring event identified by recurringEventId. Immutable.
            "date": "A String", # The date, in the format "yyyy-mm-dd", if this is an all-day event.
            "timeZone": "A String", # The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end.
            "dateTime": "A String", # The time, as a combined date-time value (formatted according to RFC 3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.
          },
          "organizer": { # The organizer of the event. If the organizer is also an attendee, this is indicated with a separate entry in attendees with the organizer field set to True. To change the organizer, use the move operation. Read-only, except when importing an event.
            "self": False, # Whether the organizer corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.
            "displayName": "A String", # The organizer's name, if available.
            "email": "A String", # The organizer's email address, if available.
            "id": "A String", # The organizer's Profile ID, if available.
          },
          "id": "Jim String", # Identifier of the event. When creating new single or recurring events, you can specify their IDs. Provided IDs must follow these rules:
              # - characters allowed in the ID are those used in base32hex encoding, i.e. lowercase letters a-v and digits 0-9, see section 3.1.2 in RFC2938
              # - the length of the ID must be between 5 and 1024 characters
              # - the ID must be unique per calendar  Due to the globally distributed nature of the system, we cannot guarantee that ID collisions will be detected at event creation time. To minimize the risk of collisions we recommend using an established UUID algorithm such as one described in RFC4122.
          "hangoutLink": "A String", # An absolute link to the Google+ hangout associated with this event. Read-only.
          "attendees": [ # The attendees of the event.
            {
              "comment": "A String", # The attendee's response comment. Optional.
              "displayName": "A String", # The attendee's name, if available. Optional.
              "self": False, # Whether this entry represents the calendar on which this copy of the event appears. Read-only. The default is False.
              "id": "A String", # The attendee's Profile ID, if available.
              "email": "A String", # The attendee's email address, if available. This field must be present when adding an attendee.
              "additionalGuests": 0, # Number of additional guests. Optional. The default is 0.
              "resource": False, # Whether the attendee is a resource. Read-only. The default is False.
              "organizer": True or False, # Whether the attendee is the organizer of the event. Read-only. The default is False.
              "optional": False, # Whether this is an optional attendee. Optional. The default is False.
              "responseStatus": "A String", # The attendee's response status. Possible values are:
                  # - "needsAction" - The attendee has not responded to the invitation.
                  # - "declined" - The attendee has declined the invitation.
                  # - "tentative" - The attendee has tentatively accepted the invitation.
                  # - "accepted" - The attendee has accepted the invitation.
            },
          ],
          "source": { # Source of an event from which it was created; for example a web page, an email message or any document identifiable by an URL using HTTP/HTTPS protocol. Accessible only by the creator of the event.
            "url": "A String", # URL of the source pointing to a resource. URL's protocol must be HTTP or HTTPS.
            "title": "A String", # Title of the source; for example a title of a web page or an email subject.
          },
          "htmlLink": "A String", # An absolute link to this event in the Google Calendar Web UI. Read-only.
          "recurrence": [ # List of RRULE, EXRULE, RDATE and EXDATE lines for a recurring event. This field is omitted for single events or instances of recurring events.
            "A String",
          ],
          "start": { # The (inclusive) start time of the event. For a recurring event, this is the start time of the first instance.
            "date": "2015-07-18", # The date, in the format "yyyy-mm-dd", if this is an all-day event.
            "timeZone": "A String", # The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end.
            "dateTime": "Noonstring", # The time, as a combined date-time value (formatted according to RFC 3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.
          },
          "etag": "A String", # ETag of the resource.
          "location": "4501 SW String 98116", # Geographic location of the event as free-form text. Optional.
          "recurringEventId": "A String", # For an instance of a recurring event, this is the event ID of the recurring event itself. Immutable.
          "extendedProperties": { # Extended properties of the event.
            "shared": { # Properties that are shared between copies of the event on other attendees' calendars.
              "a_key": "A String", # The name of the shared property and the corresponding value.
            },
            "private": { # Properties that are private to the copy of the event that appears on this calendar.
              "a_key": "A String", # The name of the private property and the corresponding value.
            },
          },
          "status": "A String", # Status of the event. Optional. Possible values are:
              # - "confirmed" - The event is confirmed. This is the default status.
              # - "tentative" - The event is tentatively confirmed.
              # - "cancelled" - The event is cancelled.
          "updated": "A String", # Last modification time of the event (as a RFC 3339 timestamp). Read-only.
          "description": "in out 215 pw drive 200 roof moss 185 String", # Description of the event. Optional.
          "iCalUID": "A String", # Event ID in the iCalendar format.
          "gadget": { # A gadget that extends this event.
            "preferences": { # Preferences.
              "a_key": "A String", # The preference name and corresponding value.
            },
            "title": "A String", # The gadget's title.
            "height": 42, # The gadget's height in pixels. Optional.
            "width": 42, # The gadget's width in pixels. Optional.
            "link": "A String", # The gadget's URL.
            "type": "A String", # The gadget's type.
            "display": "A String", # The gadget's display mode. Optional. Possible values are:
                # - "icon" - The gadget displays next to the event's title in the calendar view.
                # - "chip" - The gadget displays when the event is clicked.
            "iconLink": "A String", # The gadget's icon URL.
          },
          "endTimeUnspecified": False, # Whether the end time is actually unspecified. An end time is still provided for compatibility reasons, even if this attribute is set to True. The default is False.
          "sequence": 42, # Sequence number as per iCalendar.
          "visibility": "default", # Visibility of the event. Optional. Possible values are:
              # - "default" - Uses the default visibility for events on the calendar. This is the default value.
              # - "public" - The event is public and event details are visible to all readers of the calendar.
              # - "private" - The event is private and only event attendees may view event details.
              # - "confidential" - The event is private. This value is provided for compatibility reasons.
          "guestsCanModify": False, # Whether attendees other than the organizer can modify the event. Optional. The default is False.
          "end": { # The (exclusive) end time of the event. For a recurring event, this is the end time of the first instance.
            "date": "2015-07-18", # The date, in the format "yyyy-mm-dd", if this is an all-day event.
            "timeZone": "A String", # The time zone in which the time is specified. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) For recurring events this field is required and specifies the time zone in which the recurrence is expanded. For single events this field is optional and indicates a custom time zone for the event start/end.
            "dateTime": "Afterstring", # The time, as a combined date-time value (formatted according to RFC 3339). A time zone offset is required unless a time zone is explicitly specified in timeZone.
          },
          "attendeesOmitted": False, # Whether attendees may have been omitted from the event's representation. When retrieving an event, this may be due to a restriction specified by the maxAttendee query parameter. When updating an event, this can be used to only update the participant's response. Optional. The default is False.
          "kind": "calendar#event", # Type of the resource ("calendar#event").
          "locked": False, # Whether this is a locked event copy where no changes can be made to the main event fields "summary", "description", "location", "start", "end" or "recurrence". The default is False. Read-Only.
          "created": "A String", # Creation time of the event (as a RFC 3339 timestamp). Read-only.
          "colorId": "A String", # The color of the event. This is an ID referring to an entry in the event section of the colors definition (see the  colors endpoint). Optional.
          "anyoneCanAddSelf": False, # Whether anyone can invite themselves to the event. Optional. The default is False.
          "reminders": { # Information about the event's reminders for the authenticated user.
            "overrides": [ # If the event doesn't use the default reminders, this lists the reminders specific to the event, or, if not set, indicates that no reminders are set for this event.
              {
                "minutes": 42, # Number of minutes before the start of the event when the reminder should trigger.
                "method": "A String", # The method used by this reminder. Possible values are:
                    # - "email" - Reminders are sent via email.
                    # - "sms" - Reminders are sent via SMS.
                    # - "popup" - Reminders are sent via a UI popup.
              },
            ],
            "useDefault": True or False, # Whether the default reminders of the calendar apply to the event.
          },
          "guestsCanSeeOtherGuests": True, # Whether attendees other than the organizer can see who the event's attendees are. Optional. The default is True.
          "summary": "A String", # Title of the event.
          "guestsCanInviteOthers": True, # Whether attendees other than the organizer can invite others to the event. Optional. The default is True.
          "transparency": "opaque", # Whether the event blocks time on the calendar. Optional. Possible values are:
              # - "opaque" - The event blocks time on the calendar. This is the default value.
              # - "transparent" - The event does not block time on the calendar.
          "privateCopy": False, # Whether this is a private event copy where changes are not shared with other copies on other calendars. Optional. Immutable. The default is False.
        },
    ],
    "updated": "A String", # Last modification time of the calendar (as a RFC 3339 timestamp). Read-only.
    "summary": "A String", # Title of the calendar. Read-only.
    "etag": "A String", # ETag of the collection.
    "nextSyncToken": "A String", # Token used at a later point in time to retrieve only the entries that have changed since this result was returned. Omitted if further results are available, in which case nextPageToken is provided.
    "timeZone": "A String", # The time zone of the calendar. Read-only.
    "accessRole": "A String", # The user's access role for this calendar. Read-only. Possible values are:
        # - "none" - The user has no access.
        # - "freeBusyReader" - The user has read access to free/busy information.
        # - "reader" - The user has read access to the calendar. Private events will appear to users with reader access, but event details will be hidden.
        # - "writer" - The user has read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible.
        # - "owner" - The user has ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs.
  }
