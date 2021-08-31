import requests
import json

local_url = 'https://5680-188-223-102-254.ngrok.io/webhook'

data = {'Device': 'CSI-Connect',
         'Hydro Pump State': 'Good'}

local = requests.post(local_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

