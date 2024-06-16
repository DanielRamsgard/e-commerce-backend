import os
import requests
from requests.structures import CaseInsensitiveDict
import os
from dotenv import load_dotenv

def send_res(email, address, total, item_list):
    load_dotenv()

    sendgrid_api_key = os.getenv('API_KEY')

    url = "https://api.sendgrid.com/v3/mail/send"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {sendgrid_api_key}"
    headers["Content-Type"] = "application/json"

    data = {
    "personalizations": [
        {
        "to": [
            {
            "email": f"{email}"
            }
        ],
        "subject": "Sendgrid",
        }
    ],
    "from": {
        "email": "Daniel.Ramsgard@unc.edu",
    },
    "content": [
        {
        "type": "text/plain",
        "value": f"Dear {email},\n\n Your order totalling ${total} for {item_list} will be shipped to {address} within 24 hours.",
        }
    ]
    }

    res = requests.post(url, headers=headers, json=data)