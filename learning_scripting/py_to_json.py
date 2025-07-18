# Convert a Python dictionary into a JSON-formatted string and a JSON file
# - Convert this Python dictionary into a JSON-formatted string
# - Convert this Python dictionary to a JSON file

import json


def convert_dict_to_json(data_dict, indent=4):
    """
    Convert a Python dictionary to a JSON-formatted string.

    :param data_dict: The dictionary to convert.
    :param indent: Number of spaces for indentation in the output string.
    :return: JSON-formatted string.
    """
    return json.dumps(data_dict, indent=indent)

def write_json_to_file(data_dict, filename, indent=4):
    with open(filename, 'w') as f:
        json.dump(data_dict, f, indent=indent)