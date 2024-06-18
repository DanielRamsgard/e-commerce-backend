import os
import requests
from requests.structures import CaseInsensitiveDict
import os
from dotenv import load_dotenv

def send_res(email, total, address, item_list):
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
        "subject": "Honey Order",
        }
    ],
    "from": {
        "email": "dramsgard@gmail.com",
    },
    "content": [
        {
        "type": "text/plain",
        "value": f"Dear {email},\n\nYour order totalling ${total} for {item_list} will be shipped to {address} within 72 hours.\n\nSincerely, \n\nDaniel Ramsgard\n3154478656\ndramsgard@gmail.com",
        }
    ]
    }

    requests.post(url, headers=headers, json=data)