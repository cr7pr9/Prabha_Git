import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from mimetypes import guess_type
from email.encoders import encode_base64
from getpass import getpass
from smtplib import SMTP


def get_email(email):
    if '<' in email:
        data = email.split('<')
        email = data[1].split('>')[0].strip()
    return email.strip()

class Email(object):
    def __init__(self, from_, to, subject, message, message_type='plain',
                 attachments=None, cc=None, message_encoding='us-ascii'):
        self.email = MIMEMultipart()
        self.email['From'] = from_
        self.email['To'] = to
        self.email['Subject'] = subject
        if cc is not None:
            self.email['Cc'] = cc
        text = MIMEText(message, message_type, message_encoding)
        self.email.attach(text)
        if attachments is not None:
            for filename in attachments:
                mimetype, encoding = guess_type(filename)
                mimetype = mimetype.split('/', 1)
                fp = open(filename, 'rb')
                attachment = MIMEBase(mimetype[0], mimetype[1])
                attachment.set_payload(fp.read())
                fp.close()
                encode_base64(attachment)
                attachment.add_header('Content-Disposition', 'attachment',
                                      filename=os.path.basename(filename))
                self.email.attach(attachment)

    def __str__(self):
        return self.email.as_string()


class EmailConnection(object):
    def __init__(self, server, username, password):
        if ':' in server:
            data = server.split(':')
            self.server = data[0]
            self.port = int(data[1])
        else:
            self.server = server
            self.port = 25
        self.username = username
        self.password = password
        self.connect()

    def connect(self):
        self.connection = SMTP(self.server, self.port)
        self.connection.ehlo()
        self.connection.starttls()
        self.connection.ehlo()
        self.connection.login(self.username, self.password)

    def send(self, message, from_=None, to=None):
        if type(message) == str:
            if from_ is None or to is None:
                raise ValueError('You need to specify `from_` and `to`')
            else:
                from_ = get_email(from_)
                to = get_email(to)
        else:
            from_ = message.email['From']
            if 'Cc' not in message.email:
                message.email['Cc'] = ''
            to_emails = [message.email['To']] + message.email['Cc'].split(',')
            to = [get_email(complete_email) for complete_email in to_emails]
            message = str(message)
        return self.connection.sendmail(from_, to, message)

    def close(self):
        self.connection.close()
#example_email_utils.py
#!/usr/bin/env python
# coding: utf-8

# This script asks your name, email, password, SMTP server and destination
# name/email. It'll send an email with this script's code as attachment and
# with a plain-text message. You can also pass `message_type='html'` in
# `Email()` to send HTML emails instead of plain text.
# You need email_utils.py to run it correctly. You can get it on:
#                 https://gist.github.com/1455741
# Copyright 2011-2020 Álvaro Justen [alvarojusten at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

import sys
from getpass import getpass
from email_utils import EmailConnection, Email


print ('I need some information...')
name = raw_input(' - Your name: ')
email = raw_input(' - Your e-mail: ')
password = getpass(' - Your password: ')
mail_server = raw_input(' - Your mail server: ')
to_email = raw_input(' - Destination email: ')
to_name = raw_input(' - Name of destination: ')
subject = 'Sending mail easily with Python'
message = 'here is the message body'
attachments = [sys.argv[0]]

print ('Connecting to server...')
server = EmailConnection(mail_server, email, password)
print ('Preparing the email...')
email = Email(from_='"%s" <%s>' % (name, email), #you can pass only email
              to='"%s" <%s>' % (to_name, to_email), #you can pass only email
              subject=subject, message=message, attachments=attachments)
print ('Sending...')
server.send(email)
print ('Disconnecting...')
server.close()
print ('Done!')
#send_mail.py
#!/usr/bin/env python3
# Script to send emails using Python using the command-line.
# Copyright 2020 Álvaro Justen [alvarojusten at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>
import argparse
import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(
    smtp_host, smtp_port, smtp_user, smtp_pass, from_address, to_addresses,
    subject, text, html=False
):
    # TODO: use `emails_utils` code
    message = MIMEMultipart()
    message["From"] = from_address
    message["To"] = ",".join(to_addresses)
    message["Subject"] = subject
    if html:
        message.attach(MIMEText(text, "html", "utf-8"))
    else:
        message.attach(MIMEText(text, "plain", "utf-8"))
    server = smtplib.SMTP(host=smtp_host, port=smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(from_address, to_addresses, message.as_string())
    server.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--html", action="store_true")
    parser.add_argument("--smtp-host", default=os.environ.get("SMTP_HOST"))
    parser.add_argument("--smtp-port", default=os.environ.get("SMTP_PORT", 587))
    parser.add_argument("--smtp-user", default=os.environ.get("SMTP_USER"))
    parser.add_argument("--smtp-pass", default=os.environ.get("SMTP_PASS"))
    parser.add_argument("from_address")
    parser.add_argument("to_addresses", help="If more than one, separate by comma")
    parser.add_argument("subject")
    parser.add_argument("message")
    args = parser.parse_args()

    if None in (args.smtp_host, args.smtp_port, args.smtp_user, args.smtp_pass):
        print("ERROR: missing SMTP configuration", file=sys.stderr)
        exit(1)

    to_addresses = [
        address.strip()
        for address in args.to_addresses.split(",")
        if address.strip()
    ]
    send_mail(
        smtp_host=args.smtp_host,
        smtp_port=args.smtp_port,
        smtp_user=args.smtp_user,
        smtp_pass=args.smtp_pass,
        from_address=args.from_address,
        to_addresses=to_addresses,
        subject=args.subject,
        text=args.message,
        html=args.html,
    )