# Convert a Python dictionary into a JSON-formatted string and a JSON file
# Note: py_to_json contains functions to convert and write to file
# - separate so the code can be reused
# file is written to dict_to_json.json
import py_to_json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# Convert and print the JSON string
json_string = py_to_json.convert_dict_to_json(servers_dict)
print(json_string)

# Write to a file
py_to_json.write_json_to_file(servers_dict, "dict_to_json.json")

# Note: json file looks the same as python dict, but it is now a json STRING