import json

def pretty_print(label, data):
    print(label, json.dumps(data, indent=2))
