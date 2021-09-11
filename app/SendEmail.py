from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Send(email_to, email_from, email_subject, email_message):
    CLIENT_SECRET_FILE = 'credentials/credentials.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']

    print('SEND_EMAIL')

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = email_to
    mimeMessage['from'] = email_from
    mimeMessage['Reply-To'] = email_from
    mimeMessage['subject'] = email_subject
    emailMsg = email_message
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    email_message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(email_message)

