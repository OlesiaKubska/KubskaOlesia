from __future__ import print_function
import datetime
import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.events']


def authenticate_google_calendar():
    creds = None
    token_path = 'token.pickle'
    credentials_path = 'src/credentials/credentials.json'

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def create_calendar_event(summary="Family Board Game Time", description="Fun time!", start_time=None, end_time=None):
    creds = authenticate_google_calendar()
    service = build('calendar', 'v3', credentials=creds)

    if start_time is None or end_time is None:
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.isoformat()
        end_time = (now + datetime.timedelta(hours=1)).isoformat()

    event = {
        'summary': f'🧒 {summary}',
        'location': 'Home',
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Europe/Warsaw',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Europe/Warsaw',
        },
        'reminders': {
            'useDefault': True,
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"✅ Event created: {event.get('htmlLink')}")


if __name__ == '__main__':
    create_calendar_event()