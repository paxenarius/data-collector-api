import json
import datetime
import urllib.request
from urllib.parse import urlencode
import urllib.parse
import requests

TOKEN_URL = 'https://bz-sandbox.opay-test.net/auth/token'
ACCESS_CODE_URL = 'https://bz-sandbox.opay-test.net/auth/access_code'
DEPOSIT_URL = 'https://bz-sandbox.opay-test.net/api/apc/deposit'


def get_access_code():
    print('getting access code')
    payload = {
        'public_key': 'public-key',
    }
    url_values = urllib.parse.urlencode(payload)
    full_url = ACCESS_CODE_URL + '?' + url_values
    respons = urllib.request.urlopen(full_url)
    print(respons.info())
    data = json.loads(respons.read().decode(respons.info().get_param('charset') or 'utf-8'))
    return data['access_code']


def get_token(access_code):
    print('getting token')
    headers = {'Content-Type': 'application/json'}
    data = {
        'private-key': 'private-key',
        'access_code': access_code,
    }
    r = requests.post(TOKEN_URL, data=data, headers=headers)
    print(r)
    return json.loads(r.text)['access_token']


def deposit_opay(token, timestamp):
    print('deposit money')
    headers = {
        'Authorization': 'token ' + token,
        'Content-type': 'application/json',
        'Accept': 'application/json',
        'Nonce': timestamp,
        'Idempotence-key': '3N2Y0NmFiNT',
        'Signature': 'ZTQwNzMzODNjYWI3N2Y0NmFiNTMzYjA2MmZjZTAiLCJleHAiO'

    }
    data = {
        "reference": "RTY34567FGH",
        "recipient_phone": "254721217172",
        "amount": 1
    }
    r = requests.get(DEPOSIT_URL, headers=headers, data=data)
    data = r.json()
    return data


def make_deposit(amount):
    access_code = get_access_code()
    token = get_token(access_code)
    if token:
        deposit = deposit_opay(token, timestamp=datetime.datetime.now())
        if deposit['status'] == '200':
            return True
    return False