

import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail

# sg = sendgrid.SendGridAPIClient(
#     apikey=os.environ.get("SENDGRID_API_KEY")
# )
# sg = sendgrid.SendGridAPIClient(
#     api_key=""
# )
# from_email = Email(email="mailt6246@gmail.com")
# to_email = Email(email="vika41130@gmail.com")
# subject = "A test email from Sendgrid"
# content = Content(
#     "text/plain", "Here's a test email sent through Python"
# )
# mail = Mail(from_email, subject, to_email, content)
# response = sg.client.mail.send.post(request_body=mail.get())

message = Mail(
    from_email='mailt6246@gmail.com',
    to_emails='vika41130@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    sg = sendgrid.SendGridAPIClient("")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))
