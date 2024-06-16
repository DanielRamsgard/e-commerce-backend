import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

message = Mail(from_email="daniel.ramsgard@unc.edu",
               to_emails="dramsgard@gmail.com",
               subject="Sendgrid",
               plain_text_content="This is a sendgrid email",
               html_content="<p> Hello World </p>"
               )

try:
    sg = SendGridAPIClient(os.getenv('API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print(e)