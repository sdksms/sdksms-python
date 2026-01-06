# Python Example (Requires requests library)
import hashlib
import time
import json
import requests

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

userName = 'lsgy'
password = 'VWjFR'
timestamp = int(time.time() * 1000)

# Calculate Sign
sign = md5(userName + str(timestamp) + md5(password))

data = {
    "userName": userName,
    "timestamp": timestamp,
    "sign": sign,
    "messageList": [
        {"phone": "15011111111", "content": "[Signature] SMS Content 1"},
        {"phone": "15022222222", "content": "[Signature] SMS Content 2"}
    ]
}

url = "https://sdksms.com/api/sendMessageOne"
headers = {'Content-Type': 'application/json;charset=utf-8'}

try:
    response = requests.post(url, json=data, headers=headers)
    print(response.text)
except Exception as e:
    print(e)
