import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from groq import Groq

# === YOUR KEYS ===
GROQ_API_KEY = "your-groq-api-key-here"

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# === CONNECT TO GMAIL ===
def connect_to_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(r'C:\Users\Abhishek\Documents\email-agent\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

# === FETCH EMAILS ===
def get_recent_emails(service, max_emails=25):
    results = service.users().messages().list(userId='me', maxResults=max_emails, q='newer_than:2d').execute()
    messages = results.get('messages', [])

    emails = []
    for msg in messages:
        full_msg = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = full_msg['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')

        body = ""
        payload = full_msg.get('payload', {})
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    data = part['body'].get('data', '')
                    body = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')[:300]
                    break

        emails.append(f"FROM: {sender}\nSUBJECT: {subject}\nPREVIEW: {body}\n---")

    return emails

# === ASK GROQ TO SUMMARIZE ===
def summarize_with_groq(emails):
    client = Groq(api_key=GROQ_API_KEY)
    email_text = "\n".join(emails)

    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""You are my personal job search assistant. I am actively applying for jobs and networking.

Here are my recent emails. Please give me:
1. 📊 QUICK STATS — How many job, networking, rejection, or interview emails?
2. 🔥 URGENT — What needs my attention TODAY
3. 💼 APPLICATIONS — Any updates on jobs I applied to
4. 🌱 NETWORKING — Who reached out, who I should follow up with
5. ✅ MY TOP 3 ACTION ITEMS for today

Emails:
{email_text}"""
            }
        ]
    )
    return chat.choices[0].message.content

# === RUN ===
def main():
    print("🤖 Starting Email Agent...")
    print("📬 Connecting to Gmail...")
    service = connect_to_gmail()

    print("📧 Fetching recent emails...")
    emails = get_recent_emails(service)

    if not emails:
        print("No emails found from the last 2 days!")
        return

    print(f"✅ Found {len(emails)} emails. Analyzing with Groq AI...")
    summary = summarize_with_groq(emails)

    print("\n" + "="*50)
    print("📋 YOUR DAILY EMAIL BRIEFING")
    print("="*50 + "\n")
    print(summary)

if __name__ == "__main__":
    main()