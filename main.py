import smtplib, ssl, email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import csv

# password = input("Type your password and press enter: ")
subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
password = "***"
sender_email = "mailt6246@gmail.com"
receiver_email = "vika41130@gmail.com"

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email

part = None # attachment
part1 = None # plain
part2 = None # html

# Add body to email
message.attach(MIMEText(body, "plain"))
filename = "assets/porche.jpg"  # In same directory as script

# Open file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    "attachment; filename= {}".format(filename),
)

# Add attachment to message and convert message to string
message.attach(part)

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

html = """\
<html>
  <body>
    <p>
       <h3>Simple email with Python</h3><br>
       <a href="http://www.realpython.com">Real Python</a> has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()
port = 465  # For SSL
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)

    with open("assets/mail_list.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            print(f"Sending email to {name}")
            # Send email here
            server.sendmail(sender_email, email, message.as_string())
        # server.sendmail(sender_email, receiver_email, message.as_string())

