from ratetask import app
from flask import request
import ratetask.validators.app_service_validators as app_service_validators
from ratetask.utils.error_formatter import error_formatter
from http import HTTPStatus
from voluptuous import Error as ValidationError

@app.route("/rates")
def average_rate():
    try:
        app_service_validators.rates_validator(request.args.to_dict())
        return ''
    except ValidationError as error_message:
        return error_formatter(error_message.__str__(), HTTPStatus.BAD_REQUEST)

    