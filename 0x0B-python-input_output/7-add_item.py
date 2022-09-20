#!/usr/bin/python3
"""this module has a script that adds args to a Python list in a file"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    coollist = load_from_json_file(file)
except:
    coollist = []
finally:
    for argument in sys.argv[1:]:
        coollist.append(argument)

save_to_json_file(coollist, file)
