#!/usr/bin/env python3
from email.message import EmailMessage
import os.path
import mimetypes
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path=""):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    if attachment_path!="":
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))
        ap.close()
    send_email(message,sender)

def send_email(message, sender):
    mail_server = smtplib.SMTP('localhost')
    #mail_server.login(sender, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()
