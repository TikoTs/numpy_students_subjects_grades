import json
import sys


def read_data_from_json(file_path, key):
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)[key]
    except KeyError:
        print(f"The key: {key} does not exist in file: {file_path}")
        sys.exit()
