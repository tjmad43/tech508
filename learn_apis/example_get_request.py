import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/ch13nd")

print(type(post_codes_req))
# type is a class - which will have methods
print(post_codes_req)

print(f"Status code: {post_codes_req.status_code}")
print(f"Headers: {post_codes_req.headers}")

print(f"Content: {post_codes_req.content}")
# 'b' in above (type checked below) stands for bytecode
print(type(post_codes_req.content))

print(f"JSON: {post_codes_req.json()}")
# json converted to python dictionary already
print(f"Data type of JSON: {type(post_codes_req.json())}")


print(f'Region: {post_codes_req.json()['result']['region']}')
# OR
#print(f'Region: {post_codes_req.json()['result']['region']}')

