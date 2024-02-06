from django.test import TestCase
import requests
access_token = 'EAAzYNu24zkoBOzB4nHH5BMPo40CvugZBJstO0ySZAqXb3Gp4WsiqSf04l4cvR0hHuHZAuicsxIScHGrT4mkg9Kqx1ZBowzztK1Xq2klyoZCOAZAiyMlnzO81yQVcCa0RIYAr08DvSTh2WDNPUQH6ha2UCmZC5lJlE8sZBdF7LfI822Hz2XuPJAKE9dv2r1JCZCwEMYBhI69fqziIjetuVcwcZD'
url = 'https://graph.facebook.com/v18.0/238510749334858/messages'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}
data = {
    "messaging_product": "whatsapp",
    "to": "994557431498",
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {
            "code": "en_US"
        }
    }
}

response = requests.post(url, headers=headers, json=data)

print(response.text)