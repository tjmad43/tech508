# multiple postcodes at once
import requests
import json

# dumps - converts dict to json string to pass on as request body
json_body = json.dumps({'postcodes': ["CH1 3ND", "SY12 9HG", "CH4 7EN"]})
# specify that body is json
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())