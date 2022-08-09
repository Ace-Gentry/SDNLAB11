import datetime
import json
import os
import netmiko
import paramiko
import requests
import getpass
import pprint

from getpass import getpass
from pprint import pprint
from pathlib import Path
from requests.auth import HTTPBasicAuth

#Getpass
username = input("Username: ")
password = getpass("Enter your password: ")

#Token API
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.post(url, auth=HTTPBasicAuth(username, password), headers=headers, data=payload, verify=False)

devtoken = response.json()

token = devtoken['Token']

#Device list API

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Token': token,
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response2 = requests.get(url, headers=headers, data=payload, verify=False)

devicelistjson = response2.json()

pprint(devicelistjson)
