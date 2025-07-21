# Convert JSON file to a Python dictionary
import json

# Open and load JSON file
# 'r' - read access only
# with - good practice, closes file automatically after indented section
with open('servers.json', 'r') as jsonfile:
    servers_dict = json.load(jsonfile)

# Note: json.loads also exists. load: load from file, loads: load from string

print(servers_dict)
print(type(servers_dict))

print(f"Key and value: 'server1' = {servers_dict["server1"]}")


print(f"Key and value: 'server2' = {servers_dict["server2"]}")

