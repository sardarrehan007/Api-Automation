import requests
import json


Base_URL = 'http://0efb80c845d1.ngrok.io/admin/admin_login'
json_open = open('Login.json', 'r')
json_read = json_open.read()
json_load = json.loads(json_read)
valid = json_load['valid']

response = requests.post(Base_URL , valid)
token= (json.dumps(response.json(), indent=4))