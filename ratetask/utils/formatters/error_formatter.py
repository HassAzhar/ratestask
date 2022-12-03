import json

# For more understandable error messages. Would be reusable in a larger project
def error_formatter(message, status):
    error = {}
    error["message"] = message
    error["status"] = status
    return json.dumps(error)
