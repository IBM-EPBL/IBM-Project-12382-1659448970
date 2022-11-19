# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from dotenv import load_dotenv

load_dotenv()
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendmail(usermail,subject,content):
    message = Mail(from_email='karthikrajask5000@gmail.com',to_emails=usermail,subject=subject,html_content='<strong> {} </strong>'.format(content))
    try:
        sg = SendGridAPIClient("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")
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)