import json


def load_file(filename: str, file_type: str) -> dict:
    if file_type == 'json':
        with open(filename, encoding='utf8') as json_file:
            file_content = json.load(json_file)
    return file_content
