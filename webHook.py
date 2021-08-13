import requests
import json

local_url = 'http://4f9836ac50b3.ngrok.io/webhook'
local_url2 = 'http://4f9836ac50b3.ngrok.io/file'

data = {'Device': 'CSI-Connect',
         'Hydro Pump State': 'Good'}

local = requests.post(local_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

local2 = requests.post(local_url2, data=json.dumps(data), headers={'Content-Type': 'application/json'})
