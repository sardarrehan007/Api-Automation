import bcolors
import requests
import json

# Base URL
Base_URL = 'http://1499e3cd9494.ngrok.io/admin/admin_login'

# Open File
json_open = open('Login.json', 'r')
json_read = json_open.read()
json_load = json.loads(json_read)

# Array includes parent keys of json
array1 = ['valid']

# Array for executing all test cases
for i in array1:
    json_data = json_load[i] # use for loop increment
    print("Test Data")
    print(json_data)   # use to display input data
    response = requests.post(Base_URL, json=json_data)  # Pass Json data as a body
    print(json.dumps(response.json(), indent=4))   # Response
    print("Status Code")
    actual_result = str(response.status_code)    # Status Code
    print(actual_result)
    json_data_string = str(json_data)     # change status code type from var to string
    json_dump = json.dumps(json_data_string)
    json_split = json_dump.split()        # split string to access the status code
    savejson_status = json_split[5]
    expected_result = savejson_status.replace('}"', '')

    # Test Case Pass or Fail
    if actual_result == expected_result:
        print( 'Test Case Status :' + bcolors.BLUEIC + ' Pass' + bcolors.END)
    else:
        print( 'Test Case Status : ' + bcolors.FAIL + ' Fail' + bcolors.END)
