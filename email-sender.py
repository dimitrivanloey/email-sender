import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'John Doe'
email['to'] = 'johndoe@gmail.com'
email['subject'] = 'You just won an 1.000.oo dollars!'

email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummyaccount@gmail.com', 'testpw')
    smtp.send_message(email)
    print('all good!')