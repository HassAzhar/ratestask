import json

def error_formatter(message, status):
    error = {}
    error['message'] = message
    error['status'] = status
    return json.dumps(error)