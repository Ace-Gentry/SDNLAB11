import datetime
import json
import os
import netmiko
import paramiko
import requests
import getpass

from getpass import getpass
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

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

devtoken = print(response.text)

#Device list API

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Token': devtoken,
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response2 = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response2.text)
