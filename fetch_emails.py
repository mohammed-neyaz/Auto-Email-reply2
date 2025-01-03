
import imaplib
import email
from email.header import decode_header
import json

def clean(text):
    return "".join(char if char.isalnum() else "_" for char in text)

def fetch_emails(email_user, email_password):
    emails = []

    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(email_user, email_password)
    imap.select("inbox")

    status, messages = imap.search(None, "ALL")
    email_ids = messages[0].split()

    for email_id in email_ids:
        res, msg = imap.fetch(email_id, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                from_ = msg.get("From")
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain" and part.get("Content-Disposition") is None:
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()

                emails.append({"from": from_, "subject": subject, "body": body})

    imap.close()
    imap.logout()
    return emails
