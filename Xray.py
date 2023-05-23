import json

import bcolors as bcolors
import requests

# Automated Refresh Token
from Refresh_Token import token

my_token = token
print(my_token)# result that include auth token
token_split = my_token.split()     # split the result
token_index = token_split[4]            # index of auth_token
auth_token = token_index.replace('"', '')   # auth token without extra information'''
print(auth_token)

# End Point and Auth_token
endpoint = "http://1499e3cd9494.ngrok.io/feedBack/M1feedback"  # end_point
head = {"Authorization": "Bearer %s" % auth_token}  # auth_token

# Input Data

user_id = input("user_id : ")


# Pass input data as a value to json key
data = {

    "user_id": user_id
}

# JSON Write
json_load = json.dumps(data)
json_file = open('Xray.json', 'w')
json_file.write(json_load)
json_file.close()

# JSON Read
json_file_read = open('Xray.json', 'r')
json_file_read1 = json_file_read.read()
json_load = json.loads(json_file_read1)

# Response
response = requests.get(endpoint, json=json_load,headers=head)
json_response = (json.dumps(response.json(), indent=4))
print(json_response)
print(response.status_code)

# Test Case Pass or Fail
json_response_split = json_response.split()
if json_response_split[2] == "true,":
    print( 'Test Case Status :' + bcolors.BLUEIC + ' Pass')
else:
    print('Test Case Status : ' + bcolors.FAIL + ' Fail')
