import requests
import json

local_url = 'http://8695a32d35a2.ngrok.io/webhook'

data = {'Device': 'CSI-Connect',
         'Hydro Pump State': 'Good'}

local = requests.post(local_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

