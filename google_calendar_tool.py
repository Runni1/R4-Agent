from __future__ import print_function
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_service():
    creds = None

    # kalau sudah ada token.json, pakai itu
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # kalau belum ada token, atau token invalid → ulang login Google
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # simpan token biar ga login berkali-kali
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)
    return service


def add_event(title, date):
    """Menambahkan event ke Google Calendar kamu"""
    service = get_service()

    event = {
        'summary': title,
        'start': {
            'date': date,
            'timeZone': 'Asia/Jakarta',
        },
        'end': {
            'date': date,
            'timeZone': 'Asia/Jakarta',
        }
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    return f"Berhasil menambahkan jadwal '{title}' di tanggal {date} ke Google Calendar! ✨"


def show_events():
    """Menampilkan 10 jadwal mendatang"""
    service = get_service()
    now = datetime.datetime.utcnow().isoformat() + "Z"

    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])

    if not events:
        return "Tidak ada jadwal mendatang."

    result = "📅 Jadwal Mendatang di Google Calendar:\n"
    for event in events:
        start = event['start'].get('date')
        summary = event['summary']
        result += f"- {start}: {summary}\n"

    return result
